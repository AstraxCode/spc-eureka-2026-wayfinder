# Pendahuluan-archonx

Dosis radiasi pada pekerja yang menangani bahan radioaktif perlu ditekan, dan batasnya bukan anjuran.
Salah satu contoh penanganan semacam itu adalah penanganan bahan bakar pada reaktor nuklir, yang
kadar radiasinya perlu dikurangi pada setiap tahap. Panduan keselamatan menetapkan batas dosis pekerja
20 mSv per tahun — dirata-ratakan atas lima tahun,
tanpa melebihi 50 mSv pada satu tahun — serta 1 mSv per tahun bagi masyarakat umum, sementara analisis
UNSCEAR menunjukkan dosis tahunan rata-rata pekerja dari sumber buatan manusia sebesar 0,6 mSv.[1]
Alasan batas itu ketat bersifat biologis: radiasi pengion dapat mengionisasi DNA secara langsung maupun
melalui pembentukan radikal bebas, dan perubahan kimia yang ditimbulkannya dapat berujung pada kanker
atau kelainan genetika.[1] Karena paparan tidak dapat dihilangkan seluruhnya pada pekerjaan semacam ini,
jarak dan penghalang menjadi dua cara utama menekan dosis.

Penanganan jarak jauh sudah menjadi praktik, bukan gagasan baru. Sistem jarak jauh dipakai secara luas
pada fasilitas pengelolaan bahan bakar nuklir bekas, dan alasan yang dikutip untuk pemakaiannya adalah
pengurangan dosis pada pekerja, peningkatan kinerja operasi, serta pekerjaan yang berlangsung di dalam
selubung pelindung atau pengungkung.[2] Karena operator tidak lagi menyentuh objek, seluruh mutu gerakan
berpindah ke antarmuka kendali.

Perpindahan itu melahirkan masalah yang menjadi fokus penelitian ini: akurasi penempatan. Ketika lengan
dikendalikan dari jarak jauh, ketepatan berhenti di atas sasaran tidak lagi ditentukan oleh tangan
operator melainkan oleh cara perintah operator diterjemahkan menjadi gerakan sendi. Kehilangan presisi
saat penempatan pada penanganan bahan radioaktif berisiko pada bahan yang ditangani maupun pada
lingkungan sekitarnya, sehingga akurasi penempatan menjadi syarat kerja, bukan nilai tambah.
**Rumusan masalah penelitian ini adalah bagaimana meningkatkan akurasi penempatan pada penanganan bahan
radioaktif secara jarak jauh**; latar akurasi dan penanganan ini dipertahankan tanpa perubahan dari
rumusan semula.

Pekerjaan sebelumnya menjawab pertanyaan yang lebih sempit, yaitu antarmuka masukan mana yang
menghasilkan akurasi lebih tinggi; dua antarmuka masukan dibandingkan pada tugas yang sama. Perbandingan
itu tetap menjadi motivasi di sini, tetapi bukan lagi pertanyaan penelitiannya: hasil perbandingan
bergantung pada perangkat yang diuji dan tidak menjelaskan mengapa satu antarmuka lebih akurat daripada
yang lain. Celah yang disasar penelitian ini berbeda — **bagaimana bentuk perintah operator di dekat
sasaran**, bukan perangkat apa yang dipakai.

Tujuan proyek:

1. Mengembangkan lengan robot 5-DOF teleoperasi yang dikendalikan pengendali PS2.
2. Merancang mode posisi-halus, yaitu lapisan kendali yang menurunkan gain perintah ke sendi dan menahan
   posisi saat stik dikembalikan ke tengah.
3. Menguji pengaruh mode posisi-halus terhadap galat penempatan, keberhasilan tahan 2 detik, dan latensi
   satu arah pada jarak 1 m dan 3 m menurut protokol 2x2 yang ditetapkan di muka.

Kebaruan yang diajukan bersifat sisi-operator. Penurunan gain di dekat sasaran bukan hal baru di
literatur teleoperasi, tetapi literatur mencapainya melalui kopling perangkat keras pada perangkat
master yang mahal. Penelitian ini memindahkan mekanisme itu ke perangkat lunak pada lengan meja
berbiaya rendah dengan sisi penerima yang tetap terbuka — tanpa sensor umpan balik baru — dan
memicunya dari pengendali PS2 yang sudah dimiliki tim. Kontribusinya adalah mode posisi-halus beserta
perilaku tahan setelah pelepasan sebagai pengganti kopling perangkat keras; pengaruhnya divalidasi
melalui rencana protokol 2x2 dan dilaporkan sebagai harapan pra-registrasi, bukan sebagai hasil
pengukuran.

## Catatan draf (scaffolding — hapus saat perakitan, ticket 20)-archonx

- **Frozen-boundary compliance.** Latar dosis/radiasi, DNA, penanganan jarak jauh, akurasi, dan rumusan
  masalah dipertahankan sesuai Extended Abstract (admin ruling 14 Okt). Dua perbaikan disetujui pengguna
  pada 16 Okt: (a) atribusi pemancar spesifik dibuang — sumbernya (S2) hanya menyatakan "radiasi
  pengion" secara umum; (b) rantai kegagalan mekanis tak bersumber (ledger C8 = NOT FOUND) dibuang dan
  risikonya dinyatakan secara umum. Tidak ada klaim tak bersumber yang tersisa.
- **Peta klaim → ledger:** [1] = C1 + C2 (S2, IAEA *Radiation, People and the Environment*) ·
  [2] = C3 (S1, IAEA-TECDOC-1433). Keduanya sudah ada di ledger sebelum ticket ini; tidak ada entri baru.
- Perbandingan lama disebut sebagai "dua antarmuka masukan" tanpa menamai perangkatnya: nama perangkat
  yang lama masuk daftar konten terlarang `spec.md` → Testing Decisions butir 7, jadi tidak dieja di sini
  agar cek itu tetap bersih pada naskah maupun pada catatan draf.
