# Daftar Pustaka-archonx

[1] IAEA, *Radiation, People and the Environment*, IAEA/PI/A.75/04-00391, Vienna: International Atomic Energy Agency, Feb. 2004. [Daring]. Tersedia: https://www.iaea.org/sites/default/files/radiation0204.pdf

[2] IAEA, *Remote Technology Applications in Spent Fuel Management*, IAEA-TECDOC-1433, Vienna: International Atomic Energy Agency, 2005. [Daring]. Tersedia: https://www-pub.iaea.org/MTCD/Publications/PDF/TE_1433_web.pdf

[3] J. Han dan G.-H. Yang, "Improving teleoperator efficiency using position–rate hybrid controllers and task decomposition," *Applied Sciences*, vol. 12, no. 19, Art. no. 9672, hlm. 1–18, 2022. doi: 10.3390/app12199672. [Daring]. Tersedia: https://www.mdpi.com/2076-3417/12/19/9672

[4] F. Richter, R. K. Orosco, dan M. C. Yip, "Motion scaling solutions for improved performance in high delay surgical teleoperation," dalam *Proc. IEEE Int. Conf. Robot. Autom. (ICRA)*, Montreal, QC, Canada, 2019, hlm. 1590–1595. doi: 10.1109/ICRA.2019.8794109. [Daring]. Tersedia: https://arxiv.org/abs/1902.03290

[5] H. Lee, J. Han, dan G.-H. Yang, "Development of variable scaling teleoperation framework for improving teleoperation performance," *International Journal of Control, Automation and Systems*, vol. 22, no. 3, hlm. 936–945, 2024. doi: 10.1007/s12555-022-1099-z. [Daring]. Tersedia: https://link.springer.com/article/10.1007/s12555-022-1099-z

[6] J. Yoon, S. Park, H. Park, C. Kim, S. Park, dan M. Hwang, "A single scale doesn't fit all: Adaptive motion scaling for efficient and precise teleoperation," arXiv:2503.01216v1, 2025. [Daring]. Tersedia: https://arxiv.org/abs/2503.01216v1

[7] Z. Wang, Y. Zhang, dan X. Zhang, "A comparative study on human motion smoothing filters for RGB-D camera teleoperation," dalam *Proc. 2024 30th Int. Conf. Mechatronics Mach. Vision Pract. (M2VIP)*, 2024, hlm. 1–6. [Daring]. Tersedia: https://ieeexplore.ieee.org/abstract/document/10746144

[8] R. Akl, D. Tummala, dan X. Li, "Indoor propagation modeling at 2.4 GHz for IEEE 802.11 networks," Department of Computer Science and Engineering, University of North Texas, Denton, TX, Tech. Rep., 2006. [Daring]. Tersedia: https://digital.library.unt.edu/ark:/67531/metadc30827/m2/1/high_res_d/Akl-2006-Indoor_Propagation_Modeling_at_2.4.pdf

[9] P. Pandey dan R. Parasuraman, "Empirical analysis of bi-directional Wi-Fi network performance on mobile robots in indoor environments," arXiv:2110.03011, 2021. [Daring]. Tersedia: https://arxiv.org/abs/2110.03011

[10] B. Porter, "Arduino-PS2X: Playstation 2 controller library for Arduino," repositori kode sumber madsci1016/Arduino-PS2X (diportasi untuk ESP32 oleh MyArduinoLib/Arduino-PS2X-ESP32, 2020). [Daring]. Tersedia: https://github.com/madsci1016/Arduino-PS2X

## Catatan draf (scaffolding — hapus saat perakitan, ticket 20)-archonx

