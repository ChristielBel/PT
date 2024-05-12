import os
import random

from docx.enum.text import WD_PARAGRAPH_ALIGNMENT as align
from scipy.special import erf

import generation.writer as writer

source_doc_path = os.path.dirname(os.path.abspath(__file__)) + "/texts/task16.docx"
m = 5
sigma = 0.05
alpha = 5.08


def generate_task(target_doc_path):
    global m
    global sigma
    global alpha

    m = random.randint(3, 6)
    sigma = round(random.uniform(0.04, 0.06), 2)
    alpha = m + 0.08

    replacement_values = [m, sigma, alpha]

    writer.replace_placeholders_and_write_to_target(source_doc_path, target_doc_path, replacement_values, "`")


def calculate_task(target_doc_path):
    global m
    global sigma
    global alpha

    x = round((alpha - m) / sigma, 2)

    ans = laplace_func(float('inf')) - laplace_func(x)

    writer.write_text(target_doc_path,
                      "16. " + f'{ans:.5f}',
                      "Arial", 14,
                      align.LEFT,
                      False)


def laplace_func(x):
    return erf(x / 2 ** 0.5) / 2
