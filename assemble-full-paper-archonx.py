"""Ticket 20 — assemble the SPC Eureka 2026 full paper into the official template.

Reads the nine section drafts in .scratch/spc-full-paper/draft/, strips the
`Catatan draf (scaffolding ...)` sections and the internal `-archonx` watermark
suffix, and writes a DOCX whose layout follows `Full paper/Format Full Paper.docx`
(TNR 12 pt body, 1.15 spacing, A4, 2.54 cm margins, page-numbered footer).

Usage:
    ./.venv/Scripts/python.exe assemble-full-paper-archonx.py
"""
from __future__ import annotations

import copy
import os
import re
import sys

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK, WD_LINE_SPACING, WD_TAB_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

ROOT = os.path.dirname(os.path.abspath(__file__))
DRAFT = os.path.join(ROOT, ".scratch", "spc-full-paper", "draft")
TEMPLATE = os.path.join(ROOT, "Full paper", "Format Full Paper.docx")
TITLE_FILE = os.path.join(ROOT, ".scratch", "spc-full-paper", "title.md")
OUT_DIR = os.path.join(ROOT, "outputs")

BODY_FONT = "Times New Roman"
MONO_FONT = "Courier New"
MATH_FONT = "Cambria Math"

TEXT_WIDTH_CM = 21.0 - 2.54 * 2  # A4 width minus the guidebook margins

# (heading printed in the paper, draft file, order)
SECTIONS = [
    ("Abstrak", "16-abstrak-archonx.md"),
    ("PENDAHULUAN", "12-pendahuluan-archonx.md"),
    ("DASAR TEORI", "11-dasar-teori-archonx.md"),
    ("METODOLOGI", "13-metodologi-archonx.md"),
    ("HASIL DAN PEMBAHASAN", "14-hasil-dan-pembahasan-archonx.md"),
    ("KESIMPULAN DAN SARAN", "15-kesimpulan-dan-saran-archonx.md"),
    ("DAFTAR PUSTAKA", "18-daftar-pustaka-archonx.md"),
    ("LAMPIRAN", "19-lampiran-archonx.md"),
]

TEAM = [
    "Anargya Arkan Dhafy Hamdani",
    "Muhamad Naufal Firdaus",
    "Fakhri Ahmad Kendri",
]
SCHOOL = "SMAIT As-Syifa Boarding School Jalancagak, Subang, Jawa Barat, Indonesia"
EMAIL = "arkn981@gmail.com"
SUBTEMA = "Instrumentasi, Elektronika, dan Sistem Cerdas"
DATE = "17 Oktober 2026"


# ---------------------------------------------------------------- helpers
def read_title() -> str:
    txt = open(TITLE_FILE, encoding="utf-8").read()
    m = re.search(r"^TITLE_SUBMISSION:\s*(.+)$", txt, re.M)
    if not m:
        raise SystemExit("TITLE_SUBMISSION not found in title.md")
    return m.group(1).strip()


def strip_watermark(text: str) -> str:
    """Remove the internal -archonx watermark suffix from headings."""
    text = re.sub(r"-archonx\b", "", text)
    return text.strip()


def set_run_font(run, name=BODY_FONT, size=12, bold=None, italic=None):
    run.font.name = name
    run.font.size = Pt(size)
    if bold is not None:
        run.font.bold = bold
    if italic is not None:
        run.font.italic = italic
    rpr = run._element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.append(rfonts)
    for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rfonts.set(qn(attr), name)


def fmt_par(p, align=None, before=0, after=6, line=1.15, keep_next=False,
            left=None, hanging=None, first=None):
    pf = p.paragraph_format
    if align is not None:
        p.alignment = align
    pf.space_before = Pt(before)
    pf.space_after = Pt(after)
    if line is None:
        pf.line_spacing_rule = WD_LINE_SPACING.SINGLE
    else:
        pf.line_spacing = line
    pf.keep_with_next = keep_next
    pf.widow_control = True
    if left is not None:
        pf.left_indent = Cm(left)
    if hanging is not None:
        pf.first_line_indent = Cm(-hanging)
    if first is not None:
        pf.first_line_indent = Cm(first)


