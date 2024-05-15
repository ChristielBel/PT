import os
import random
from math import sqrt
from math import pi
from math import exp
from scipy.special import erf

from docx.enum.text import WD_PARAGRAPH_ALIGNMENT as align

import generation.writer as writer

source_doc_path = os.path.dirname(os.path.abspath(__file__)) + "/texts/task_9.docx"

val = 50


def generate_task(target_doc_path):
    global val

    val = random.randint(30, 100)
    replacement_values = [val]

    writer.replace_placeholders_and_write_to_target(source_doc_path, target_doc_path, replacement_values, "*")


def calculate_task(target_doc_path):
    global val

    l: float = sqrt(val * (4 / 36) * (32 / 36))
    x: float = (10 - val * (4 / 36)) / l
    ans1 = phi(x) * (1 / l)
    x2: float = (val - val * (4 / 36)) / l
    ans2 = laplace_func(x2) - laplace_func(x)

    writer.write_text(target_doc_path,
                      "9. а: " + f'{ans1:.6f}' + "\n    б: " + f'{ans2:.6f}',
                      "Arial", 14,
                      align.LEFT,
                      False)


def laplace_func(x):
    if x >= 5:
        return 0.5
    return erf(x / 2 ** 0.5) / 2

def phi(x):
    if x >= 4:
        return 0
    return 1 / sqrt(2 * pi) * exp(-x ** 2 / 2)