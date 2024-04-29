import random

from docx import Document


def generate_task_1(target_doc_path):
    first_val = random.randint(20, 40)
    second_val = random.randint(5, int(first_val / 2))
    replacement_values = [str(first_val), str(second_val)]
    # Open the source document
    source_doc = Document("Task1.docx")
    style = source_doc.styles()

    # Initialize index to track replacement value
    replacement_index = 0

    # Clone the source document
    target_doc = Document(target_doc_path)

    # Iterate over paragraphs
    for paragraph in source_doc.paragraphs:
        # Place all values to all paragraphs
        print(paragraph.text)
        while paragraph.text.find("+") != -1:
            paragraph.text = paragraph.text.replace("+", replacement_values[replacement_index], 1)
            print(paragraph.text.find("+"))

            replacement_index += 1

        target_doc.add_paragraph(paragraph.text)

    # Save the modified document
    target_doc.save(target_doc_path)
