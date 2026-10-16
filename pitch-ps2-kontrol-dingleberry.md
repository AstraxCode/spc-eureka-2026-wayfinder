# Pitch: Kontrol Stik PS2 untuk Lengan Robot Teleoperasi-dingleberry

SPC Eureka 2026 — draft pitch (tim), 15 Okt 2026. Status: usulan baru, belum final.

## Inti idenya

Ganti antarmuka kontrol dari aplikasi/web joystick di HP menjadi **stik PS2** (joystick analog
+ tombol ABXY + trigger), target harga **di bawah Rp50.000**. Satu perangkat genggam murah yang
sudah dikenal semua orang menggantikan UI di layar.

## Skema kontrol (tiga lapis)

1. **Koordinasi multi-DOF (mode kasar):** dorong joystick ke depan → *end-effector* bergerak
   maju; rotasi beberapa sendi dihitung bersamaan (kinematika koordinasi di firmware). Operator
   memikirkan arah tangan, bukan sendi per sendi. Ini pola *rate control* yang dipakai robot
   teleoperasi sungguhan.
2. **Sendi tunggal (presisi terarah):** tekan satu tombol ABXY untuk memilih sendi (mis. △ =
   sendi lengan), lalu gerakkan joystick → hanya sendi itu yang bergerak. Enam tombol cukup
   untuk memetakan 5 DOF + gripper.
3. **Fine mode (trigger):** tahan/tekan trigger → sensitivitas turun (gain kecil), gerakan
   joystick kecil menghasilkan gerakan sendi sangat halus untuk penempatan akhir. Lepas joystick
   (posisi netral) → lengan menahan posisi (release-to-hold jadi alami: joystick diam = nol
   perintah = lengan diam).

## Kenapa ini kuat untuk paper

- **Hemat biaya:** stik PS2 kelas klon jauh lebih murah daripada membangun glove 5x MPU6050
  atau menambah sensor apa pun. Receiver tetap terbuka (open-loop) — tanpa encoder, tanpa
  sensor baru. Angka Feasibility (15% nilai) naik.
- **Prior art mendukung:** hibrida *position/rate control* + *motion scaling* adalah pendekatan
  yang terbukti di literatur (Richter 2019; Han & Yang 2022; Lee 2024). Skema 3-lapis di atas
  = versi murah dari pola yang sama, dan itulah kontribusi paper: **membuktikan pola kontrol
  teleoperasi kelas berat bisa dijalankan di perangkat keras di bawah Rp50.000.**
- **Ergonomi:** operator teleoperasi bekerja lama; stik game dirancang untuk sesi panjang,
  semua kontrol ada di satu pegangan (joystick + tombol + trigger) tanpa lihat layar.
- **Latensi bisa diukur:** stik → ESP32 (UART/SPI bit-bang, pustaka PS2X untuk ESP32 tersedia) →
  Wi-Fi → penerima → servo. Satu jalur sederhana, t_latency tetap terukur langsung.

## Fakta yang sudah diverifikasi (15 Okt 2026)

- **Interfacing:** pustaka `PS2X_lib` untuk ESP32 tersedia publik (Arduino-PS2X-ESP32, GitHub);
  banyak tutorial wiring PS2→Arduino/ESP32. Stik PS2 wireless memakai receiver 2,4 GHz yang
  berbicara protokol SPI-like — didukung pustaka tersebut. (Sumber: github.com/MyArduinoLib/
  Arduino-PS2X-ESP32; electropeak.com tutorial PS2-Arduino.)
- **Harga: PERHATIAN — klaim <Rp50.000 BELUM terverifikasi live.** Sweep Tokopedia 15 Okt 2026
  untuk "stik ps2 wireless": termurah di halaman pertama **Rp85.000** (85k–150k). Stik PS2
  *wired* klon "TW" adalah kelas yang biasanya di bawah Rp50k, tapi harga pastinya belum
  diambil dari listing. Kabel juga bukan masalah untuk meja kerja tabletop 1–3 m.
  → Perkiraan tim (16 Okt): stik PS2 wired "sekitar Rp40.000-Rp70.000" — LABEL SEBAGAI PERKIRAAN TIM, bukan harga terverifikasi listing. Tindakan: simpan link listing nyata sebelum angka masuk paper.

## Yang berubah dari keputusan sebelumnya

- Aplikasi/web joystick di HP (ADR 0002) → **digeser** menjadi stik PS2. Web joystick tetap
  bisa jadi fallback terdokumentasi.
- Larangan "analog joystick" ronde 1 → dicabut pengguna secara eksplisit: stik PS2 justru
  analog dan itu inti skema multi-DOF.
- Glove/IMU: tetap ditolak total (tidak muncul di paper).
- Metrics (galat penempatan, tahan 2 detik, latensi satu arah) dan protokol 2×2: **tidak berubah**.
  Sel "kondisi A vs B" kini berarti baseline stik vs baseline stik + fine mode.

## Risiko yang harus dijawab sebelum final

1. **Harga <Rp50k** — belum terverifikasi (lihat di atas). Kalau wireless Rp85k dan wired
   ternyata >Rp50k juga, klaim angka harus diubah.
2. **Kinematika koordinasi multi-DOF** — ini pekerjaan firmware baru (inverse kinematics sederhana
   atau mapping tetap per-arah). Untuk paper tanpa uji fisik, cukup dispesifikasikan; untuk
   Final, harus dibangun dan diuji.
3. **Akurasi stick analog** — joystick klon murah bisa punya deadzone asimetris; risiko kecil,
   disebut jujur di batasan paper.
4. **Ergonomi tombol ABXY saat menekan + menggerakkan joystick bersamaan** — pola umum di game,
   tapi perlu diuji saat Final.

## Kalimat pitch untuk tim (Bahasa Indonesia)

"Kita ganti kontrol HP dengan stik PS2 di bawah Rp50 ribu: joystick untuk menggerakkan tangan
robot ke segala arah sekaligus, tombol ABXY untuk mengunci satu sendi, trigger untuk mode halus
saat penempatan akhir. Satu perangkat murah, pola kontrol yang sama dengan robot teleoperasi
sungguhan, dan semua metrik uji kita tetap berlaku."
