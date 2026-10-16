# Rencana Konsep — Lengan Robot Teleoperasi (versi teks)

Penjelasan konsep untuk semua orang, berdasarkan isi mindmap `mindmap-rencana-konsep.png`.

## 1. Masalahnya

- Pekerja pembangkit nuklir terpapar radiasi saat menangani bahan radioaktif.
- Solusinya: robot yang digerakkan dari jarak jauh.
- Yang dituntut: akurasi — tidak boleh salah ambil, tidak boleh menjatuhkan.

## 2. Robotnya

- Lengan robot meja dengan 5 sendi (5-DOF).
- Perangkat keras: servo MG996R, papan ESP32, driver PCA9685.
- Sistem terbuka (tanpa sensor posisi) — semua presisi datang dari cara kita mengontrolnya.

## 3. Cara Kendalinya — stik PS2 (± Rp40–70 ribu, perkiraan tim)

- **Joystick maju** → tangan robot maju; banyak sendi bergerak bersamaan, operator cukup
  memikirkan arah, bukan sendi per sendi.
- **Tombol ABXY** → kunci satu sendi saja, lalu joystick mengatur sendi itu (kontrol per sendi).
- **Trigger** → MODE HALUS: sensitivitas turun, gerakan kecil di joystick menghasilkan gerakan
  sangat presisi untuk penempatan akhir.
- **Lepas joystick** → robot diam dan menahan posisi terakhir.
- **Cadangan:** web joystick di HP lewat Wi-Fi (dokumentasi ADR 0002).

## 4. Pembuktiannya — uji 2×2

- Banding: mode kasar saja **vs** mode kasar + fine mode.
- Jarak: **1 meter vs 3 meter**.
- **40 percobaan per kondisi, 3 operator bergantian** (urutan diselingi agar efek belajar tidak
  mengotori hasil).
- Yang diukur: **galat penempatan**, **ketahanan 2 detik**, **latensi jaringan**.

## 5. Kejujuran paper

- Belum ada data fisik sebelum 18 Okt — prototype terkunci di balik tahap paper.
- Semua hasil ditulis sebagai **PERKIRAAN**, tidak pernah sebagai hasil pengukuran.
- Angka target didaftarkan lebih dulu (mis. latensi ≤ 200 ms; galat ≤ satu kotak petak), bukan
  dipalsukan.
- Uji fisik nyata dilakukan di tahap Final, November.

## 6. Jadwal

- **18 Okt** — batas pengumpulan tim.
- **23 Okt** — batas resmi kompetisi.
- **Terbuka:** judul paper masih menunggu keputusan tim (lihat GitHub Issue #1).

---
Sumber keputusan: `map.md` dan folder `issues/`. Diagram visual: `mindmap-rencana-konsep.png`.
