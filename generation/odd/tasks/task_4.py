import math
import os
import random

from docx.enum.text import WD_PARAGRAPH_ALIGNMENT as align

import generation.writer as writer

source_doc_path = os.path.dirname(os.path.abspath(__file__)) + "/texts/task4.docx"
first_val = 0.6
second_val = 0.8


def generate_task(target_doc_path):
    global first_val
    global second_val

    first_val = round(random.uniform(0.4, 0.9), 2)
    second_val = round(random.uniform(0.4, 0.9), 2)

    replacement_values = [first_val, second_val]

    writer.replace_placeholders_and_write_to_target(source_doc_path, target_doc_path, replacement_values, "+")


def calculate_task(target_doc_path):
    global first_val
    global second_val

    ans = math.pow(first_val, 2) * second_val + math.pow(first_val, 3)

    writer.write_text(target_doc_path,
                      "4. " + f'{ans:.5f}',
                      "Arial", 14,
                      align.LEFT,
                      False)
