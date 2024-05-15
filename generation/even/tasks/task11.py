import os
import random
from math import sqrt

from docx.enum.text import WD_PARAGRAPH_ALIGNMENT as align

import generation.writer as writer

source_doc_path = os.path.dirname(os.path.abspath(__file__)) + "/texts/task_11.docx"

p1 = 0.3
p2 = 0.7


def generate_task(target_doc_path):
    global p1
    global p2

    p1 = round(random.uniform(0.25, 0.4), 2)
    p2 = round(random.uniform(0.65, 0.8), 2)
    replacement_values = [p1, p2]

    writer.replace_placeholders_and_write_to_target(source_doc_path, target_doc_path, replacement_values, "*")


def calculate_task(target_doc_path):
    global p1
    global p2

    q1 = 1 - p1
    q2 = 1 - p2

    x = [1, 2, 3, 4, 5]
    p0 = p1 + p2 * q1
    pp = q1 * q2
    p = [p0, pp * p0, (pp ** 2) * p0, (pp ** 3) * p0, (pp ** 4) * p0]

    ans = "11.  xi" + " " * 8
    for i in range(5):
        ans += str(x[i]) + " " * 11
    ans += "\n" + " " * 7 + "pi  "
    for i in range(5):
        ans += str(f'{p[i]:.3f}') + " " * 2

    mx = 0
    for i in range(5):
        mx += x[i] * p[i]

    mx_2 = 0
    for i in range(5):
        mx_2 += x[i] ** 2 * p[i]

    dx = mx_2 - mx ** 2

    sigma = sqrt(dx)

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