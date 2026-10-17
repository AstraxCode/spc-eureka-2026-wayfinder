# Hasil dan Pembahasan-archonx

Bab ini menyajikan analisis ekspektasi performa perancangan sistem teleoperasi lengan robot 5-DOF
serta evaluasi kritis terhadap target kuantitatif yang telah dipra-registrasikan. Pembahasan disusun
dalam empat bagian: (i) pernyataan eksplisit status hasil dan komitmen integritas akademik, (ii) tabel
target kuantitatif pra-registrasi, (iii) analisis ekspektasi perancangan kendali dan transmisi nirkabel,
serta (iv) batasan operasional dan evaluasi kejujuran ilmiah.

## Pernyataan status hasil dan komitmen integritas akademik-archonx

Seluruh pemaparan, metrik performa, dan nilai numerik yang disajikan pada bab ini merupakan target
pra-registrasi (*pre-registered targets*) dan analisis ekspektasi berbasis perancangan teknis serta kajian
pustaka, bukan data hasil pengukuran empiris dari pengujian fisik prototipe. Penegasan ini disampaikan
secara eksplisit di awal bab berdasarkan dua pertimbangan fundamental:

1. *Jadwal realisasi prototipe:* Sesuai dengan jadwal kerja tim dan linimasa kompetisi yang diatur pada
   Buku Panduan Science Project Competition Eureka! ITB 2026 (hal. 4 dan hal. 13), perakitan akhir serta
   pengujian fisik kuantitatif prototipe dijadwalkan berlangsung pada 18 Oktober 2026 untuk persiapan tahap
   Final. Pada tahap penulisan dan pengumpulan draf Full Paper ini, data empiris fisik belum dihimpun.
2. *Kepatuhan integritas akademik:* Ketentuan umum Buku Panduan Eureka! ITB 2026 (hal. 5 butir 7) secara
   tegas menyatakan bahwa seluruh karya wajib menjunjung tinggi integritas akademik, dan segala bentuk
   fabrikasi data, falsifikasi data, maupun manipulasi hasil akan dikenakan sanksi berupa pengurangan
   nilai atau diskualifikasi langsung dari kompetisi. Menyajikan hasil rekayasa atau simulasi hipotetis
   seolah-olah merupakan data pengukuran riil merupakan pelanggaran integritas ilmiah yang tidak dapat
   dibenarkan.

Oleh karena itu, bab ini difokuskan pada analisis mendalam terhadap kelayakan perancangan (*design feasibility*),
mekanisme intervensi kendali yang diusulkan, dan rasionalisasi target kuantitatif terukur yang akan diuji
secara empiris pada tahap berikutnya menggunakan protokol eksperimen 2×2 yang telah dibakukan pada bab Metodologi.

## Target kuantitatif pra-registrasi-archonx

Untuk menyediakan kriteria pengujian yang objektif, transparan, dan dapat diverifikasi secara independen,
tim menetapkan serangkaian target kinerja kuantitatif sebelum pengujian fisik dilaksanakan. Target-target
ini ditabulasikan pada Tabel 1.

Tabel 1. Matriks target kuantitatif pra-registrasi sistem teleoperasi lengan robot 5-DOF-archonx

| Parameter / Metrik | Kondisi Pengujian | Nilai Target Pra-registrasi | Rasionalisasi & Dasar Teori | Metode Verifikasi |
|---|---|---|---|---|
| Latensi transmisi satu arah (*t_latency*) | Jarak 1 m dan 3 m, Wi-Fi 2,4 GHz (UDP) | ≤ 200 ms | Ambang batas persepsi kendali semi-real-time operator; mengantisipasi variabilitas propagasi dalam ruangan (Akl et al. 2006 [8]; Pandey & Parasuraman 2021 [9]) | Selisih penandaan waktu mikrokontroler: Persamaan (4) (*t_receive* − *t_send*) |
| Galat penempatan *end-effector* Euclidean (*e*) | Kondisi B (stik + mode posisi-halus) | Dalam batas 1 sel kisi uji target (*e* ≤ ukuran sel kisi target) | Resolusi kendali sudut mikro via modulasi PWM 12-bit PCA9685 dan penskalaan gerak halus (Richter et al. 2019 [4]; Han & Yang 2022 [3]) | Pengukuran jarak Euclidean via foto tegak lurus ponsel terhadap kisi milimeter: Persamaan (5) |
| Tingkat keberhasilan penahanan posisi (*success rate*) | Kondisi A dan Kondisi B (40 pengulangan per operator, 3 operator) | Kriteria proyek: ≥ 8 dari 10 percobaan (80%) stabil selama 2 detik | Kriteria keberhasilan berbasis waktu penahanan proyek (*project-defined criterion*) untuk menguji kestabilan pelepasan tuas | Pencatatan durasi penahanan stabil objek di area target tanpa *slip* atau osilasi berlebih |
| Performa komparatif antarmuka | Kondisi B relatif terhadap Kondisi A | Penurunan nilai rata-rata galat (*x̄_B* < *x̄_A*) dan penurunan deviasi standar (*s_B* < *s_A*) | Hipotesis intervensi mode posisi-halus menurunkan fenomena *hunting* dan lonjakan koreksi operator dekat sasaran | Analisis statistik sampel: Persamaan (6) untuk rata-rata dan Persamaan (7) untuk simpangan baku |

