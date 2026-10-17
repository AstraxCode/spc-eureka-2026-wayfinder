# Lampiran-archonx

Dokumen ini memuat lampiran pendukung naskah *Full Paper* sesuai dengan sistematika buku panduan Science Project Competition (SPC) Eureka! ITB 2026. Lampiran mencakup pembagian tugas dan kontribusi anggota tim, rincian anggaran biaya, tabel spesifikasi komponen sistem, skema rangkaian kelistrikan teleoperasi, serta rancangan algoritma kendali.

---

## Lampiran 1. Pembagian Tugas dan Kontribusi Anggota Tim-archonx

Berikut adalah rincian pembagian tugas dan kontribusi masing-masing anggota tim selama proses penelitian, perancangan sistem, pengembangan prototipe, serta penyusunan laporan naskah ilmiah:

| No. | Nama Anggota Tim | Peran | Rincian Tugas dan Kontribusi |
|---|---|---|---|
| 1 | **Anargya Arkan Dhafy Hamdani** | Ketua Tim | • Mengoordinasikan seluruh tahapan pengembangan proyek dan perumusan arah penelitian.<br>• Merancang konsep kendali teleoperasi, spesifikasi mode posisi-halus (*fine-positioning mode*), dan logika *release-to-hold*.<br>• Mengembangkan dan menguji firmware integrasi pada mikrokontroler pengirim (pembacaan stik PS2 via pustaka PS2X) dan penerima (pengondisian sinyal perintah).<br>• Menyusun dan menyelaraskan naskah *Full Paper* (Abstrak, Pendahuluan, Metodologi, dan Pembahasan). |
| 2 | **Muhamad Naufal Firdaus** | Anggota 1 | • Merancang dan memodifikasi struktur mekanik cetak 3D lengan robot 5-DOF (adaptasi desain rujukan Wonder Tiger).<br>• Mengoptimalkan tata letak penempatan aktuator servo, jalur perkabelan internal, dan penyangga modul elektronik pada rangka lengan.<br>• Melakukan perhitungan beban momen inersia dan verifikasi kecukupan torsi motor servo TowerPro MG996R pada konfigurasi terburuk (*worst-case cantilever*).<br>• Menyusun dokumentasi spesifikasi teknis komponen mekanik dan perakitan struktur prototipe. |
| 3 | **Fakhri Ahmad Kendri** | Anggota 2 | • Merancang arsitektur sistem kelistrikan, pengkabelan driver PWM PCA9685, dan pemisahan jalur catu daya (*power isolation*).<br>• Merancang tata letak peredaman lonjakan arus transien (pemasangan kapasitor *bulk* elektrolit dan filter tapis frekuensi tinggi).<br>• Merancang protokol eksperimen 2×2 (prosedur pengukuran galat penempatan pada kisi target terkalibrasi dan pencatatan latensi jaringan satu arah).<br>• Mengompilasi kebutuhan anggaran proyek, analisis kelayakan biaya implementasi, dan penyusunan lampiran teknis. |

---

## Lampiran 2. Rincian Anggaran Biaya Pengembangan Proyek-archonx

Rincian kebutuhan anggaran disusun secara realistis sesuai kebutuhan perancangan prototipe sistem lengan robot teleoperasi 5-DOF berbasis pengendali stik PS2. Seluruh komponen dipilih untuk memaksimalkan kelayakan implementasi (*feasibility*) dan efisiensi biaya.

*Tabel 2. Rincian anggaran biaya perancangan prototipe*

