import os
import random
from math import sqrt
from math import pi
from math import exp
from scipy.special import erf

from docx.enum.text import WD_PARAGRAPH_ALIGNMENT as align

import generation.writer as writer

source_doc_path = os.path.dirname(os.path.abspath(__file__)) + "/texts/task_10.docx"

first_val = 0.005
second_val = 200


def generate_task(target_doc_path):
    global first_val
    global second_val

    first_val = round(random.uniform(0.005, 0.09), 3)
    second_val = random.randint(20, 60) * 5
    replacement_values = [first_val, second_val]

    writer.replace_placeholders_and_write_to_target(source_doc_path, target_doc_path, replacement_values, "*")


def calculate_task(target_doc_path):
    global first_val
    global second_val

    l: float = sqrt(second_val * first_val * (1 - first_val))
    x1: float = (0 - second_val * first_val) / l
    x2: float = (3 - second_val * first_val) / l
    ans = laplace_func(x2) - laplace_func(x1)

    writer.write_text(target_doc_path,
                      "10. " + f'{ans:.3f}',
                      "Arial", 14,
                      align.LEFT,
                      False)


def laplace_func(x):
    return erf(x / 2 ** 0.5) / 2