- **Urutan kemunculan sitasi dalam naskah:**
  - `[1]` = Bab I (Pendahuluan), baris kemunculan pertama. Mendukung C1 (dosis batas pekerja BSS 20 mSv/thn, rata-rata UNSCEAR 0,6 mSv/thn) dan C2 (mekanisme kerusakan DNA dan risiko karsinogenesis). Sumber: S2 (IAEA, *Radiation, People and the Environment*).
  - `[2]` = Bab I (Pendahuluan), baris kemunculan kedua. Mendukung C3 (sistem teleoperasi/penanganan jarak jauh untuk reduksi dosis radiasi pekerja fasilitas nuklir). Sumber: S1 (IAEA-TECDOC-1433).
  - `[3]` = Bab II (Dasar Teori), baris kemunculan ketiga. Mendukung C14 (kompromi resolusi-kecepatan dan strategi *bubble* kendali hibrida posisi–laju Han & Yang 2022). Sumber: S10 (Applied Sciences 12(19), 9672).
  - `[4]` = Bab II (Dasar Teori), baris kemunculan keempat. Mendukung C15 (penskalaan gerak teleoperasi bedah berlatensi tinggi Richter et al. 2019). Sumber: S9 (ICRA 2019 / arXiv:1902.03290).
  - `[5]` = Bab II (Dasar Teori), baris kemunculan kelima. Mendukung C16 (kerangka kerja penskalaan variabel Lee et al. 2024, disitasi kualitatif pada tingkat abstrak). Sumber: S11 (IJCAS 22, 936–945).
  - `[6]` = Bab II (Dasar Teori), baris kemunculan keenam. Mendukung C17 (penskalaan adaptif kasar/halus Yoon et al. 2025). Sumber: S12 (arXiv:2503.01216v1).
  - `[7]` = Bab II (Dasar Teori), baris kemunculan ketujuh. Mendukung C18 (perbandingan delapan filter deret waktu Wang et al. 2024; dasar batas kejujuran bahwa pemulusan semata tidak membuktikan perbaikan akurasi penempatan). Sumber: S13 (IEEE M2VIP 2024).
  - `[8]` = Bab II (Dasar Teori), baris kemunculan kedelapan. Mendukung C5 (model rugi propagasi dalam ruang 2,4 GHz Akl et al. 2006). Sumber: S3 (Univ. of North Texas Tech. Rep.).
  - `[9]` = Bab II (Dasar Teori), baris kemunculan kesembilan. Mendukung C6 (karakterisasi empiris latensi dan *jitter* Wi-Fi 2,4 GHz teleoperasi robot Pandey & Parasuraman 2021). Sumber: S4 (arXiv:2110.03011).
  - `[10]` = Bab II (Dasar Teori), baris kemunculan kesepuluh. Mendukung C11 (arsitektur protokol stik PS2 berbasis *four-wire synchronous polling* yang mewajibkan mikrokontroler pengirim). Sumber: S8 (Bill Porter / madsci1016 upstream & MyArduinoLib ESP32 fork).

- **Audit klaim ledger:**
  - Klaim aktif naskah Full Paper: C1, C2, C3, C5, C6, C11, C14, C15, C16, C17, C18 (11 klaim eksternal terbukti, seluruhnya tersitasi pada `[1]`–`[10]`).
  - Klaim C4: Telah dibantah (*CONTRADICTED*) oleh S1 dan S7, dijadikan reframing batasan masalah (bukan klaim temuan).
  - Klaim C7: Terkait perbandingan sarung tangan vs stik (S5, S6) pada era Extended Abstract; telah disupersede oleh ADR 0002 / Ticket 04 / Ticket 06 / Ticket 09 / Ticket 11 (intervensi mode halus pada stik).
  - Klaim C8: Tidak ditemukan rujukan (*NOT FOUND*), telah dihapus sesuai keputusan pengguna 16 Okt (Ticket 12).
  - Klaim C9: Hipotesis awal sarung tangan (ditinggalkan).
  - Klaim C10: Data eksperimen mandiri tim (bukan sitasi eksternal).
  - Klaim C12, C13: Estimasi harga internal dan inventaris internal tim (bukan sitasi eksternal).
  - Sumber S5, S6, S7:
    - S7: Berstatus *UNVERIFIED* di ledger, tidak disitasi sesuai aturan integritas akademik.
    - S5 & S6: Sumber awal studi komparasi antarmuka (Zhou et al., Jia et al.). Karena naskah Full Paper beralih sepenuhnya ke intervensi kendali mode posisi-halus pada stik PS2 dan tidak lagi menyajikan perbandingan empiris sarung tangan vs stik, S5 dan S6 tidak disitasi dalam badan naskah. Rekomendasi untuk Load A / perakitan: Tandai S5 dan S6 sebagai *SUPERSEDED (antarmuka sarung tangan ditinggalkan)* dalam ledger saat perakitan akhir.
