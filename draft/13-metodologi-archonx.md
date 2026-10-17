# Metodologi-archonx

Bab ini menguraikan metodologi perancangan dan validasi sistem teleoperasi lengan robot 5-DOF.
Pemaparan dibagi menjadi tiga bagian utama: (i) arsitektur sistem kendali teleoperasi dari pengirim
hingga aktuator, (ii) spesifikasi intervensi kendali mode posisi-halus dan penguncian posisi saat tuas
netral, serta (iii) protokol eksperimen validasi 2×2 yang dirancang sebagai rencana pengujian pra-registrasi.
Seluruh variabel, target kuantitatif, dan batas kriteria pada bab ini dipetakan secara ketat ke dokumen
`claim-ledger-archonx.md`.

## Arsitektur sistem kendali teleoperasi-archonx

Sistem teleoperasi dirancang untuk memungkinkan operator mengendalikan lengan robot 5-DOF dari jarak
aman tanpa paparan langsung terhadap objek yang ditangani. Rantai kendali fisik yang dibangun mengikuti
urutan: **PS2 controller → sender ESP32 (PS2X) → Wi-Fi → receiver ESP32 → PCA9685 → MG996R servos**.
Rantai ini memisahkan subsistem operator di sisi pengirim dengan subsistem manipulator di sisi penerima
secara fisik dan nirkabel.

### 1. Subsistem operator (sisi pengirim)-archonx

Subsistem operator menggunakan unit pengendali PS2 berkabel sebagai antarmuka fisik tunggal. Pengendali
PS2 merupakan periferal ter-polling (*polled peripheral*) yang tidak dapat mentransmisikan data secara
mandiri ke jaringan, melainkan membutuhkan mikrokontroler hos untuk membaca status tuas dan tombolnya.[10]
Fungsi hos ini dijalankan oleh mikrokontroler pengirim (ESP32 pengirim) melalui komunikasi serial empat
kawat (*data, command, clock, attention/select*) dengan memanfaatkan pustaka PS2X.[10]

Tiga lapisan kendali diimplementasikan langsung pada *firmware* mikrokontroler pengirim:
1. *Lapisan kendali laju terkoordinasi (mode kasar):* simpangan tuas stik analog memetakan perintah laju
   kecepatan end-effector maju/mundur dan rotasi secara terkoordinasi pada multi-sendi.
2. *Lapisan seleksi sendi tunggal:* tombol aksi (△, ○, ✕, □) memilih artikulasi sendi tertentu, sehingga
   simpangan tuas stik berikutnya hanya menggerakkan sendi yang dipilih secara individual.
3. *Lapisan pengkondisian mode posisi-halus:* penekanan tombol pemicu (*trigger*) mengaktifkan pengali
   penurunan gain, dan pelepasan tuas ke titik tengah secara otomatis menghentikan laju perintah gerak.

Sebelum paket data perintah dikirimkan melalui gelombang radio Wi-Fi 2,4 GHz (protokol UDP), mikrokontroler
pengirim menyematkan tanda waktu pengiriman (*t_send*). Penandaan waktu tepat pada saat pembacaan stik
memastikan bahwa selang waktu *polling* mikrokontroler terhadap stik ikut terukur di dalam jalur latensi
secara konsisten baik pada kondisi dasar maupun intervensi.

### 2. Subsistem transmisi nirkabel dan manipulator (sisi penerima)-archonx

Paket kendali ditransmisikan melalui tautan Wi-Fi 2,4 GHz lokal ke mikrokontroler penerima (ESP32 penerima)
yang terpasang pada rangka manipulator. Begitu paket tiba, mikrokontroler penerima segera mencatat tanda
waktu penerimaan (*t_receive*) untuk keperluan kalkulasi latensi transmisi jaringan.

Mikrokontroler penerima bertugas menerjemahkan paket perintah menjadi sinyal modulasi lebar pulsa (PWM)
untuk menggerakkan 5 unit motor servo TowerPro MG996R pada lima sumbu gerak lengan (rotasi dasar, elevasi
bahu, elevasi siku, fleksi pergelangan, dan pencengkeram *gripper*). Komunikasi dari ESP32 penerima ke modul
driver servo PCA9685 berlangsung melalui bus I2C perangkat keras (frekuensi kerja PWM 50 Hz, resolusi
12-bit / 4096 tingkat pulsa).

Sisi penerima beroperasi secara lingkar terbuka (*open-loop*), yaitu tanpa penggunaan enkoder posisi absolut
maupun sensor umpan balik gaya tambahan. Presisi penempatan dan keamanan mekanik sepenuhnya mengandalkan
intervensi kendali di sisi operator serta pembatasan perangkat lunak (*software clamping*) pada rentang sudut
aman [θ_min, θ_max] yang tertanam pada *firmware* penerima.

