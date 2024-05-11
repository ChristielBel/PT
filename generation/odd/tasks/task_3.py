import os
import random

from docx.enum.text import WD_PARAGRAPH_ALIGNMENT as align

import generation.writer as writer

source_doc_path = os.path.dirname(os.path.abspath(__file__)) + "/texts/task3.docx"

first_val = 0.8
second_val = 0.95


def generate_task(target_doc_path):
    global first_val
    global second_val

    first_val = round(random.uniform(0.6, 0.95), 2)
    second_val = round(random.uniform(0.6, 0.95), 2)

    replacement_values = [first_val, second_val]

    writer.replace_placeholders_and_write_to_target(source_doc_path, target_doc_path, replacement_values, "+")


def calculate_task(target_doc_path):
    global first_val
    global second_val

    first_val_neg = 1.0 - first_val
    second_val_neg = 1.0 - second_val
    ans1 = first_val * second_val_neg + first_val_neg * second_val
    ans2 = 1.0 - first_val_neg * second_val_neg
    ans3 = first_val * second_val

    writer.write_text(target_doc_path,
                      "3. а: " + f'{ans1:.5f}' + "\n    б: " + f'{ans2:.5f}' + "\n    в: " + f'{ans3:.5f}',
                      "Arial", 14,
                      align.LEFT,
                      False)
