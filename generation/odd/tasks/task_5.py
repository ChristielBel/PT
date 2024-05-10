import os
import random

from docx.enum.text import WD_PARAGRAPH_ALIGNMENT as align

import generation.writer as writer

source_doc_path = os.path.dirname(os.path.abspath(__file__)) + "/texts/task5.docx"
first_val = 20
second_val = 30


def generate_task(target_doc_path):
    global first_val
    global second_val

    first_val = random.randint(1, 8) * 10
    second_val = random.randint(1, 8) * 10

    replacement_values = [first_val, second_val]

    writer.replace_placeholders_and_write_to_target(source_doc_path, target_doc_path, replacement_values)


def calculate_task(target_doc_path):
    global first_val
    global second_val

    s = first_val + second_val

    ans = first_val / s * (first_val - 1) / (s - 1) * (first_val - 2) / (s - 2)

    writer.write_text(target_doc_path,
                      "5. " + f'{ans:.5f}',
                      "Arial", 14,
                      align.LEFT,
                      False)
