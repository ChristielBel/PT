import os
import random

from docx.enum.text import WD_PARAGRAPH_ALIGNMENT as align

import generation.writer as writer

source_doc_path = os.path.dirname(os.path.abspath(__file__)) + "/texts/task6.docx"
first_val = 15
second_val = 8
third_val = 7
s = first_val + second_val + third_val


def generate_task(target_doc_path):
    global first_val
    global second_val
    global third_val
    global s

    first_val = random.randint(5, 15)
    second_val = random.randint(5, 15)
    third_val = random.randint(5, 15)
    s = first_val + second_val + third_val

    replacement_values = [s, first_val, second_val, third_val]

    writer.replace_placeholders_and_write_to_target(source_doc_path, target_doc_path, replacement_values)


def calculate_task(target_doc_path):
    global first_val
    global second_val
    global third_val
    global s

    ans = first_val / s * 1 / 6 + second_val / s * 1 / 6 + third_val / s * 1 / 6

    writer.write_text(target_doc_path,
                      "6. " + f'{ans:.5f}',
                      "Arial", 14,
                      align.LEFT,
                      False)