| No. | Komponen / Material | Kategori | Jumlah | Harga Satuan (Rp) | Total (Rp) |
|:---:|---|---|:---:|:---:|:---:|
| **1** | **Antarmuka Masukan (Operator)** | | | | |
| 1.1 | Pengendali Stik PS2 (Model klon berkabel, 4-wire interface) | Perangkat Kendali | 1 unit | 55.000<br>*(Perkiraan tim: Rp40.000–Rp70.000)* | 55.000 |
| **2** | **Mikrokontroler & Pemrosesan Sinyal** | | | | |
| 2.1 | Modul ESP32 DevKit V1 (Unit Pengirim / Master Operator) | Mikrokontroler | 1 buah | 65.000 | 65.000 |
| 2.2 | Modul ESP32 DevKit V1 (Unit Penerima / Slave Robot) | Mikrokontroler | 1 buah | 65.000 | 65.000 |
| 2.3 | Modul Driver Servo PCA9685 (16-Kanal PWM 12-bit, I2C) | Antarmuka Aktuator | 1 buah | 35.000 | 35.000 |
| **3** | **Material Prototipe & Aktuator** | | | | |
| 3.1 | Motor Servo TowerPro MG996R (Metal Gear, torsi ~9,4–11 kg·cm) | Aktuator Sendi & Gripper | 5 buah | 45.000 | 225.000 |
| 3.2 | Bahan Cetak 3D PLA (Filamen rangka struktur 5-DOF adaptasi Wonder Tiger) | Struktur Mekanik | 1 rol (1 kg) | 130.000 | 130.000 |
| 3.3 | Baut, mur M3, bearing, dan pengencang mekanik | Komponen Mekanik | 1 paket | 25.000 | 25.000 |
| **4** | **Bahan Kelistrikan & Catu Daya** | | | | |
| 4.1 | Unit Adaptor Catu Daya 6V 5A (Jalur daya khusus servo aktuator) | Catu Daya Aktuator | 1 unit | 60.000 | 60.000 |
| 4.2 | Regulator Tegangan Step-Down / Adaptor 5V 2A (Logika mikrokontroler) | Catu Daya Logika | 1 unit | 25.000 | 25.000 |
| 4.3 | Komponen Pasif (Kapasitor bulk 1000 µF, dekap 0,1 µF, kabel jumper, konektor) | Komponen Pasif | 1 paket | 20.000 | 20.000 |
| **5** | **Pengujian & Kalibrasi Instrumen** | | | | |
| 5.1 | Papan Uji Kisi Terkalibrasi (Grid akurasi mm) & Objek Target Uji | Media Eksperimen | 1 set | 20.000 | 20.000 |
| | **Total Estimasi Anggaran Proyek** | | | | **Rp725.000** |

> **Catatan Keterbukaan Anggaran (Integrity Note):** Harga pengendali stik PS2 berkabel dicantumkan sebesar Rp55.000 berdasarkan label **perkiraan tim (rentang estimasi Rp40.000–Rp70.000)** dan bukan kutipan tunggal listing pasar definitif. Tim telah memiliki 2 unit modul ESP32 dalam inventaris awal, sehingga biaya aktual yang dikeluarkan tim di lapangan berada di bawah total estimasi rancangan baru.

---

## Lampiran 3. Spesifikasi Teknis Komponen Sistem (`tabel-komponen-archonx`)-archonx

Tabel berikut memuat spesifikasi teknis lengkap dari seluruh komponen pembangun sistem teleoperasi lengan robot 5-DOF dengan arsitektur kendali stik PS2 dan komunikasi Wi-Fi nirkabel:

*Tabel 3. Spesifikasi komponen sistem teleoperasi 5-DOF-archonx*