INLINE_RE = re.compile(r"(\*\*.+?\*\*|\*[^*\n]+?\*|`[^`\n]+?`)")
SUB_RE = re.compile(r"(?<![A-Za-z0-9])([A-Za-z\u03b1-\u03c9\u0391-\u03a9\u03c4])((?:_[A-Za-z0-9\u03b1-\u03c9]+)+)")


def add_inline(p, text, size=12, mono=MONO_FONT, base_italic=False, base_bold=False):
    """Add runs to paragraph, honouring **bold**, *italic* and `code`; nested emphasis recurses."""
    for tok in INLINE_RE.split(text):
        if not tok:
            continue
        bold, italic, name = base_bold or None, base_italic or None, BODY_FONT
        body, nested = tok, None
        if tok.startswith("**") and tok.endswith("**") and len(tok) > 4:
            body, nested = tok[2:-2], "bold"
        elif tok.startswith("*") and tok.endswith("*") and len(tok) > 2:
            body, nested = tok[1:-1], "italic"
        elif tok.startswith("`") and tok.endswith("`") and len(tok) > 2:
            body, name = tok[1:-1], mono
        if nested == "bold":
            add_inline(p, body, size, mono, base_italic, True)
            continue
        if nested == "italic":
            add_inline(p, body, size, mono, True, base_bold)
            continue
        run = p.add_run(body)
        set_run_font(run, name, size, bold=bold, italic=italic)


def add_equation(doc, text, number):
    """Centred equation with the number flush right (template convention)."""
    p = doc.add_paragraph()
    fmt_par(p, after=6, line=1.0)
    pf = p.paragraph_format
    pf.tab_stops.add_tab_stop(Cm(TEXT_WIDTH_CM / 2), WD_TAB_ALIGNMENT.CENTER)
    pf.tab_stops.add_tab_stop(Cm(TEXT_WIDTH_CM), WD_TAB_ALIGNMENT.RIGHT)
    p.add_run("\t")
    # subscripts: x_final -> x + subscript(final)
    pos = 0
    for m in SUB_RE.finditer(text):
        if m.start() > pos:
            r = p.add_run(text[pos:m.start()]); set_run_font(r, MATH_FONT, 11)
        r = p.add_run(m.group(1)); set_run_font(r, MATH_FONT, 11)
        r2 = p.add_run(m.group(2).replace("_", ""))
        set_run_font(r2, MATH_FONT, 11)
        r2.font.subscript = True
        pos = m.end()
    if pos < len(text):
        r = p.add_run(text[pos:]); set_run_font(r, MATH_FONT, 11)
    p.add_run("\t")
    r = p.add_run(f"({number})"); set_run_font(r, BODY_FONT, 12)


def add_code_block(doc, lines):
    if doc.paragraphs:
        doc.paragraphs[-1].paragraph_format.keep_with_next = True
    maxchars = max((len(l) for l in lines), default=1)
    size = min(8.5, 15.0 / (0.0212 * max(maxchars, 1)))
    size = max(6.5, round(size * 2) / 2)
    for i, line in enumerate(lines):
        p = doc.add_paragraph()
        fmt_par(p, align=WD_ALIGN_PARAGRAPH.LEFT, before=0, after=0, line=None,
                keep_next=(i < len(lines) - 1))
        p.paragraph_format.left_indent = Cm(0.4)
        r = p.add_run(line if line.strip() else " ")
        set_run_font(r, MONO_FONT, size)


def _borders(table, sz=8):
    tbl = table._tbl
    tblPr = tbl.tblPr
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "bottom", "insideH"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), "4" if edge == "insideH" else str(sz))
        el.set(qn("w:space"), "0"); el.set(qn("w:color"), "000000")
        borders.append(el)
    for edge in ("left", "right", "insideV"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "nil")
        borders.append(el)
    tblPr.append(borders)