Penetapan target latensi ≤ 200 ms dan galat penempatan dalam batas satu sel kisi target merupakan target
internal tim yang didasarkan pada batasan arsitektur perangkat keras dan kajian teleoperasi yang telah
didokumentasikan dalam *claim ledger* proyek (`claim-ledger-archonx.md`).

## Analisis ekspektasi perancangan kendali dan teleoperasi-archonx

### 1. Dinamika intervensi mode posisi-halus dan stabilitas operator-archonx

Ekspektasi utama dari perancangan sistem ini adalah peningkatan akurasi penempatan objek secara signifikan
ketika operator mengaktifkan mode posisi-halus (Kondisi B) dibandingkan kendali stik standar (Kondisi A).
Rasionalisasi mekanistik dari ekspektasi ini bertumpu pada interaksi antara keterbatasan neuromuskular
operator dan resolusi perintah aktuator.

Pada pengoperasian stik analog konvensional (Kondisi A), simpangan fisik tuas stik dipetakan langsung
menurut gain konstan (*K_coarse*) sesuai Persamaan (2). Dalam fase pendekatan akhir (*docking*) saat capit
berada beberapa milimeter di atas sasaran, defleksi jempol operator sebesar pecahan milimeter menghasilkan
kecepatan sudut sendi yang relatif kasar. Upaya operator untuk melakukan koreksi posisi mikro kerap kali
menghasilkan koreksi berlebih (*overshooting*), memicu fenomena *operator-induced oscillation* atau *hunting*.
Operator terpaksa mengoreksi posisi secara berulang-ulang, yang berpotensi menyebabkan ketidakstabilan
atau benturan dengan batas target.

Sebaliknya, pada Kondisi B, penekanan tombol pemicu (*trigger*) mengaktifkan faktor reduksi gain α
(0 < α < 1) sesuai Persamaan (3). Ekspektasi perilaku sistem pada mode ini mencakup:
1. *Peningkatan resolusi fisik antarmuka:* Rentang gerak fisik tuas stik yang sama menghasilkan perubahan
   sudut servo yang jauh lebih kecil (*v_fine = α · K_coarse · δ_stick*). Hal ini memperluas rentang toleransi
   kinestetik tangan operator, memungkinkan pergerakan mikro berkecepatan rendah yang stabil di dekat sasaran.
   Prinsip penskalaan gerak ini konsisten dengan literatur teleoperasi bedah mikro (Richter et al. 2019 [4])
   dan teleoperasi penanganan bahan nuklir (Han & Yang 2022 [3]), di mana penskalaan gerak terbukti
   menurunkan tingkat galat operator secara terukur.
2. *Peniadaan kebutuhan kopling perangkat keras (release-to-hold):* Di bawah kendali laju (*rate control*),
   ketika tuas stik dilepaskan ke titik netral (dibantu oleh pegas internal stik), nilai *δ_stick* bernilai nol,
   sehingga kecepatan sudut perintah menjadi nol (*v_arm = 0*). *Firmware* mikrokontroler secara otomatis
   mempertahankan sudut perintah terakhir pada register PWM PCA9685. Karakteristik ini berfungsi sebagai
   pengunci posisi alami (*natural position hold*) tanpa memerlukan mekanisme kopling fisik (*hardware clutch*)
   atau rem elektromagnetik tambahan yang dapat menambah bobot serta kompleksitas biaya lengan robot.

### 2. Karakteristik transmisi nirkabel Wi-Fi 2,4 GHz dan latensi teleoperasi-archonx

