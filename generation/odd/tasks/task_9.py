import math
import os
import random

from docx.enum.text import WD_PARAGRAPH_ALIGNMENT as align
from scipy.special import erf

import generation.writer as writer

source_doc_path = os.path.dirname(os.path.abspath(__file__)) + "/texts/task9.docx"
first_val = 100
second_val = 0.92
third_val = 10


def generate_task(target_doc_path):
    global first_val
    global second_val
    global third_val

    first_val = random.randint(7, 13) * 10
    second_val = round(random.uniform(0.9, 0.95), 2)
    third_val = random.randint(1, 3) * 5

    replacement_values = [first_val, second_val, third_val]

    writer.replace_placeholders_and_write_to_target(source_doc_path, target_doc_path, replacement_values)


def calculate_task(target_doc_path):
    global first_val
    global second_val
    global third_val

    p = second_val
    q = 1 - second_val
    x1 = (0 - first_val * q) / math.sqrt(first_val * p * q)
    x2 = (first_val / 2 - first_val * q) / math.sqrt(first_val * p * q)

    x = round((third_val - first_val * q) / math.sqrt(first_val * p * q), 2)

    ans1 = laplace_func(x2) - laplace_func(x1)
    ans2 = phi(x)

    writer.write_text(target_doc_path,
                      "9. а: " + f'{ans1:.4f}' + "\n    б: " + f'{ans2:.4f}',
                      "Arial", 14,
                      align.LEFT,
                      False)


def laplace_func(x):
    return erf(x / 2 ** 0.5) / 2


def phi(x):
    if x >= 4:
        return 0
    return 1 / math.sqrt(2 * math.pi) * math.exp(-x ** 2 / 2)
