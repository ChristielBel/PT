import math
import os
import random

from docx.enum.text import WD_PARAGRAPH_ALIGNMENT as align

import generation.writer as writer

source_doc_path = os.path.dirname(os.path.abspath(__file__)) + "/texts/task11.docx"
p1 = 0.95
p2 = 0.9


def generate_task(target_doc_path):
    global p1
    global p2

    p1 = round(random.uniform(0.85, 0.95), 2)
    p2 = round(random.uniform(0.85, 0.95), 2)

    replacement_values = [p1, p2]

    writer.replace_placeholders_and_write_to_target(source_doc_path, target_doc_path, replacement_values, "+")


def calculate_task(target_doc_path):
    global p1
    global p2

    q1 = 1 - p1
    q2 = 1 - p2
    x = [0, 1, 2]
    p = [q1 * q2, p1 * q2 + p2 * q1, p1 * p2]

    ans = "11.  xi" + " " * 8
    for i in range(3):
        ans += str(x[i]) + " " * 11
    ans += "\n" + " " * 7 + "pi  "
    for i in range(3):
        ans += str(f'{p[i]:.4f}') + " " * 2

    mx = 0
    for i in range(3):
        mx += x[i] * p[i]

    mx2 = 0
    for i in range(3):
        mx2 += x[i] ** 2 * p[i]

    dx = mx2 - mx ** 2

    sigma = math.sqrt(dx)

    ans += "\n" + " " * 4 + "M(X) = " + str(round(mx, 4))
    ans += "\n" + " " * 4 + "D(X) = " + str(round(dx, 4))
    ans += "\n" + " " * 4 + "σ(X) = " + str(round(sigma, 4))

    f1 = p[0]
    f2 = f1 + p[1]

    f = ("    F(X) = 0, x <= 0\n"
         "    F(X) = " + str(round(f1, 4)) + ", 0 < x <= 1\n"
         "    F(X) = " + str(round(f2, 4)) + ", 1 < x <= 2\n"
         "    F(X)=  1, x > 2")

    ans += '\n' + f

    writer.write_text(target_doc_path,
                      ans,
                      "Arial", 14,
                      align.LEFT,
                      False)
