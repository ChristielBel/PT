import os
import random
from scipy.special import erf

from docx.enum.text import WD_PARAGRAPH_ALIGNMENT as align

import generation.writer as writer

source_doc_path = os.path.dirname(os.path.abspath(__file__)) + "/texts/task_16.docx"

m = 100
m1 = 100
a = 94
b = 106
c = 104


def generate_task(target_doc_path):
    global m
    global m1
    global a
    global b
    global c

    m = random.randint(100, 120)
    m1 = m
    a = random.randint(90, 99)
    k = abs(m - a)
    b = k + a
    a1 = a + 2
    b1 = b - 2
    c = random.randint(a1, b1)
    replacement_values = [m, m1, a, b, c]

    writer.replace_placeholders_and_write_to_target(source_doc_path, target_doc_path, replacement_values, "*")


def calculate_task(target_doc_path):
    global m
    global a
    global b
    global c

    sigma = 1
    x2 = (b - m) / sigma
    x1 = (c - m) / sigma
    P = laplace_func(x2) - laplace_func(x1)

    ans = "16. "
    ans += "P(T>" + str(c) + ") = " + "{:.10f}".format(P)

    writer.write_text(target_doc_path,
                      ans,
                      "Arial", 14,
                      align.LEFT,
                      False)


def laplace_func(x):
    if x >= 5:
        return 0.5
    if x <= -5:
        return -0.5
    return erf(x / 2 ** 0.5) / 2
