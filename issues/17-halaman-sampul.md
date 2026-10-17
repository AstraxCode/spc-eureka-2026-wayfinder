# 17: Halaman Sampul

**What to build:** The cover page in the official template, using the provisional title until
ticket 10 lands.

**Blocked by:** 10 (final title; a provisional title is acceptable until this closes).

**Status:** resolved

- [x] Follows the official template's cover layout.
- [x] Title is drawn from the single title source (expand–contract) — substituting ticket 10's
      value needs one edit and no rewrite.
- [x] Carries the `-archonx` watermark convention on the title.
- [x] Author/team fields filled per the template.

## Answer

**Resolved 2026-10-17 (ArchonX).** Draft: `.scratch/spc-full-paper/draft/17-halaman-sampul-archonx.md`.

### Template Compliance and Metadata Alignment

The cover page format mirrors the official competition template (`Full paper/Format Full Paper.docx`):
1. **Outer Cover Page (Halaman Sampul Luar):** Competition title (`SCIENCE PROJECT COMPETITION EUREKA! ITB 2026`), Title, Author attribution (`oleh <Nama Anggota>`), Institution block (`HIMPUNAN MAHASISWA FISIKA / PROGRAM STUDI FISIKA / INSTITUT TEKNOLOGI BANDUNG / 2026`).
2. **Inner Header & Metadata (Halaman Judul Dalam):** Includes school affiliation (`SMAIT As-Syifa Boarding School Jalancagak, Subang, Jawa Barat, Indonesia`), organizer name, contact email (`arkn981@gmail.com`), subtheme (`Instrumentasi, Elektronika, dan Sistem Cerdas`), and completion date (`17 Oktober 2026`).

### Single Title Source

Drawn directly from `.scratch/spc-full-paper/title.md` (locked in ticket 10):
- `TITLE_INTERNAL`: *Mode Posisi-Halus Berbasis Stik PS2 untuk Akurasi Penempatan Lengan Robot Teleoperasi 5-DOF pada Penanganan Bahan Radioaktif-archonx*
- `TITLE_SUBMISSION`: *Mode Posisi-Halus Berbasis Stik PS2 untuk Akurasi Penempatan Lengan Robot Teleoperasi 5-DOF pada Penanganan Bahan Radioaktif*

### Verification Run (Executed)

Programmatic verification via Python:
- Title matches `title.md` exactly: `TITLE_INTERNAL present: True`, `TITLE_SUBMISSION present: True`.
- All markdown headers end with `-archonx` watermark convention: `True` (4/4 headers verified).
- Prohibited wording audit: `aplikasi web`: 0, `smartphone app`: 0, `sarung tangan sensor`: 0, `glove`: 0.
- Author, affiliation, subtheme, and email verified against primary team submission records (`Extended abstract/Abstract asbosch prime.docx`).

Pre-edit backup: `.scratch/_backups/spc-full-paper-20261017-1337/17-halaman-sampul.md`.
