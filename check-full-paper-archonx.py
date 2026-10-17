"""Ticket 20 — compliance checks on the assembled DOCX/PDF."""
from __future__ import annotations

import os
import re
import sys
import zipfile
from collections import Counter

from docx import Document
from docx.shared import Cm, Pt
from pypdf import PdfReader

ROOT = r"C:\Users\Arkandhafy\OneDrive\Documents\The Hivemind\Dingle's research\SPC Eureka 2026"
DOCX = os.path.join(ROOT, "outputs", "SPC_FullPaper_AnargyaArkanDhafyHamdani.docx")
PDF = os.path.join(ROOT, "outputs", "SPC_FullPaper_AnargyaArkanDhafyHamdani.pdf")

HEADINGS = ["Abstrak", "PENDAHULUAN", "DAFTAR TEORI", "METODOLOGI", "HASIL DAN PEMBAHASAN",
            "KESIMPULAN DAN SARAN", "DAFTAR PUSTAKA", "LAMPIRAN"]
HEADINGS[2] = "DASAR TEORI"

fail = []
ok = []


def check(cond, msg):
    (ok if cond else fail).append(msg)


# ---------------------------------------------------------------- docx
d = Document(DOCX)
sec = d.sections[0]
print("=== PAGE SETUP ===")
print("page", round(sec.page_width.cm, 2), "x", round(sec.page_height.cm, 2))
print("margins L/R/T/B", *(round(getattr(sec, a).cm, 2) for a in
                          ("left_margin", "right_margin", "top_margin", "bottom_margin")))
check(abs(sec.page_width.cm - 21.0) < 0.05 and abs(sec.page_height.cm - 29.7) < 0.05, "A4 page size")
check(all(abs(getattr(sec, a).cm - 2.54) < 0.02 for a in
          ("left_margin", "right_margin", "top_margin", "bottom_margin")), "2.54 cm margins on all sides")

# headings in order
heads = [(p.style.name, p.text.strip()) for p in d.paragraphs if p.style.name.startswith("Heading")]
h2 = [t for s, t in heads if s == "Heading 2"]
print("\n=== H2 HEADINGS (order) ===")
for t in h2:
    print("  ", t)
missing = [h for h in HEADINGS if h not in h2]
check(not missing, f"all nine headings present (missing={missing})")
order = [h for h in h2 if h in HEADINGS]
check(order == HEADINGS, f"heading order correct ({order})")

# fonts and sizes
fonts, sizes, anom = Counter(), Counter(), []
for p in d.paragraphs:
    for r in p.runs:
        if not r.text.strip():
            continue
        name = r.font.name or d.styles["normal"].font.name
        size = r.font.size.pt if r.font.size else (d.styles["normal"].font.size.pt if d.styles["normal"].font.size else None)
        fonts[name] += 1
        sizes[size] += 1
        if name not in ("Times New Roman", "Courier New", "Cambria Math"):
            anom.append((name, r.text[:40]))
print("\n=== FONTS ===", dict(fonts))
print("=== SIZES ===", dict(sizes))
print("=== NON-TEMPLATE FONTS ===", anom[:5])
check(not anom, "only Times New Roman / Courier New (code) / Cambria Math (equations) used")
check(sizes.get(12.0, 0) > 0, "12 pt body text present")

# line spacing
ls = Counter()
for p in d.paragraphs:
    if p.text.strip():
        v = p.paragraph_format.line_spacing
        ls[v] += 1
print("=== LINE SPACING ===", dict(ls))

# watermark leakage
alltext = "\n".join(p.text for p in d.paragraphs)
prose_text = "\n".join(
    p.text for p in d.paragraphs
    if not p.runs or any((r.font.name or "") != "Courier New" for r in p.runs)
)
for t in d.tables:
    for row in t.rows:
        for c in row.cells:
            alltext += "\n" + c.text
check("-archonx" not in alltext, "no -archonx watermark left in the assembled document")
scaffold = [p.text[:60] for p in d.paragraphs if "scaffolding" in p.text.lower() or "Catatan draf" in p.text]
check(not scaffold, f"no drafting scaffolding left ({scaffold[:3]})")

# ---------------------------------------------------------------- pdf
pdf = PdfReader(PDF)
pages = [pg.extract_text() or "" for pg in pdf.pages]
print("\n=== PDF ===", len(pages), "pages")
starts = {}
for i, txt in enumerate(pages, 1):
    flat = " ".join(txt.split())
    for h in HEADINGS:
        if h not in starts and re.search(rf"(?<![A-Za-z]){re.escape(h)}(?![A-Za-z])", flat):
            starts[h] = i
print("section start pages:", starts)
body_start = starts.get("Abstrak")
bib_start = starts.get("DAFTAR PUSTAKA")
lamp_start = starts.get("LAMPIRAN")
if body_start and bib_start:
    body_pages = bib_start - body_start
    print(f"BODY PAGES (Abstrak..Kesimpulan dan Saran) = {body_pages}")
    check(10 <= body_pages <= 20, f"body length within 10-20 pages (got {body_pages})")
    print(f"bibliography pages = {lamp_start - bib_start if lamp_start else '?'}")
    print(f"appendix pages = {len(pages) - lamp_start + 1 if lamp_start else '?'}")

full = "\n".join(pages)
flat_all = " ".join(full.split())

print("\n=== FORBIDDEN CONTENT (whole PDF) ===")
forbidden = {
    "glove/IMU": r"glove|sarung tangan|\bIMU\b|MPU ?6050|flex sensor",
    "web app / smartphone interface": r"aplikasi web|antarmuka web|web joystick|Blynk|\bsmartphone\b|ponsel pintar",
    "analog physical joystick": r"joystick analog|stik analog fisik",
    "watermark": r"-archonx",
}
for name, pat in forbidden.items():
    hits = [m.group(0) for m in re.finditer(pat, flat_all, re.I)]
    print(f"  {name}: {len(hits)} {hits[:6]}")
    check(not hits, f"zero occurrences of {name}")

print("\n=== CITATIONS ===")
cite_text = prose_text + "\n" + "\n".join(
    c.text for t in d.tables for row in t.rows for c in row.cells
)
nums = sorted({int(x) for x in re.findall(r"\[(\d+)\]", cite_text)})
print("bracket numbers found:", nums)
check(nums == list(range(1, 12)), f"citation numbers [1]-[11] contiguous ({nums})")

print("\n=== CATEGORY CHECKS ===")
checks = {
    "smoothing-is-a-hypothesis caveat": r"tidak ditemukan bukti langsung|hipotesis",
    "2-second hold is project-defined": r"project-defined|dirumuskan secara internal",
    "expectation labelling": r"target pra-registrasi|ekspektasi",
    "frozen problem statement": r"radioaktif",
}
for name, pat in checks.items():
    hits = re.findall(pat, flat_all, re.I) if name != "frozen problem statement" else None
    if hits is not None:
        print(f"  {name}: {len(hits)} matches")
        check(bool(hits), name)

print("\n=== RESULT ===")
for m in ok:
    print("  PASS:", m)
for m in fail:
    print("  FAIL:", m)
print(f"\n{len(ok)} passed, {len(fail)} failed")
sys.exit(1 if fail else 0)
