import math
import os
import random

from docx.enum.text import WD_PARAGRAPH_ALIGNMENT as align

import generation.writer as writer

source_doc_path = os.path.dirname(os.path.abspath(__file__)) + "/texts/task8.docx"
first_val = 5
second_val = 2


def generate_task(target_doc_path):
    global first_val
    global second_val

    first_val = random.randint(3, 5)
    second_val = random.randint(1, first_val - 1)

    replacement_values = [first_val, second_val]

    writer.replace_placeholders_and_write_to_target(source_doc_path, target_doc_path, replacement_values, "+")


def calculate_task(target_doc_path):
    global first_val
    global second_val

    p = 1 / 216
    q = 215 / 216

    ans = (math.factorial(first_val)
           / (math.factorial(second_val)
              * math.factorial(first_val - second_val))
           * math.pow(p, second_val)
           * math.pow(q, first_val - second_val))

    writer.write_text(target_doc_path,
                      "8. " + f'{ans:.12f}',
                      "Arial", 14,
                      align.LEFT,
                      False)