def _row_props(row, header=False):
    trPr = row._tr.get_or_add_trPr()
    cant = OxmlElement("w:cantSplit")
    trPr.append(cant)
    if header:
        th = OxmlElement("w:tblHeader")
        trPr.append(th)


def _col_widths(rows, ncols):
    """Widths that never break a number mid-token, then share leftover space."""
    mins, wants = [], []
    for ci in range(ncols):
        cells = [r[ci].replace("<br>", " ") for r in rows if ci < len(r)]
        longest_word = max(max((len(w) for w in c.split()), default=1) for c in cells)
        avg_total = sum(len(c) for c in cells) / max(1, len(cells))
        mins.append(min(5.0, longest_word * 0.19 + 0.28))
        wants.append(max(2.4, avg_total * 0.19 + 0.28))
    if sum(mins) > TEXT_WIDTH_CM:            # pathological: scale the minimums
        k = TEXT_WIDTH_CM / sum(mins)
        return [m * k for m in mins]
    extra = TEXT_WIDTH_CM - sum(mins)
    weight = [max(0.05, w - m) for w, m in zip(wants, mins)]
    wsum = sum(weight)
    return [m + extra * w / wsum for m, w in zip(mins, weight)]


def _cell_margins(table, cm=0.08):
    tblPr = table._tbl.tblPr
    mar = OxmlElement("w:tblCellMar")
    for side in ("top", "left", "bottom", "right"):
        el = OxmlElement(f"w:{side}")
        el.set(qn("w:w"), str(int(cm * 567)))
        el.set(qn("w:type"), "dxa")
        mar.append(el)
    tblPr.append(mar)


def _header_rule(cell, sz=6):
    tcPr = cell._tc.get_or_add_tcPr()
    borders = OxmlElement("w:tcBorders")
    el = OxmlElement("w:bottom")
    el.set(qn("w:val"), "single"); el.set(qn("w:sz"), str(sz))
    el.set(qn("w:space"), "0"); el.set(qn("w:color"), "000000")
    borders.append(el)
    tcPr.append(borders)


def add_table(doc, rows):
    if doc.paragraphs:
        doc.paragraphs[-1].paragraph_format.keep_with_next = True
    ncols = len(rows[0])
    table = doc.add_table(rows=0, cols=ncols)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    _borders(table)
    _cell_margins(table)
    widths = _col_widths(rows, ncols)
    tsize = 10 if ncols <= 4 else 9
    for ri, row in enumerate(rows):
        tr = table.add_row()
        _row_props(tr, header=(ri == 0))
        cells = tr.cells
        for ci, raw in enumerate(row[:ncols]):
            cell = cells[ci]
            cell.width = Cm(widths[ci])
            cell.text = ""
            p = cell.paragraphs[0]
            fmt_par(p, align=WD_ALIGN_PARAGRAPH.LEFT, before=0, after=0, line=1.0)
            parts = raw.split("<br>")
            for pi, part in enumerate(parts):
                if pi:
                    p.add_run().add_break()
                add_inline(p, part.strip(), size=tsize)
                if ri == 0:
                    for run in p.runs:
                        run.font.bold = True
        if ri == 0:
            for cell in cells:
                _header_rule(cell)
    # breathing room after the table
    sp = doc.add_paragraph()
    fmt_par(sp, after=0, line=None)
    sp.add_run("").font.size = Pt(6)