Arsitektur teleoperasi nirkabel proyek ini mengandalkan komunikasi radio Wi-Fi 2,4 GHz langsung (protokol UDP)
antara ESP32 sisi pengirim dan ESP32 sisi penerima. Evaluasi perancangan jaringan menghasilkan ekspektasi
berikut:
- *Pengaruh jarak dan rugi propagasi:* Berdasarkan model rugi propagasi dalam ruangan Akl, Tummala, dan Li (2006)
  [8], daya sinyal rata-rata yang diterima menurun secara logaritmik terhadap jarak (*PL ∝ 10·n·log₁₀(d)*),
  dengan eksponen *n* berada pada rentang 1,2 hingga 8 tergantung pada sekat dan material ruangan. Pada jarak
  pengujian laboratorium (1 m dan 3 m tanpa halangan dinding masif), penurunan daya sinyal diperkirakan tidak
  mencapai batas ambang putus (*drop-off*), namun peningkatan jarak berpotensi meningkatkan variasi waktu
  tempuh paket data.
- *Variabilitas latensi (jitter):* Sebagaimana dilaporkan oleh Pandey dan Parasuraman (2021) [9] dalam studi
  empiris teleoperasi robot bergerak melalui Wi-Fi 2,4 GHz, delay transmisi memiliki variabilitas yang tinggi,
  di mana nilai simpangan baku delay kerap kali setara atau bahkan melampaui nilai rata-ratanya akibat interferensi
  kanal nirkabel dan *queuing*. Oleh karena itu, target pra-registrasi latensi satu arah ≤ 200 ms ditetapkan
  sebagai batas atas desain sistem. Latensi di bawah 200 ms diekspektasikan mempertahankan persepsi kontinuitas
  kendali bagi operator manusia, mencegah operator beralih ke pola pengoperasian diskrit ("gerak lalu tunggu")
  yang menurunkan efisiensi tugas penempatan secara drastis.

## Batasan operasional dan evaluasi kejujuran ilmiah-archonx

Untuk menjaga kejujuran ilmiah dan mencegah misinterpretasi terhadap capaian proyek ini, batasan-batasan
berikut harus dinyatakan secara transparan:

### 1. Batasan pembuktian konsep skala meja (tabletop proof of concept)-archonx

Sistem teleoperasi yang dikembangkan dalam penelitian ini secara murni merupakan pembuktian konsep skala
meja (*tabletop proof of concept*) yang memanfaatkan objek uji laboratorium berupa balok busa sintetis
berdimensi 30 mm × 30 mm × 30 mm.

Sistem ini sama sekali **tidak ditujukan dan tidak diklaim** mampu menangani batang bahan bakar nuklir riil
(*real spent nuclear fuel rods*). Penanganan bahan bakar nuklir bekas riil pada fasilitas nuklir beroperasi
di bawah kondisi ekstrem yang sangat berbeda dari lingkungan laboratorium skala meja, sebagaimana dipaparkan
dalam dokumen teknis IAEA-TECDOC-1433 [1] dan IAEA Radiation [2]:
- *Beban mekanik masif:* Batang bahan bakar nuklir atau bundel bahan bakar memiliki bobot puluhan kilogram
  hingga hitungan ton, memerlukan manipulator hidrolik atau elektro-mekanik berkekuatan tinggi, bukan motor
  servo hobi berdaya rendah.
- *Lingkungan radiasi pengion gamma ekstrem:* Paparan fluks radiasi tinggi dari produk fisi menyebabkan
  degradasi cepat pada komponen elektronik semikonduktor standar (ESP32, modul I2C) dan material polimer
  plastik cetak 3D. Manipulator nuklir sesungguhnya memanfaatkan komponen elektronik khusus tahan radiasi
  (*radiation-hardened*), kabel pelindung timbal, atau perpanjangan mekanik melalui dinding perisai tebal (*hot cell*).
- *Tingkat keandalan dan redundansi:* Fasilitas industri nuklir menuntut sistem kendali berlebih (*fail-safe
  redundancy*), sensor umpan balik multi-kanal, dan sertifikasi keselamatan ketat untuk mencegah kecelakaan fatal.

Lengan robot dalam karya ini semata-mata menguji kelayakan integrasi antarmuka stik terjangkau dan keefektifan
algoritma kendali mode posisi-halus pada manipulasi presisi jarak jauh berskala miniatur.

### 2. Keterbatasan sistem loop terbuka (open-loop) dan aktuator-archonx

