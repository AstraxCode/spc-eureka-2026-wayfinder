# Kesimpulan dan Saran-archonx

Bab ini menyajikan sintesis akhir dari perancangan sistem teleoperasi lengan robot 5-DOF serta arah
pengembangan selanjutnya. Pembahasan dibagi menjadi dua bagian utama: (i) kesimpulan yang merangkum
kontribusi perancangan, keterbatasan operasional, dan status integritas data pra-registrasi, serta (ii) saran
yang memuat rekomendasi pelaksanaan pengujian empiris dan pencatatan terarah mengenai otonomi berbasis kamera.

## Kesimpulan-archonx

Berdasarkan hasil perancangan teknis, analisis teoritis, dan perumusan protokol validasi yang telah dipaparkan,
dapat ditarik beberapa kesimpulan mendasar:

1. *Kontribusi intervensi kendali mode posisi-halus:* Penelitian ini berhasil merumuskan solusi kendali teleoperasi
   lengan robot 5-DOF berbiaya terjangkau untuk skenario penanganan presisi jarak jauh. Kontribusi utama perancangan
   terletak pada intervensi *mode posisi-halus* (*fine-positioning mode*) berbasis pengendali stik PS2 dan arsitektur
   mikrokontroler ganda ESP32 (transmisi nirkabel Wi-Fi 2,4 GHz UDP). Melalui integrasi faktor reduksi gain α
   (0 < α < 1) yang diaktifkan melalui tombol pemicu (*trigger*), rentang gerak fisik tuas stik diperluas, sehingga
   secara efektif memitigasi fenomena osilasi koreksi berlebih (*hunting*) akibat keterbatasan kontrol neuromuskular
   operator pada fase akhir pergerakan (*docking*).
2. *Eliminasi kopling perangkat keras melalui release-to-hold:* Penerapan kendali laju (*rate control*) pada tuas
   stik menghasilkan karakteristik *release-to-hold* secara inheren di mana pemulangan tuas ke posisi netral
   secara otomatis menghasilkan kecepatan sudut nol dan mempertahankan sudut sendi terakhir pada register PWM
   PCA9685. Fitur perangkat lunak ini berfungsi sebagai pengunci posisi alami yang menggantikan kebutuhan mekanisme
   kopling fisik (*hardware clutch*) atau rem tambahan, menjaga kesederhanaan mekanik dan efisiensi biaya purwarupa.
3. *Batasan operasional dan pembuktian konsep skala meja:* Sistem teleoperasi yang dirancang merupakan pembuktian
   konsep skala meja (*tabletop proof of concept*) yang memanfaatkan objek uji balok busa sintetis 30 mm × 30 mm × 30 mm
   di lingkungan laboratorium terkendali. Sistem ini beroperasi secara *strictly open-loop* tanpa umpan balik enkoder
   maupun sensor gaya, serta secara tegas **tidak ditujukan** untuk penanganan batang bahan bakar nuklir riil pada
   fasilitas reaktor nuklir yang menuntut ketahanan radiasi pengion gamma ekstrem dan kapasitas beban hidrolik masif
   sesuai standar teknis IAEA (IAEA-TECDOC-1433 dan IAEA Radiation).
4. *Penegasan status hasil pra-registrasi dan kepatuhan integritas ilmiah:* Seluruh parameter evaluasi yang diajukan
   dalam karya ini—mencakup target latensi satu arah ≤ 200 ms, galat penempatan Euclidean dalam batas satu sel kisi target,
   dan penahanan posisi stabil selama 2 detik (kriteria keberhasilan proyek ≥ 8 dari 10 pengulangan)—merupakan target
   kinerja pra-registrasi dan ekspektasi perancangan, bukan hasil fabrikasi data pengukuran empiris. Pendekatan ini
   diambil demi mematuhi ketentuan integritas akademik Buku Panduan SPC Eureka! ITB 2026 (hal. 5 butir 7) mengingat
   perakitan fisik prototipe baru dijadwalkan pada 18 Oktober 2026 untuk persiapan tahap Final.

