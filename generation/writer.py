import docx
from docx.shared import Pt


def write_text(doc_path, text, font_name, font_size, alignment, isBold):
    doc = docx.Document(doc_path)

    paragraph = doc.add_paragraph()
    paragraph.alignment = alignment

    run = paragraph.add_run(text)
    font = run.font
    font.name = font_name
    font.size = Pt(font_size)
    font.bold = isBold

    doc.save(doc_path)