# ---------------------------------------------------------------- parsing
def split_sections(path):
    """Yield (kind, payload) blocks for one draft file, scaffolding removed."""
    raw = open(path, encoding="utf-8").read().replace("\r\n", "\n")
    lines = raw.split("\n")
    out = []
    i = 0
    in_fence = False
    fence = []
    para = []

    def flush_para():
        nonlocal para
        if para:
            text = " ".join(x.strip() for x in para).strip()
            if text:
                out.append(("p", strip_watermark(text)))
            para = []

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if in_fence:
            if stripped.startswith("```"):
                out.append(("code", fence))
                fence, in_fence = [], False
            else:
                fence.append(line.rstrip())
            i += 1
            continue

        if stripped.startswith("```"):
            flush_para()
            in_fence = True
            fence = []
            i += 1
            continue

        # scaffolding sections are always last: stop at the marker
        if re.match(r"^#{1,6}\s+Catatan draf \(scaffolding", stripped):
            break

        m = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        if m:
            flush_para()
            level, text = len(m.group(1)), strip_watermark(m.group(2))
            if level == 1:          # draft title -> replaced by the real section heading
                i += 1
                continue
            text = text.replace("`", "").replace("**", "").replace("*", "")
            text = re.sub(r"\s*\([a-z0-9][a-z0-9-]{6,}\)\s*$", "", text)  # drop internal file slugs
            out.append((f"h{min(level, 4)}", text))
            i += 1
            continue

        if not stripped:
            flush_para()
            i += 1
            continue

        if stripped in ("---", "***", "___"):
            flush_para()
            i += 1
            continue

        if stripped.startswith("|") and stripped.endswith("|"):
            flush_para()
            block = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                block.append(lines[i].strip())
                i += 1
            out.append(("table", block))
            continue

        bm = re.match(r"^[-*]\s+(.*)$", stripped)
        if bm:
            flush_para()
            text = strip_watermark(bm.group(1))
            i += 1
            # markdown wraps long bullets onto indented continuation lines
            while i < len(lines):
                nxt = lines[i].strip()
                if (not nxt or re.match(r"^([-*]\s|\d+\.\s|#{1,6}\s|\||```|>)", nxt)
                        or re.match(r"^#{1,6}\s", nxt)):
                    break
                text += " " + strip_watermark(nxt)
                i += 1
            out.append(("bullet", text))
            continue

        nm = re.match(r"^(\d+)\.\s+(.*)$", stripped)
        if nm:
            flush_para()
            text = f"{nm.group(1)}. {strip_watermark(nm.group(2))}"
            i += 1
            while i < len(lines):
                nxt = lines[i].strip()
                if (not nxt or re.match(r"^([-*]\s|\d+\.\s|#{1,6}\s|\||```|>)", nxt)):
                    break
                text += " " + strip_watermark(nxt)
                i += 1
            out.append(("num", text))
            continue

        if stripped.startswith(">"):
            flush_para()
            out.append(("quote", strip_watermark(stripped.lstrip("> ").strip())))
            i += 1
            continue

        para.append(stripped)
        i += 1

    flush_para()
    return out


def parse_table(block):
    rows = []
    aligns = None
    for idx, line in enumerate(block):
        cells = [c.strip() for c in line.strip("|").split("|")]
        if all(re.fullmatch(r":?-{2,}:?", c) for c in cells):
            aligns = cells
            continue
        rows.append([strip_watermark(c) for c in cells])
    return rows


EQ_RE = re.compile(r"^(.*?[^\s])\s{2,}\((\d+)\)$")


