import os
import random
from scipy.special import erf

from docx.enum.text import WD_PARAGRAPH_ALIGNMENT as align

import generation.writer as writer

source_doc_path = os.path.dirname(os.path.abspath(__file__)) + "/texts/task_17.docx"

mx = 100
a = 15
b = 75


def generate_task(target_doc_path):
    global mx
    global a
    global b

    mx = random.randint(100, 120)
    a = random.randint(10, 20)
    b = random.randint(65, 80)

    replacement_values = [mx, a, b]

    writer.replace_placeholders_and_write_to_target(source_doc_path, target_doc_path, replacement_values, "*")


def calculate_task(target_doc_path):
    global mx
    global a
    global b

    x1 = (b - mx) / a
    x2 = (0 - mx) / a
    P = laplace_func(x1) - laplace_func(x2)

    ans = "17. "
    ans += "P(T<" + str(b) + ") = " + "{:.10f}".format(P)

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