| Komponen | Spesifikasi | Fungsi |
|---|---|---|
| **Lengan robot cetak 3D** | Adaptasi desain rujukan Wonder Tiger (lisensi CC BY-NC 4.0), 5 derajat kebebasan (*degrees of freedom* / DOF), material PLA dengan penguatan pada titik tumpu sendi bahu dan siku. | Membentuk struktur mekanis manipulator (rotasi dasar, elevasi bahu, elevasi siku, fleksi pergelangan, dan pencengkeram *gripper*). |
| **Motor servo aktuator** | TowerPro MG996R, *metal gear*, torsi penahan ±9,4 kg·cm pada tegangan 4,8 V (hingga 11 kg·cm pada 6,0 V), sudut rotasi operasional 0°–180°, jumlah 5 buah. | Menggerakkan masing-masing sumbu sendi manipulator dan mekanisme rahang pembuka/penutup objek uji. |
| **Driver motor servo** | PCA9685, 16-kanal PWM independen, resolusi 12-bit (4096 tingkat resolusi pulsa per siklus), frekuensi kerja PWM 50 Hz, komunikasi bus I2C (alamat `0x40`). | Menerjemahkan sinyal perintah posisi sudut dari ESP32 penerima menjadi modulasi lebar pulsa presisi untuk tiap motor servo secara serempak. |
| **Pengendali operator** | Pengendali stik PS2 (*handheld controller* klon berkabel), tuas analog ganda (*dual analog thumbsticks*), tombol digital aksi (△, ○, ✕, □), tombol navigasi (*D-pad*), dan tombol bahu/pemicu (*trigger buttons* L1/L2/R1/R2). | Menyediakan antarmuka fisik terpadu bagi operator: kemudi multi-DOF terkoordinasi (tuas analog), seleksi artikulasi sendi tunggal (tombol aksi), dan aktivasi mode posisi-halus (tombol pemicu). |
| **Mikrokontroler pengirim** | ESP32 DevKit V1, prosesor ganda Xtensa 32-bit LX6 @ 240 MHz, modul nirkabel Wi-Fi 802.11 b/g/n (2,4 GHz), antarmuka komunikasi perangkat keras SPI/GPIO. | Melakukan *polling* berkala terhadap status tuas dan tombol stik PS2 via pustaka PS2X, membungkus data kendali ke dalam struktur paket, menyematkan penanda waktu kirim (*t_send*), dan mentransmisikan paket via Wi-Fi. |
| **Mikrokontroler penerima** | ESP32 DevKit V1, konektivitas Wi-Fi 2,4 GHz mode stasiun / titik akses lokal (*AP/STA*), bus perangkat keras I2C master (GPIO 21 SDA, GPIO 22 SCL). | Menerima paket perintah teleoperasi, menghitung latensi transmisi (*t_receive - t_send*), mengeksekusi algoritma pemetaan mode posisi-halus dan penguncian posisi (*release-to-hold*), serta memperbarui register PCA9685. |
| **Catu daya terpisah** | Unit catu daya teregulasi 6 V DC kontinu (arus kerja minimal 5 A) untuk rail aktuator servo; regulator tegangan 5 V / 3,3 V DC untuk sirkuit logika mikrokontroler dan driver PCA9685. | Memisahkan jalur daya aktuator dari jalur logika guna mencegah gangguan fluktuasi tegangan, *noise* induktif motor, dan restart mikrokontroler (*brownout reset*). |
| **Kapasitor peredam lonjakan** | Kapasitor elektrolit *bulk* 1000 µF / 16 V terpasang paralel pada terminal catu daya servo PCA9685, dipadukan kapasitor keramik *bypass* 0,1 µF pada rail VCC logika. | Meredam lonjakan arus sesaat (*transient current spike*) ketika motor servo mulai bergerak atau mengalami kondisi torsi beban puncak. |
| **Objek uji & kisi ukur** | Balok busa densitas seragam berukuran 30 mm × 30 mm × 30 mm (bobot ±15 gram); papan uji dengan kisi koordinat bertingkat milimeter (ketelitian pembacaan 0,5 mm). | Menyediakan target tugas pemindahan dan penempatan teleoperasi terstandardisasi untuk mengevaluasi galat jarak penempatan secara empiris. |

---

## Lampiran 4. Skema Rangkaian Kelistrikan Teleoperasi (`skema-rangkaian-teleoperasi-archonx`)-archonx

Arsitektur teleoperasi menggunakan rantai kendali terisolasi: **Stik PS2 → ESP32 Pengirim → Wi-Fi 2,4 GHz → ESP32 Penerima → PCA9685 → 5× Servo MG996R**.

### 1. Diagram Blok Aliran Sistem Rangkaian-archonx

```
┌──────────────────────────────────────────────────────────────────────────┐
│                   UNIT OPERATOR (SISI PENGIRIM)                          │
│                                                                          │
│  ┌───────────────────────┐             ┌──────────────────────────────┐  │
│  │   KONTROLER STIK PS2  │             │   ESP32 PENGIRIM (MASTER)    │  │
│  │                       │  4-wire SPI │                              │  │
│  │ • Tuas Analog Kiri    │────────────▶│ • Pembacaan status via PS2X  │  │
│  │ • Tuas Analog Kanan   │  DATA, CMD, │ • Pembentukan paket kendali  │  │
│  │ • Tombol Aksi (ABXY)  │  CLK, ATT   │ • Penanda waktu (t_send)     │  │
│  │ • Tombol Pemicu (L/R) │             │ • Modul Wi-Fi 2,4 GHz TX     │  │
│  └───────────────────────┘             └──────────────┬───────────────┘  │
└───────────────────────────────────────────────────────┼──────────────────┘
                                                        │
                                                        │ Gelombang Radio Wi-Fi
                                                        │ Paket UDP / ESP-NOW
                                                        │ (Jarak Uji: 1 m & 3 m)
                                                        ▼
┌──────────────────────────────────────────────────────────────────────────┐
│                    UNIT MANIPULATOR (SISI PENERIMA)                      │
│                                                                          │
│  ┌────────────────────────────────────────────────────────────────────┐  │
│  │   ESP32 PENERIMA (SLAVE)                                           │  │
│  │   • Menerima paket & hitung latensi: t_latency = t_receive - t_send│  │
│  │   • Filter deadzone tuas & penskalaan gain mode posisi-halus (G)   │  │
│  │   • Logika pengunci posisi saat netral (release-to-hold latch)     │  │
│  │   • Pustaka Wire Master I2C                                        │  │
│  └─────────────────────────────────┬──────────────────────────────────┘  │
│                                    │ Jalur I2C (SDA: GPIO 21, SCL: GPIO 22)
│                                    ▼                                     │
│  ┌────────────────────────────────────────────────────────────────────┐  │
│  │   DRIVER PWM PCA9685 (16-Kanal, 12-bit, frekuensi 50 Hz)           │  │
│  │   • VCC Logika : 3,3 V / 5 V (dari regulator logika ESP32)         │  │
│  │   • V+ Servo   : Rail 6 V terpisah (dari Adaptor 6 V 5 A)          │  │
│  │   • Kapasitor  : Elektrolit 1000 µF paralel pada rail V+ ke GND    │  │
│  └────────┬───────────┬───────────┬───────────┬───────────┬───────────┘  │
│           │CH0        │CH1        │CH2        │CH3        │CH4           │
│           ▼           ▼           ▼           ▼           ▼              │
│       ┌───────┐   ┌───────┐   ┌───────┐   ┌───────┐   ┌───────┐          │
│       │ Servo │   │ Servo │   │ Servo │   │ Servo │   │ Servo │          │
│       │ Base  │   │ Bahu  │   │ Siku  │   │ Pergel│   │Gripper│          │
│       │ MG996R│   │ MG996R│   │ MG996R│   │ MG996R│   │ MG996R│          │
│       └───────┘   └───────┘   └───────┘   └───────┘   └───────┘          │
│                                                                          │
│  ══════════════════ JALUR CATU DAYA & MASSA BERSAMA ══════════════════   │
│  Adaptor 6 V 5 A ───▶ Rail V+ Servo PCA9685 ───▶ Motor Servo (MG996R)    │
│  Adaptor 5 V 2 A ───▶ VCC Logika ESP32 & VCC PCA9685                     │
│  COMMON GROUND   ───▶ Penyatuan seluruh titik GND logika & daya aktuator │
└──────────────────────────────────────────────────────────────────────────┘
```