Untuk menjamin kestabilan logika dan menghindari kegagalan sistem (*brownout reset*), sistem kelistrikan
menggunakan pemisahan catu daya:
- Catu daya logika teregulasi 5 V DC memasok daya mikrokontroler dan sirkuit logika driver PCA9685.
- Catu daya aktuator terpisah 6 V DC (kapasitas arus minimal 5 A kontinu) memasok daya khusus untuk rel
  daya motor servo.
- Kapasitor *bulk* elektrolit 1000 µF dipasang paralel pada rel daya servo guna meredam lonjakan arus
  sesaat (*transient spike*) ketika motor bergerak serempak atau mengalami torsi beban puncak, didukung
  kapasitor keramik *bypass* 0,1 µF untuk menyaring derau frekuensi tinggi.

## Spesifikasi intervensi kendali mode posisi-halus-archonx

Intervensi utama yang diajukan dalam penelitian ini adalah penyediaan **mode posisi-halus** (*fine-positioning
mode*) yang dipadukan dengan perilaku **tahan setelah pelepasan** (*release-to-hold*). Mekanisme ini
dirancang untuk mengatasi ketidakstabilan penempatan objek di dekat sasaran tanpa menambah komponen
perangkat keras sensorik pada manipulator.

### 1. Mekanisme penurunan gain (gain reduction)-archonx

Aktivasi mode posisi-halus dilakukan oleh operator secara sadar menggunakan tombol pemicu (*trigger*) pada
pengendali PS2. Tombol pemicu bertindak sebagai mekanisme tombol sakelar independen, terpisah dari pergerakan
tuas stik analog maupun penekanan tombol aksi seleksi sendi.

Pada kondisi kendali kasar (dasar), hubungan antara simpangan masukan operator dan perintah sudut sendi
mengikuti Persamaan (2) yang telah ditetapkan pada Dasar Teori:

θ_cmd = clamp[θ_ref + G · u, θ_min, θ_max]

Ketika tombol pemicu ditekan, sistem beralih ke mode posisi-halus dengan menerapkan faktor pelemahan gain α,
sebagaimana dirumuskan pada Persamaan (3):

θ_cmd,halus = clamp[θ_ref + α · G · u, θ_min, θ_max],  0 < α < 1

Dengan nilai α yang berada pada rentang 0 < α < 1 (ditetapkan sebagai parameter *firmware*), simpangan fisik
tuas stik yang sama akan menghasilkan perubahan sudut sendi yang jauh lebih kecil. Penurunan rasio gerak ini
memberikan resolusi spasial yang lebih tinggi bagi operator untuk melakukan penyesuaian akhir di atas area
sasaran, merujuk pada prinsip penskalaan gerak yang terbukti mereduksi galat penempatan pada studi teleoperasi
terdahulu.[4],[3]

### 2. Perilaku tahan setelah pelepasan (release-to-hold)-archonx

Di samping penurunan gain, mode kendali ini mengimplementasikan logika *release-to-hold*. Karena tuas stik
analog bekerja berdasarkan prinsip kendali laju (*rate control*), simpangan tuas dari titik tengah
merepresentasikan kecepatan gerak sendi. Ketika operator melepaskan tuas stik, pegas internal pengendali
secara otomatis mengembalikan tuas ke posisi tengah netral (u = 0), yang secara matematis menghasilkan
perintah laju nol.

Pada saat kondisi u = 0 terdeteksi, *firmware* menahan nilai sudut acuan terakhir (θ_ref = θ_terakhir) dan
mengunci keluaran register PWM pada sudut tersebut. Manipulator berhenti seketika di posisi terakhir tanpa
mengalami pergeseran (*drift*). Dalam penelitian ini, perilaku perangkat lunak *release-to-hold* diajukan
sebagai kontribusi desain berbiaya nol yang menggantikan fungsi kopling perangkat keras (*hardware clutch*)
yang lazim digunakan pada instrumen *master telemanipulator* konvensional.

### 3. Batas keamanan dan penanganan kegagalan-archonx

Intervensi perangkat lunak ini tidak mengabaikan lapisan keselamatan dasar:
- *Batas sudut (clamping):* Fungsi `clamp[θ_min, θ_max]` tetap aktif secara mutlak pada kedua mode kendali
  guna mencegah artikulasi melebihi batas fisik mekanik rangka cetak 3D.
- *Pencegahan tabrakan sinyal:* Pelepasan tuas stik saat mode posisi-halus aktif tidak akan melawan fungsi
  tombol henti darurat fisik yang memutus daya rel aktuator servo secara instan.
- *Pengawas koneksi (watchdog):* Jika paket data Wi-Fi tidak diterima oleh mikrokontroler penerima selama
  lebih dari batas waktu ambang (*timeout*), sistem penerima secara otomatis mempertahankan sudut terakhir
  dan membekukan pergerakan lengan hingga koneksi pulih.

