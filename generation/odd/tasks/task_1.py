import os
import random
from math import factorial

from docx.enum.text import WD_PARAGRAPH_ALIGNMENT as align

import generation.writer as writer

source_doc_path = os.path.dirname(os.path.abspath(__file__)) + "/texts/task1.docx"
first_val = 20
second_val = 5


def generate_task(target_doc_path):
    global first_val
    global second_val

    first_val = random.randint(15, 30)
    second_val = random.randint(3, 9)
    replacement_values = [first_val, second_val]

    writer.replace_placeholders_and_write_to_target(source_doc_path, target_doc_path, replacement_values, "+")


def calculate_task(target_doc_path):
    global first_val
    global second_val

    ans1 = 1 / (factorial(first_val) / (factorial(first_val - second_val)))
    ans2 = 1.0 - ans1

    writer.write_text(target_doc_path,
                      "1. а: " + f'{ans1:.15f}' + "\n    б: " + f'{ans2:.15f}',
                      "Arial", 14,
                      align.LEFT,
                      False)
