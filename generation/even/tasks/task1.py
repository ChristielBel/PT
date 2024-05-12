import os
import random
from math import factorial

from docx.enum.text import WD_PARAGRAPH_ALIGNMENT as align

import generation.writer as writer

source_doc_path = os.path.dirname(os.path.abspath(__file__)) + "/texts/task_1.docx"

val = 6


def generate_task(target_doc_path):
    global val

    val = random.randint(3, 10)
    replacement_values = [val]

    writer.replace_placeholders_and_write_to_target(source_doc_path, target_doc_path, replacement_values, "*")


def calculate_task(target_doc_path):
    global val

    ans1 = 1 / (factorial(val))
    ans2 = (factorial(val - 2)) / (factorial(val))

    writer.write_text(target_doc_path,
                      "1. а: " + f'{ans1:.3f}' + "\n    б: " + f'{ans2:.3f}',
                      "Arial", 14,
                      align.LEFT,
                      False)