## Protokol pengujian validasi 2×2-archonx

Seluruh prosedur pengujian divalidasi melalui rencana eksperimen faktorial 2×2 yang terstruktur dan
terstandardisasi. Karena pengujian eksperimental dijadwalkan pada tahap lanjutan setelah batas pengumpulan
naskah ini, seluruh metodologi pengujian disajikan secara jujur sebagai **rencana protokol validasi
pra-registrasi**. Luaran pengujian disajikan dalam bentuk target kuantitatif dan ekspektasi terarah, bukan
klaim data empiris yang telah diukur.

### 1. Rancangan faktorial dan kondisi pengujian-archonx

Protokol eksperimen mengevaluasi interaksi antara dua faktor perlakuan independen:
1. **Faktor antarmuka kendali (2 tingkat):**
   - *Kondisi A (dasar / baseline):* Kendali tuas stik PS2 mode kasar saja, tanpa aktivasi mode posisi-halus.
   - *Kondisi B (intervensi):* Kendali tuas stik PS2 dengan ketersediaan aktivasi mode posisi-halus via tombol pemicu.
2. **Faktor jarak teleoperasi (2 tingkat):**
   - Jarak 1 meter (garis pandang langsung tanpa halangan fisik).
   - Jarak 3 meter (kondisi jarak kerja teleoperasi yang memicu variasi atenuasi sinyal nirkabel).

Pemilihan jarak 1 meter dan 3 meter didasarkan pada landasan fisika propagasi gelombang elektromagnetik
dalam ruangan: daya sinyal nirkabel berkurang secara logaritmik terhadap jarak dan meningkatkan sebaran
latensi komunikasi.[8],[9]

### 2. Partisipan operator dan mitigasi bias pembelajaran-archonx

Eksperimen melibatkan **3 orang operator berpasangan** (*paired operators*), dengan rencana kontingensi
terdokumentasi berupa batas minimal **2 operator** (*fallback 2*) apabila kendala teknis di lapangan
terjadi. Setiap operator diwajibkan menyelesaikan seluruh kombinasi dari empat sel pengujian (Kondisi A 1 m,
Kondisi A 3 m, Kondisi B 1 m, Kondisi B 3 m).

Untuk meniadakan bias akibat efek pembelajaran (*learning effect*) atau kelelahan operator (*operator fatigue*),
urutan pelaksanaan kondisi diatur secara berimbang (*counterbalanced order*). Operator 1 memulai dari Kondisi A
lalu Kondisi B, sedangkan Operator 2 memulai dari Kondisi B lalu Kondisi A, dan Operator 3 menerapkan permutasi
urutan jarak pengujian secara silang.

### 3. Prosedur uji dan kriteria keberhasilan tahan 2 detik-archonx

Tugas eksperimental yang dilakukan adalah memindahkan balok busa berdensitas seragam (ukuran 30 mm × 30 mm × 30 mm,
massa ±15 gram) dari titik awal tetap menuju zona target pada papan kisi koordinat berjarak milimeter.

Setiap operator melakukan **40 kali pengulangan percobaan (*trials*) per kondisi per jarak**. Total percobaan
yang direncanakan adalah 3 operator × 4 sel kondisi × 40 pengulangan = 480 titik data uji.

Kriteria keberhasilan penempatan dievaluasi berdasarkan **kriteria tahan 2 detik (*2-second hold criterion*)**:
penempatan dinyatakan berhasil (*pass*) jika balok busa mampu bertahan stabil di atas target sasaran selama
minimal 2 detik tanpa tergelincir, jatuh, atau mengalami pergeseran posisi akibat osilasi lengan. Ambang batas
keberhasilan operasional ditetapkan sebesar **minimal 8 dari 10 percobaan sukses** pada setiap sesi pengujian.
Kriteria ini merupakan metrik keberhasilan yang dirumuskan secara internal oleh proyek (*project-defined criterion*),
dan tidak diposisikan sebagai metrik standar telemanipulasi industri.

### 4. Metrik evaluasi dan formulasi matematis-archonx

Evaluasi kinerja sistem teleoperasi diukur melalui tiga parameter utama:

#### a. Latensi transmisi satu arah (one-way latency)-archonx
Latensi satu arah didefinisikan sebagai selisih waktu antara pembacaan masukan pada mikrokontroler pengirim
dan penerimaan paket perintah pada mikrokontroler penerima:

t_latency = t_receive − t_send    (4)

Keterangan:
- t_latency : latensi transmisi jaringan satu arah (milidetik).
- t_send : tanda waktu saat mikrokontroler pengirim membaca status tuas stik via pustaka PS2X (milidetik).
- t_receive : tanda waktu saat mikrokontroler penerima menerima paket data kendali via Wi-Fi (milidetik).

