import os
import random

from docx.enum.text import WD_PARAGRAPH_ALIGNMENT as align

import generation.writer as writer

source_doc_path = os.path.dirname(os.path.abspath(__file__)) + "/texts/task_3.docx"

first_val = 0.4
second_val = 0.8


def generate_task(target_doc_path):
    global first_val
    global second_val

    first_val = round(random.uniform(0.4, 0.9), 2)
    second_val = round(random.uniform(0.8, 0.9), 2)
    replacement_values = [first_val, second_val]

    writer.replace_placeholders_and_write_to_target(source_doc_path, target_doc_path, replacement_values, "*")


def calculate_task(target_doc_path):
    global first_val
    global second_val

    ans1 = first_val * second_val
    ans2 = first_val * (1 - second_val)
    ans3 = (1 - first_val) * (1 - second_val)

    writer.write_text(target_doc_path,
                      "3. а: " + f'{ans1:.15f}' + "\n    б: " + f'{ans2:.15f}' + "\n    в: " + f'{ans3:.15f}',
                      "Arial", 14,
                      align.LEFT,
                      False)