Arsitektur mekanik dan elektronik lengan robot beroperasi secara loop terbuka penuh (*strictly open-loop*).
Modul PCA9685 membangkitkan sinyal modulasi lebar pulsa (PWM) menuju 5 unit motor servo TowerPro MG996R tanpa
adanya sensor umpan balik posisi sendi absolut (enkoder), sensor gaya sentuh pada capit (*gripper*), maupun
pengukuran arus motor.

Konsekuensi dari keterbatasan loop terbuka ini meliputi:
- *Galat mekanik tak terkompensasi:* Keausan pada roda gigi motor servo, celah mekanik (*backlash*), dan defleksi
  lentur pada struktur lengan cetak 3D tidak dapat dikoreksi secara otomatis oleh sistem kendali.
- *Beban kognitif operator:* Operator memikul seluruh tanggung jawab loop umpan balik melalui pengamatan visual
  langsung dari jarak jauh. Ketiadaan umpan balik gaya (*haptic feedback*) mengharuskan operator memperkirakan
  kekuatan cengkeraman secara visual guna menghindari deformasi objek uji atau *stall* pada motor servo capit.
Presisi sistem ini sepenuhnya bersandar pada kehalusan modulasi perintah dari operator dan batasan keamanan
sudut yang diprogram pada *firmware*.

### 3. Penegasan status ketiadaan data fisik sebelum 18 Oktober 2026-archonx

Ditegaskan kembali bahwa tidak ada angka hasil pengukuran fisik kuantitatif (seperti galat milimeter terukur,
waktu penyelesaian tugas riil, atau latensi milidetik aktual) yang dilaporkan dalam draf dokumen ini sebelum
pelaksanaan perakitan fisik pada 18 Oktober 2026.

Pilihan ini diambil secara sadar untuk menegakkan standar etika penelitian yang tinggi dan mematuhi aturan
Buku Panduan SPC Eureka! ITB 2026 hal. 5 butir 7, di mana tindakan manipulasi hasil atau fabrikasi data berakibat
pada sanksi pengurangan nilai atau diskualifikasi langsung. Protokol validasi 2×2 dengan alokasi 40 percobaan
per kondisi per operator dirancang secara ketat sebagai instrumen pengujian objektif yang siap dijalankan dan
didokumentasikan secara transparan pada tahap Final mendatang (Buku Panduan hal. 4 dan 13).

## Catatan draf (scaffolding — hapus saat perakitan, ticket 20)-archonx

- Penomoran tabel dan persamaan: Tabel 1 menyajikan matriks target pra-registrasi. Persamaan yang dirujuk
  melanjutkan bab sebelumnya: Persamaan (2) dan (3) pada Dasar Teori (pemetaan kasar dan halus), serta
  Persamaan (4)–(7) pada Metodologi (latensi satu arah, galat Euclidean, rata-rata sampel, dan simpangan baku).
- Peta klaim → ledger:
  - Pernyataan komitmen integritas & larangan fabrikasi = Buku Panduan SPC Eureka! ITB 2026 hal. 5 butir 7.
  - S1 (IAEA-TECDOC-1433) & S2 (IAEA Radiation) = batasan bahan bakar nuklir riil vs *tabletop POC*.
  - S3 (Akl et al. 2006) = rugi propagasi Wi-Fi 2,4 GHz / C5.
  - S4 (Pandey & Parasuraman 2021) = variabilitas latensi Wi-Fi teleoperasi robot / C6.
  - S8 (PS2X) = arsitektur mikrokontroler pengirim ter-polling / C11.
  - S9 (Richter et al. 2019) & S10 (Han & Yang 2022) = dasar ekspektasi efektivitas penskalaan gerak / C14, C15.
  - Target latensi satu arah ≤ 200 ms = *pre-registered in-team target*.
  - Target galat penempatan dalam batas satu sel kisi target = *pre-registered in-team target*.
  - Kriteria penahanan 2 detik (8 dari 10 berhasil) = *project-defined criterion*.
- Verifikasi kepatuhan konten terlarang: merujuk secara ketat pada kriteria pengujian dokumen `spec.md` →
  Testing Decisions butir 7 (nol kemunculan istilah antarmuka usang atau antarmuka layar sentuh sebagai
  antarmuka sistem utama).
- Seluruh pernyataan hasil dibingkai secara ketat sebagai analisis ekspektasi dan target pra-registrasi
  (nol klaim data terukur empiris).