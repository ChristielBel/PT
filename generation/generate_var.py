import docx
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT as align

from generation import writer


def generate_var(task_functions, ans_functions, check_values, doc_path, ans_path, num):

    # Add brakes
    if num > 1:
        doc1 = docx.Document(doc_path)
        doc1.add_page_break()
        doc1.save(doc_path)
        doc1 = docx.Document(ans_path)
        doc1.add_page_break()
        doc1.save(ans_path)

    # Writing header
    header = "Вариант " + str(num) + '\n'

    writer.write_text(doc_path, header, "Arial", 14, align.CENTER, True)
    writer.write_text(ans_path, header, "Arial", 14, align.CENTER, True)

    # Starting generating new var
    for i in range(len(check_values)):
        if check_values[i].get():
            task_functions[i](doc_path)
            ans_functions[i](ans_path)