### 2. Rincian Hubungan Perkabelan Antar-Pin-archonx

#### A. Koneksi Stik PS2 ke ESP32 Pengirim (*Unit Operator*)-archonx
Pustaka `PS2X_lib` membaca protokol serial stik melalui empat jalur sinyal digital yang dihubungkan ke GPIO ESP32:

| Pin Stik PS2 | Label Fungsi | Pin GPIO ESP32 Pengirim | Keterangan Sambungan |
|---|---|---|---|
| Pin 1 | DATA (MISO) | GPIO 19 | Saluran luaran data dari kontroler ke ESP32 (dilengkapi *internal pull-up* atau resistor eksternal 4,7 kΩ ke 3,3 V). |
| Pin 2 | COMMAND (MOSI) | GPIO 23 | Saluran perintah konfigurasi dari ESP32 ke kontroler. |
| Pin 4 | GROUND | GND | Terhubung ke saluran ground bersama (*common ground*). |
| Pin 5 | POWER (VCC) | 3,3 V / 5 V | Catu daya kontroler (3,3 V untuk receiver nirkabel / 5 V untuk stik berkabel). |
| Pin 6 | ATTENTION (CS) | GPIO 5 | Saluran pemilihan perangkat (*chip select / attention*), bernilai aktif rendah (*active low*). |
| Pin 7 | CLOCK (SCK) | GPIO 18 | Saluran sinyal detak sinkronisasi komunikasi serial. |

#### B. Koneksi ESP32 Penerima ke Driver PCA9685 (*Unit Manipulator*)-archonx
Komunikasi antara mikrokontroler penerima dan modul driver PWM dilakukan melalui antarmuka bus I2C:

| Pin Driver PCA9685 | Pin GPIO ESP32 Penerima | Keterangan Sistem Kelistrikan |
|---|---|---|
| VCC (Logika) | 3,3 V (ESP32) | Daya logika pengendali sirkuit terintegrasi PCA9685. |
| GND | GND (ESP32) | Terhubung ke saluran *common ground* sistem. |
| SDA | GPIO 21 | Jalur data serial bus I2C (alamat modul default: `0x40`). |
| SCL | GPIO 22 | Jalur detak serial bus I2C (kecepatan standar 100 kHz / *fast mode* 400 kHz). |
| V+ (Rail Daya Servo) | Terminal + Catu Daya 6 V | Jalur daya arus tinggi terpisah khusus motor servo aktuator. |
| Terminal Kapasitor | Elco 1000 µF / 16 V | Terpasang langsung melintang pada terminal V+ dan GND driver servo. |

#### C. Pemetaan Kanal PWM PCA9685 ke Motor Servo Lengan Robot-archonx

