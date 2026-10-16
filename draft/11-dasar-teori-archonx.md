# Dasar Teori-archonx

Bagian ini menyusun landasan yang dipakai solusi, bukan survei. Tiga hal yang harus dijawabnya:
mengapa penempatan presisi sulit pada teleoperasi, apa yang sudah dibuktikan literatur tentang
penskalaan gerak dan kendali hibrida posisi–laju, dan dasar fisika yang menghubungkan jarak dengan
latensi. Setiap klaim luar pada bagian ini dipetakan ke satu entri di `claim-ledger-archonx.md`; tidak
ada angka yang masuk tanpa sumber atau tanpa label target pra-registrasi.

## Teleoperasi dan batas akurasi penempatan-archonx

Teleoperasi berarti operator tetap berada di dalam lingkar kendali untuk setiap gerakan; tidak ada
bagian tugas yang dijalankan otomatis. Pada penanganan bahan radioaktif, alasan teleoperasi bukan
kenyamanan melainkan dosis: operator harus berdiri di luar jangkauan sumber, sehingga seluruh presisi
penempatan harus berasal dari antarmuka dan bukan dari tangan operator yang menyentuh objek. Konsekuensinya,
mutu teleoperasi diukur dari galat penempatan akhir, bukan dari kelancaran gerak.

Kesulitan utamanya adalah pertukaran antara kecepatan pendekatan dan resolusi gerak halus. Laju
kendali yang besar mempercepat pendekatan tetapi memperkasar setiap koreksi kecil di dekat sasaran;
laju kendali yang kecil memperhalus koreksi tetapi memaksa operator melakukan gerakan berulang. Dua
hukum kendali klasik yang dipakai untuk mengatasinya adalah kendali posisi dan kendali laju. Kendali
posisi memberi hubungan langsung antara perpindahan masukan dan posisi sendi sehingga terasa
transparan, tetapi jangkauan pergerakan masukan yang tetap membuatnya boros gerakan pengulangan.
Kendali laju memetakan perpindahan masukan menjadi kecepatan sehingga pendekatan ke sasaran menjadi
mudah, tetapi transparansinya buruk tepat di dekat sasaran karena operator kehilangan rasa posisi.[3]

## Penskalaan gerak dan kendali hibrida posisi–laju-archonx

Literatur yang paling relevan bagi solusi ini bukan manipulasi otonom, melainkan teleoperasi yang
dipandu manusia dan diperkuat oleh penskalaan gerak serta pergantian mode kendali.

Han dan Yang meneliti tugas teleoperasi penanganan bahan bakar nuklir dan merumuskan kompromi di atas
secara eksplisit: skala posisi yang rendah memberi gerak beresolusi tinggi tetapi menuntut banyak
operasi pengulangan, sedangkan skala tinggi mempercepat pendekatan tetapi menurunkan resolusi; kendali
laju mendekati sasaran dengan nyaman tetapi kurang transparan di dekatnya. Mereka memakai strategi
"bubble" dari literatur sebelumnya, yaitu kendali laju di luar radius sasaran dan kendali posisi di
dalamnya, dan melaporkan bahwa pengendali hibrida posisi–laju dengan dekomposisi tugas memangkas waktu
penyelesaian 17,23% dan beban kerja NASA-TLX 34,02% dibanding kendali posisi konvensional.[3]

Richter, Orosco, dan Yip menguji tiga solusi penskalaan gerak pada sistem da Vinci dengan 17 peserta di
bawah pengaruh delay. Strategi posisi menurunkan skala saat perangkat slave mendekati rintangan, sedangkan
strategi kecepatan menaikkan skala seiring kecepatan operator sehingga skala tetap rendah pada gerakan
kecil yang presisi dan lebih tinggi pada gerakan cepat. Kedua strategi melaporkan tingkat galat yang lebih
rendah dengan konsekuensi waktu tugas yang lebih panjang, dan 16 dari 17 peserta mencapai tingkat galat
terbaiknya memakai salah satu solusi yang diusulkan.[4] Studi ini adalah preseden langsung untuk mode
penempatan halus di dekat sasaran, meskipun penginderaan rintangan dan tata letak pembedahannya berbeda
dari lengan meja yang dipakai proyek ini.

