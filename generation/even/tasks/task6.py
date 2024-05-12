import os
import random

from docx.enum.text import WD_PARAGRAPH_ALIGNMENT as align

import generation.writer as writer

source_doc_path = os.path.dirname(os.path.abspath(__file__)) + "/texts/task_6.docx"

first_val = 0.2
second_val = 0.3
third_val = 0.8


def generate_task(target_doc_path):
    global first_val
    global second_val
    global third_val

    first_val = round(random.uniform(0.2, 0.9), 2)
    second_val = round(random.uniform(0.3, 0.9), 2)
    third_val = round(random.uniform(0.8, 0.9), 2)

    replacement_values = [first_val, second_val, third_val]

    writer.replace_placeholders_and_write_to_target(source_doc_path, target_doc_path, replacement_values, "*")


def calculate_task(target_doc_path):
    global first_val
    global second_val
    global third_val

    ans = (1 - first_val) * 1 / 3 + (1 - second_val) * 1 / 3 + (1 - third_val) * 1 / 3

    writer.write_text(target_doc_path,
                      "6. " + f'{ans:.6f}',
                      "Arial", 14,
                      align.LEFT,
                      False)
