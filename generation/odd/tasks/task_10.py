import math
import os
import random

from docx.enum.text import WD_PARAGRAPH_ALIGNMENT as align

import generation.writer as writer

source_doc_path = os.path.dirname(os.path.abspath(__file__)) + "/texts/task10.docx"
p = 0.001
n = 1000
k = 10


def generate_task(target_doc_path):
    global n
    global p
    global k

    n = round(random.uniform(0.001, 0.005), 3)
    p = random.randint(1, 3) * 1000
    k = random.randint(1, 3) * 5

    replacement_values = [p, n, k]

    writer.replace_placeholders_and_write_to_target(source_doc_path, target_doc_path, replacement_values)


def calculate_task(target_doc_path):
    global n
    global p
    global k

    np = n * p

    ans = (np ** k * math.exp(-np)) / math.factorial(k)

    writer.write_text(target_doc_path,
                      "10. " + f'{ans:.12f}',
                      "Arial", 14,
                      align.LEFT,
                      False)