Lee, Han, dan Yang mengusulkan kerangka penskalaan variabel yang dipilih menurut fase tugas
(kontak dan non-kontak), dan melaporkan penurunan gaya kontak, waktu penyelesaian, serta beban kerja
yang dirasakan dibanding penskalaan tetap. Teks penuhnya berbayar dan hanya abstraknya yang dapat
diakses, sehingga temuan ini dipakai pada tingkat abstrak saja tanpa mengutip angkanya.[5]

Yoon dkk. memakai klasifikasi niat kasar–halus dengan skala adaptif dan melaporkan penurunan jumlah
operasi pengulangan 38,46%, waktu penyelesaian 11,96%, dan NASA-TLX 58,01% dibanding skala tunggal yang
tetap. Perlu dicatat bahwa filter lolos-rendah pada studi itu diterapkan pada faktor skala, bukan pada
aliran perintah operator mentah.[6]

Ketiga sumber ini menetapkan bahwa penurunan gain di dekat sasaran adalah preseden yang berdasar,
bukan penemuan tanpa rujukan. Solusi proyek ini memakai penurunan gain yang sama sebagai mode
posisi-halus, dengan dua perbedaan yang disengaja: mode ini dipicu operator melalui pemicu pengendali
alih-alih otomatis dari penginderaan sasaran, dan perilaku tahan setelah pelepasan menggantikan kopling
perangkat keras yang lazim di literatur.

## Pemulusan sinyal perintah: apa yang sudah dan belum dibuktikan-archonx

Pemulusan perintah sering diasumsikan memperbaiki akurasi, dan asumsi itu perlu diperiksa karena
solusi ini tidak memakainya.

Wang, Zhang, dan Zhang membandingkan delapan filter deret waktu (termasuk Savitzky–Golay, median,
Kalman, dan rata-rata bergerak berbobot) untuk teleoperasi penangkapan gerak berbasis kamera RGB-D.
Studi itu mengevaluasi kompleksitas waktu, galat absolut rata-rata, variansi, dan RMSE, serta melaporkan
lintasan yang lebih halus pada uji teleoperasi tulisan tangan. Abstrak studi tersebut tidak melaporkan
kajian galat penempatan atau pemerolehan sasaran.[7] Dengan demikian, bukti yang ada mendukung
pengurangan osilasi masukan, bukan perbaikan akurasi tugas.

**Tidak ditemukan bukti langsung bahwa pemulusan perintah semata meningkatkan akurasi penempatan.**
Karena itu, pemulusan diperlakukan sebagai hipotesis, bukan sebagai efek yang sudah terbukti. Mode
posisi-halus proyek ini bukan filter dan tidak dipresentasikan sebagai filter: ia menurunkan gain
perintah, dan klaim yang dibuat terbatas pada apa yang diukur pada tahap pengujian.

## Mekanika sendi dan pemetaan perintah ke sudut sendi-archonx

Lengan digerakkan dengan memutar servo pada tiap sendi dan gripper. Beban lengan dan beban objek
menimbulkan gaya gravitasi ke bawah, sehingga untuk mengangkat sendi atas diperlukan torsi yang
melebihi torsi gravitasi pada lengan. Torsi yang dihasilkan motor dinyatakan sebagai

τ = kτ · I    (1)

Keterangan: τ adalah torsi motor (N·m), kτ konstanta torsi motor (N·m/A), dan I arus motor (A).
Persamaan ini dipakai sebagai dasar pemilihan aktuator, bukan sebagai kuantifikasi pengukuran pada
laporan ini.

Perintah operator dipetakan ke sudut sendi melalui pemetaan kasar sebagai berikut.

θ_cmd = clamp[θ_ref + G · u, θ_min, θ_max]    (2)

Keterangan: θ_cmd adalah sudut sendi yang diperintahkan, u adalah besar perpindahan masukan operator
yang dinormalkan, θ_ref adalah sudut acuan, G adalah gain kasar dari perintah ke sendi, θ_min dan θ_max
adalah batas sudut sendi yang diizinkan, dan clamp membatasi nilai agar tetap berada di antara kedua
batas tersebut. Pemetaan ini sengaja ditulis tidak bergantung perangkat: perpindahan masukan dapat
berupa perpindahan stik dan dapat pula berupa besaran lain, dan G yang menentukan seberapa besar
gerakan sendi yang dihasilkan.

