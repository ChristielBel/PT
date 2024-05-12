import os
import random
from math import factorial

from docx.enum.text import WD_PARAGRAPH_ALIGNMENT as align

import generation.writer as writer

source_doc_path = os.path.dirname(os.path.abspath(__file__)) + "/texts/task_5.docx"

first_val = 4
second_val = 5
third_val = 2


def generate_task(target_doc_path):
    global first_val
    global second_val
    global third_val

    first_val = random.randint(4, 12)
    second_val = random.randint(5, 12)
    third_val = random.randint(2, 4)

    replacement_values = [first_val, second_val, third_val]

    writer.replace_placeholders_and_write_to_target(source_doc_path, target_doc_path, replacement_values, "*")


def calculate_task(target_doc_path):
    global first_val
    global second_val
    global third_val

    ans = (factorial(first_val) / (factorial(first_val - third_val) * factorial(third_val))) / (
            factorial(first_val + second_val) / (
            factorial(first_val + second_val - third_val) * factorial(third_val)))

    writer.write_text(target_doc_path,
                      "5. " + f'{ans:.3f}',
                      "Arial", 14,
                      align.LEFT,
                      False)