## Saran dan Pengembangan Selanjutnya-archonx

Berdasarkan perancangan sistem dan batasan yang telah diidentifikasi, diajukan dua saran utama untuk pengembangan
pada tahap selanjutnya:

1. *Pelaksanaan pengujian empiris protokol validasi 2×2:* Disarankan untuk melaksanakan pengujian fisik kuantitatif
   secara penuh pasca-perakitan prototipe tanggal 18 Oktober 2026 menggunakan protokol 2×2 yang telah dibakukan pada
   bab Metodologi (Kondisi A vs Kondisi B, jarak 1 m vs 3 m, 40 pengulangan per kondisi oleh 3 operator berpasangan).
   Pengujian ini diperlukan guna memverifikasi secara empiris distribusi latensi transmisi riil, membuktikan signifikansi
   penurunan galat penempatan Euclidean melalui analisis foto kisi ortogonal, serta mengonfirmasi reduksi variansi performa
   antar-operator di bawah intervensi mode posisi-halus.
2. *Eksplorasi otonomi pencekeraman berbasis visi komputer (ADR 0001):* Pengembangan jangka panjang sistem teleoperasi
   ini diarahkan pada integrasi otonomi pencekeraman berbasis visi komputer (*camera-based autonomous grasping*).
   Sebagaimana ditetapkan dalam keputusan arsitektur proyek (ADR 0001), integrasi modul kamera dan komputasi cerdas
   deteksi objek tidak dimasukkan ke dalam ruang lingkup dokumen *full paper* saat ini demi menjaga kelayakan realisasi
   perangkat keras (*hardware feasibility*), mengendalikan batasan anggaran, serta menghindari klaim tanpa dukungan
   pengujian fisik awal. Kendati demikian, otonomi berbasis kamera dicatat secara resmi sebagai arah masa depan untuk
   mereduksi beban kognitif operator manusia secara substansial pada tugas pemindahan berulang. Pelaksanaan arah riset ini
   dapat dibuka kembali apabila tiga prasyarat telah terpenuhi: tersedianya kajian literatur terarah mengenai manipulasi
   terbimbing visi pada aktuator berbiaya terjangkau, keberhasilan demonstrasi purwarupa visi dan algoritma perencanaan
   gerak otonom sebelum tahap kompetisi lanjutan, serta ketersediaan anggaran untuk modul pemrosesan citra berdaya komputasi
   memadai.

## Catatan draf (scaffolding — hapus saat perakitan, ticket 20)-archonx

- Konsistensi klaim dan batasan: Bagian Kesimpulan merangkum secara utuh kontribusi mode posisi-halus, eliminasi kopling
  mekanik via *release-to-hold*, batasan *tabletop proof of concept*, keterbatasan sistem *open-loop*, dan penegasan
  komitmen integritas ilmiah terhadap target pra-registrasi (konsisten 100% terhadap Bab Metodologi dan Bab Hasil dan Pembahasan).
- Future-work paragraph: Bagian Saran memuat tepat satu paragraf terarah mengenai otonomi berbasis visi komputer sesuai
  ketetapan ADR 0001, mencatat rasionalisasi penolakan saat ini dan prasyarat pembukaan kembali tanpa mengubah sistem menjadi
  rencana kedua (*second plan*).
- Peta klaim dan angka: Nol klaim baru dan nol angka tanpa sumber. Seluruh metrik numerik yang disebut (≤ 200 ms, balok 30 mm,
  2 detik, 8/10 percobaan, 18 Oktober 2026, tanggal Final) berasal dari dokumen fondasi proyek (`spec.md`, `map.md`,
  `claim-ledger-archonx.md`, dan Buku Panduan Eureka! ITB 2026).
- Verifikasi kepatuhan konten: Mematuhi secara ketat larangan kemunculan istilah antarmuka usang atau antarmuka alternatif
  sebagaimana diatur pada `spec.md` → Testing Decisions butir 7.
- Seluruh tajuk diakhiri dengan penanda watermark internal `-archonx`.