Mode posisi-halus menurunkan gain pada persamaan tersebut dengan faktor α yang lebih kecil dari satu,
sehingga besar perpindahan masukan yang sama menghasilkan gerakan sendi yang lebih kecil.

θ_cmd,halus = clamp[θ_ref + α · G · u, θ_min, θ_max],  0 < α < 1    (3)

Nilai α adalah parameter firmware, bukan klaim pada laporan ini. Batas θ_min dan θ_max diterapkan pada
kedua mode sebagai bentuk keamanan, dan pemberhentian perintah saat sambungan terputus memakai acuan
yang sama.

## Propagasi Wi-Fi 2,4 GHz sebagai sumber variasi latensi-archonx

Jarak dijadikan variabel pengujian karena daya sinyal yang diterima menurun terhadap jarak. Akl, Tummala,
dan Li menunjukkan bahwa daya sinyal rata-rata menurun secara logaritmik terhadap jarak, dengan
eksponen kehilangan jalur n antara 1,2 dan 8 (nilai 2 pada ruang bebas, dan lebih besar ketika terdapat
penghalang), serta menegaskan bahwa kanal dalam ruangan sangat bergantung pada letak dinding dan
sekat.[8] Model kehilangan jalur itu menjelaskan mengapa jarak dan halangan mengubah mutu tautan,
tetapi tidak dapat memprediksi tautan proyek ini karena n dan simpangan bakunya bergantung lingkungan.

Pandey dan Parasuraman mengukur kinerja Wi-Fi 2,4 GHz pada robot bergerak dan melaporkan delay rata-rata
puluhan hingga ratusan milidetik, dengan simpangan baku yang pada beberapa kasus melebihi nilai
rata-ratanya, serta bergantung kuat pada penempatan titik akses dan kondisi tautan.[9] Temuan ini
mendukung pemilihan jarak sebagai variabel, dan sekaligus menjadi alasan mengapa sebaran latensi harus
dilaporkan bersama rata-ratanya, bukan rata-rata saja.

Kedua sumber menjelaskan mekanisme, bukan nilai tautan proyek ini. Latensi satu arah proyek ini
didefinisikan sebagai selisih waktu kirim dan waktu terima pada kedua mikrokontroler dan dilaporkan
sebagai target pra-registrasi, bukan sebagai angka literatur.

## Stik PS2 sebagai periferal terpolling-archonx

Pemilihan pengendali PS2 menimbulkan satu konsekuensi arsitektur yang perlu dijelaskan di sini: papan PS2
tidak mengirimkan data atas inisiatifnya sendiri. Pustaka PS2X (dan portnya untuk ESP32) membaca tombol
dan stik melalui antarmuka empat kabel yang melibatkan clock, command, attention/select, dan data, dengan
mikrokontroler hos sebagai pihak yang melakukan polling.[10] Karena itu, pengendali PS2 tidak dapat
dibaca tanpa mikrokontroler hos, dan mikrokontroler sisi pengirim pada arsitektur proyek ini ada karena
kebutuhan tersebut, bukan sebagai tambahan yang dapat dihapus.

Implikasi pengukuran yang perlu dicatat: karena waktu kirim ditandai pada saat pembacaan stik di sisi
pengirim, selang polling PS2X ikut berada di dalam jalur latensi. Selang itu belum diukur, sehingga tidak
ada angka yang boleh dituliskan untuknya; batas target latensi tetap target pra-registrasi.

## Catatan draf (scaffolding — hapus saat perakitan, ticket 20)-archonx

- Penomoran sitasi bersifat sementara: [1] dan [2] disediakan untuk Pendahuluan (IAEA), sehingga Dasar
  Teori mulai dari [3]; penomoran akhir dimiliki ticket 18 (Daftar Pustaka) dan ticket 20.
- Peta klaim → ledger: [3] = C14 (S10 Han & Yang 2022) · [4] = C15 (S9 Richter 2019) · [5] = C16
  (S11 Lee 2024, abstrak saja) · [6] = C17 (S12 Yoon 2025) · [7] = C18 (S13 Wang 2024) · [8] = C5
  (S3 Akl 2006) · [9] = C6 (S4 Pandey & Parasuraman) · [10] = C11 (S8 PS2X).
- Persamaan (1)–(3) milik bagian ini; persamaan latensi dan statistik dinomori ulang saat perakitan
  (ticket 13/20) agar tidak bertabrakan.