# ---------------------------------------------------------------- build
def build():
    title = read_title()
    doc = Document(TEMPLATE)

    body = doc.element.body
    for child in list(body):
        if child.tag == qn("w:sectPr"):
            continue
        body.remove(child)

    # single section: A4, 2.54 cm on every side
    sec = doc.sections[0]
    sec.page_width = Cm(21.0)
    sec.page_height = Cm(29.7)
    for attr in ("left_margin", "right_margin", "top_margin", "bottom_margin"):
        setattr(sec, attr, Cm(2.54))

    # centred page number from page 2 onward (cover page stays clean)
    sec.different_first_page_header_footer = True
    fp = sec.first_page_footer.paragraphs[0]
    fp.text = ""
    ftr = sec.footer
    pnum = ftr.paragraphs[0]
    pnum.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = pnum.add_run()
    set_run_font(run, BODY_FONT, 10)
    fld_begin = OxmlElement("w:fldChar"); fld_begin.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText"); instr.set(qn("xml:space"), "preserve"); instr.text = " PAGE "
    fld_end = OxmlElement("w:fldChar"); fld_end.set(qn("w:fldCharType"), "end")
    run._r.append(fld_begin); run._r.append(instr); run._r.append(fld_end)

    # base style: TNR 12 / 1.15
    normal = doc.styles["normal"]
    normal.font.name = BODY_FONT
    normal.font.size = Pt(12)
    normal.paragraph_format.line_spacing = 1.15
    normal.paragraph_format.space_after = Pt(6)
    rpr = normal.element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts"); rpr.append(rfonts)
    for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rfonts.set(qn(attr), BODY_FONT)

    # ---------------- cover page (outer)
    def cover_line(text, size=14, bold=True, before=0, after=0, align=WD_ALIGN_PARAGRAPH.CENTER):
        p = doc.add_paragraph()
        fmt_par(p, align=align, before=before, after=after, line=1.15)
        r = p.add_run(text)
        set_run_font(r, BODY_FONT, size, bold=bold)
        return p

    cover_line("SCIENCE PROJECT COMPETITION", 14)
    cover_line("EUREKA! ITB 2026", 14, after=36)
    cover_line(title, 16, after=24)
    cover_line("oleh", 12, bold=False, after=6)
    cover_line(", ".join(TEAM), 12, after=6)
    for _ in range(8):
        p = doc.add_paragraph(); fmt_par(p, after=0, line=1.0)
    cover_line("HIMPUNAN MAHASISWA FISIKA")
    cover_line("PROGRAM STUDI FISIKA")
    cover_line("INSTITUT TEKNOLOGI BANDUNG")
    cover_line("2026")

    # page break -> inner title page
    pb = doc.add_paragraph()
    fmt_par(pb, after=0, line=1.0)
    pb.add_run().add_break(WD_BREAK.PAGE)

    # ---------------- inner title block
    p = doc.add_paragraph()
    fmt_par(p, align=WD_ALIGN_PARAGRAPH.CENTER, after=0, line=1.15)
    r = p.add_run("SCIENCE PROJECT COMPETITION"); set_run_font(r, BODY_FONT, 12, bold=True)
    p = doc.add_paragraph()
    fmt_par(p, align=WD_ALIGN_PARAGRAPH.CENTER, after=12, line=1.15)
    r = p.add_run("EUREKA! ITB 2026"); set_run_font(r, BODY_FONT, 12, bold=True)

    p = doc.add_paragraph()
    fmt_par(p, align=WD_ALIGN_PARAGRAPH.CENTER, after=12, line=1.15)
    r = p.add_run(title); set_run_font(r, BODY_FONT, 14, bold=True)

    for line in (", ".join(TEAM), SCHOOL, "Himpunan Mahasiswa Fisika",
                 "Institut Teknologi Bandung", f"Email: {EMAIL}", f"Subtema: {SUBTEMA}"):
        p = doc.add_paragraph()
        fmt_par(p, align=WD_ALIGN_PARAGRAPH.CENTER, after=0, line=1.15)
        r = p.add_run(line); set_run_font(r, BODY_FONT, 12)
    p = doc.add_paragraph()
    fmt_par(p, align=WD_ALIGN_PARAGRAPH.CENTER, after=12, line=1.15)
    r = p.add_run(""); set_run_font(r, BODY_FONT, 12)
    p = doc.add_paragraph()
    fmt_par(p, align=WD_ALIGN_PARAGRAPH.CENTER, after=12, line=1.15)
    r = p.add_run(f"Tanggal: {DATE}"); set_run_font(r, BODY_FONT, 12)

    # ---------------- sections
    stats = {}
    for heading, fname in SECTIONS:
        path = os.path.join(DRAFT, fname)
        blocks = split_sections(path)
        stats[heading] = len(blocks)

        h = doc.add_paragraph()
        h.style = doc.styles["Heading 2"]
        fmt_par(h, align=WD_ALIGN_PARAGRAPH.LEFT, before=12, after=6, line=1.15, keep_next=True)
        if heading in ("PENDAHULUAN", "DAFTAR PUSTAKA", "LAMPIRAN"):
            h.paragraph_format.page_break_before = True
        r = h.add_run(heading)
        set_run_font(r, BODY_FONT, 12, bold=True)
        r.font.color.rgb = RGBColor(0, 0, 0)

        first_para_after_heading = True
        for kind, payload in blocks:
            if kind == "h2":
                p = doc.add_paragraph()
                p.style = doc.styles["Heading 3"]
                fmt_par(p, align=WD_ALIGN_PARAGRAPH.LEFT, before=10, after=4, line=1.15, keep_next=True)
                r = p.add_run(payload); set_run_font(r, BODY_FONT, 12, bold=True)
                r.font.color.rgb = RGBColor(0, 0, 0)
            elif kind == "h3":
                p = doc.add_paragraph()
                p.style = doc.styles["Heading 4"]
                fmt_par(p, align=WD_ALIGN_PARAGRAPH.LEFT, before=8, after=4, line=1.15, keep_next=True)
                r = p.add_run(payload); set_run_font(r, BODY_FONT, 12, bold=True)
                r.font.color.rgb = RGBColor(0, 0, 0)
            elif kind == "h4":
                p = doc.add_paragraph()
                fmt_par(p, align=WD_ALIGN_PARAGRAPH.LEFT, before=6, after=4, line=1.15, keep_next=True)
                r = p.add_run(payload); set_run_font(r, BODY_FONT, 12, bold=True)
            elif kind == "p":
                m = EQ_RE.match(payload)
                if m and len(payload) < 200:
                    add_equation(doc, m.group(1).strip(), m.group(2))
                    continue
                cap = re.match(r"^\**\s*(Tabel|Gambar)\s+\d+\.", payload)
                if cap:
                    p = doc.add_paragraph()
                    fmt_par(p, align=WD_ALIGN_PARAGRAPH.CENTER, before=6, after=4,
                            line=1.0, keep_next=True)
                    add_inline(p, payload.strip("*"), size=10, base_italic=True)
                    continue
                if heading == "DAFTAR PUSTAKA" and re.match(r"^\[\d+\]", payload):
                    p = doc.add_paragraph()
                    fmt_par(p, align=WD_ALIGN_PARAGRAPH.LEFT, after=6, line=1.15,
                            left=0.9, hanging=0.9)
                    add_inline(p, payload.replace("2x2", "2\u00d72"), size=12)
                    continue
                p = doc.add_paragraph()
                fmt_par(p, align=WD_ALIGN_PARAGRAPH.JUSTIFY, after=6, line=1.15)
                if heading == "Abstrak":
                    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                add_inline(p, payload.replace("2x2", "2\u00d72"), size=12)
                first_para_after_heading = False
            elif kind == "bullet":
                p = doc.add_paragraph()
                fmt_par(p, align=WD_ALIGN_PARAGRAPH.JUSTIFY, after=3, line=1.15,
                        left=0.75, hanging=0.4)
                add_inline(p, "\u2022 " + payload, size=12)
            elif kind == "num":
                p = doc.add_paragraph()
                fmt_par(p, align=WD_ALIGN_PARAGRAPH.JUSTIFY, after=3, line=1.15,
                        left=0.75, hanging=0.4)
                add_inline(p, payload, size=12)
            elif kind == "quote":
                p = doc.add_paragraph()
                fmt_par(p, align=WD_ALIGN_PARAGRAPH.JUSTIFY, after=6, line=1.15, left=0.75)
                add_inline(p, payload, size=12, base_italic=True)
            elif kind == "code":
                add_code_block(doc, payload)
            elif kind == "table":
                add_table(doc, parse_table(payload))
            else:
                raise SystemExit(f"unknown block {kind}")

    os.makedirs(OUT_DIR, exist_ok=True)
    out = os.path.join(OUT_DIR, "SPC_FullPaper_AnargyaArkanDhafyHamdani.docx")
    doc.save(out)
    print("wrote", out)
    for k, v in stats.items():
        print(f"  {k:24} blocks={v}")
    return out


if __name__ == "__main__":
    build()
