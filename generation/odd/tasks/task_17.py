import os
import random

from docx.enum.text import WD_PARAGRAPH_ALIGNMENT as align
from scipy.special import erf

import generation.writer as writer

source_doc_path = os.path.dirname(os.path.abspath(__file__)) + "/texts/task15.docx"
m = 200
sigma = 30
beta = 180


def generate_task(target_doc_path):
    global m
    global sigma
    global beta

    m = random.randint(19, 21) * 10
    sigma = random.randint(2, 4) * 10
    beta = random.randint(16, 18) * 10

    replacement_values = [m, sigma, beta]

    writer.replace_placeholders_and_write_to_target(source_doc_path, target_doc_path, replacement_values, "`")


def calculate_task(target_doc_path):
    global m
    global sigma
    global beta

    x1 = -m / sigma
    x2 = (beta - m) / sigma

    ans = laplace_func(x2) - laplace_func(x1)

    writer.write_text(target_doc_path,
                      "17. " + f'{ans:.5f}',
                      "Arial", 14,
                      align.LEFT,
                      False)


def laplace_func(x):
    return erf(x / 2 ** 0.5) / 2