Nilai latensi satu arah ini ditetapkan sebagai **target pra-registrasi internal tim sebesar ≤ 200 ms**,
dan tidak dikutip dari literatur eksternal.

#### b. Galat penempatan (placement error)-archonx
Galat penempatan objek diukur sebagai jarak Euclidean antara titik pusat fisik balok busa dengan titik pusat
lingkaran target pada papan kisi uji:

e = √[(x_final − x_target)² + (y_final − y_target)²]    (5)

Keterangan:
- e : galat jarak penempatan akhir (mm).
- (x_final, y_final) : koordinat pusat objek busa setelah pelepasan dan stabil selama 2 detik (mm).
- (x_target, y_target) : koordinat titik pusat zona target sasaran (mm).

Pengukuran koordinat (x_final, y_final) dilakukan secara objektif melalui pemotretan resolusi tinggi
menggunakan kamera ponsel cerdas dengan sudut tegak lurus (*perpendicular top-down photo*) terhadap papan kisi
terkalibrasi, kemudian dianalisis terhadap garis acuan kisi berketelitian 0,5 mm. Target performa pra-registrasi
yang dipatok adalah galat penempatan akhir berada di dalam batas toleransi satu sel kisi uji.

#### c. Analisis statistik data-archonx
Data galat penempatan dan latensi satu arah dari seluruh pengulangan diolah untuk mendapatkan nilai rata-rata
sampel dan simpangan baku guna memvalidasi stabilitas kendali:

x̄ = (1/n) · Σ xᵢ    (6)

s = √[ (1/(n − 1)) · Σ (xᵢ − x̄)² ]    (7)

Keterangan:
- xᵢ : nilai hasil pengukuran pada percobaan ke-i (latensi dalam ms atau galat dalam mm).
- x̄ : nilai rata-rata sampel pengukuran.
- s : simpangan baku sampel.
- n : jumlah total percobaan pada kondisi terkait (n = 40 pengulangan per sel pengujian per operator).

Penyajian data eksperimen wajib menyertakan nilai rata-rata dan simpangan baku secara serentak untuk memastikan
bahwa fluktuasi ekstrem atau ketidakstabilan transmisi jaringan tidak tersamarkan oleh nilai rata-rata semata.

### 5. Kontrol variabel eksperimen-archonx

Untuk memastikan validitas perbandingan antara Kondisi A dan Kondisi B, parameter berikut dijaga konstan:
- *Objek uji:* balok busa yang sama dengan dimensi 30 mm × 30 mm × 30 mm dan massa seragam.
- *Lingkungan nirkabel:* titik akses Wi-Fi bekerja pada saluran frekuensi 2,4 GHz yang sama dan ditempatkan
  pada posisi ketinggian tetap sepanjang seluruh pengujian.
- *Konfigurasi manipulator:* mekanik lengan robot cetak 3D, tegangan catu daya motor servo (6 V teregulasi),
  dan algoritma batas sudut *firmware* tidak diubah di antara kedua kondisi.
- *Tata letak target:* posisi titik awal pengambilan dan koordinat titik target sasaran berada pada jarak
  dan ketinggian meja kerja yang identik.

## Catatan draf (scaffolding — hapus saat perakitan, ticket 20)-archonx

- Penomoran persamaan melanjutkan Dasar Teori: Persamaan (1)–(3) berada pada Dasar Teori (torsi, pemetaan
  kasar, dan pemetaan posisi-halus). Metodologi memiliki Persamaan (4) untuk latensi transmisi, Persamaan (5)
  untuk galat penempatan Euclidean, Persamaan (6) untuk rata-rata sampel, dan Persamaan (7) untuk simpangan baku.
  Penomoran akhir dikonsolidasikan pada ticket 20.
- Peta klaim → ledger:
  - Rantai kendali & kebutuhan mikrokontroler pengirim ter-polling = C11 (S8 PS2X).
  - Penurunan daya sinyal Wi-Fi terhadap jarak = C5 (S3 Akl et al. 2006).
  - Variabilitas delay Wi-Fi pada robot = C6 (S4 Pandey & Parasuraman 2021).
  - Preseden penskalaan gerak = C14 & C15 (S10 Han & Yang 2022; S9 Richter et al. 2019).
  - Metrik latensi satu arah (t_receive − t_send) target ≤ 200 ms = pre-registered in-team target.
  - Kriteria tahan 2 detik (8 dari 10 berhasil) = project-defined criterion (bukan metrik standar).
  - Galat penempatan dalam satu sel kisi = pre-registered target.
- Verifikasi kepatuhan konten terlarang (merujuk pada kriteria pengujian spec.md → Testing Decisions
  butir 7): tidak ada penyebutan antarmuka usang atau antarmuka layar sentuh sebagai antarmuka sistem
  utama. Rantai kendali konsisten dengan ketetapan ticket 09.