| Kanal PCA9685 | Artikulasi Sendi Manipulator | Model Aktuator | Batasan Sudut Aman (*Firmware Clamp*) |
|---|---|---|---|
| Kanal 0 (CH0) | Rotasi Basis (*Base Yaw*) | TowerPro MG996R | 0° – 180° (Netral: 90°) |
| Kanal 1 (CH1) | Elevasi Bahu (*Shoulder Pitch*) | TowerPro MG996R | 15° – 165° (Batas mekanis anti-benturan) |
| Kanal 2 (CH2) | Elevasi Siku (*Elbow Pitch*) | TowerPro MG996R | 10° – 170° (Batas rentang kerja efektif) |
| Kanal 3 (CH3) | Fleksi Pergelangan (*Wrist Pitch*) | TowerPro MG996R | 0° – 180° (Penyejajaran orientasi *gripper*) |
| Kanal 4 (CH4) | Pencengkeram (*Gripper Jaw*) | TowerPro MG996R | 40° (Menjepit) – 120° (Terbuka penuh) |

---

## Lampiran 5. Algoritma Mode Posisi-Halus dan Penahan Posisi Netral (*Release-to-Hold*)-archonx

Berikut adalah rancangan pseudocode algoritma pemrosesan perintah kendali pada mikrokontroler penerima yang merealisasikan fitur mode posisi-halus (*fine-positioning mode*) dengan redaman gain serta penguncian posisi saat tuas dilepaskan (*release-to-hold*):

```c
// Struktur paket kendali yang diterima via Wi-Fi
struct ControlPacket {
    uint32_t t_send;       // Penanda waktu pengiriman paket (ms / us)
    int8_t stick_X;        // Nilai analog tuas sumbu X (-128 s.d. 127)
    int8_t stick_Y;        // Nilai analog tuas sumbu Y (-128 s.d. 127)
    bool btn_fine_mode;    // Status tombol trigger (true = Mode Posisi-Halus aktif)
    uint8_t selected_joint;// Seleksi artikulasi sendi tunggal (0 = Multi-DOF, 1..5 = Joint ID)
};

// Variabel status sudut tersimpan untuk masing-masing servo
float current_angle[5] = {90.0, 90.0, 90.0, 90.0, 60.0};
const int DEADZONE_THRESHOLD = 15;

void process_teleoperation(ControlPacket pkt) {
    // 1. Perhitungan latensi transmisi jaringan satu arah
    uint32_t t_receive = millis();
    uint32_t t_latency = t_receive - pkt.t_send;

    // 2. Evaluasi status Mode Posisi-Halus
    float gain = 1.0;
    if (pkt.btn_fine_mode == true) {
        // Pada mode halus, sensitivitas perintah diturunkan menjadi 25% (G = 0,25)
        gain = 0.25;
    }

    // 3. Filter deadzone tuas analog
    float input_X = 0.0;
    float input_Y = 0.0;
    if (abs(pkt.stick_X) > DEADZONE_THRESHOLD) {
        input_X = (float)pkt.stick_X / 127.0;
    }
    if (abs(pkt.stick_Y) > DEADZONE_THRESHOLD) {
        input_Y = (float)pkt.stick_Y / 127.0;
    }

    // 4. Mekanisme Release-to-Hold (Latching Posisi Saat Netral)
    // Apabila kedua tuas berada dalam deadzone (dilepaskan oleh operator):
    // Nilai input_X dan input_Y adalah 0, sehingga tidak ada delta sudut yang ditambahkan.
    // Posisi sudut servo dipertahankan secara stabil pada nilai current_angle terakhir.
    if (input_X != 0.0 || input_Y != 0.0) {
        if (pkt.selected_joint == 0) {
            // Mode Koordinasi Multi-DOF (Kinematika laju end-effector)
            current_angle[0] += (input_X * 2.0 * gain); // Rotasi basis
            current_angle[1] += (input_Y * 2.0 * gain); // Elevasi bahu
            current_angle[2] -= (input_Y * 1.5 * gain); // Elevasi siku koordinatif
        } else {
            // Mode Artikulasi Sendi Tunggal terpilih
            uint8_t j = pkt.selected_joint - 1;
            current_angle[j] += (input_Y * 2.5 * gain);
        }

        // Penegakan batas rentang sudut fisik (Clamping)
        for (int i = 0; i < 5; i++) {
            current_angle[i] = constrain(current_angle[i], MIN_ANGLE[i], MAX_ANGLE[i]);
        }
    }

    // 5. Pembaruan sinyal PWM ke modul PCA9685
    for (int i = 0; i < 5; i++) {
        uint16_t pulse = map_angle_to_pwm_counts(current_angle[i]);
        pca9685.setPWM(i, 0, pulse);
    }
}
```
