import os

import docx
import docx.shared

import task_1

if __name__ == '__main__':
    path = "modified.docx"
    doc = docx.Document()
    styles = doc.styles()
    styles['Normal'].font.name = 'Arial'

    # Change default font size
    styles['Normal'].font.size = 14
    doc.save(path)

    task_1.generate_task_1(os.path.abspath(path))
