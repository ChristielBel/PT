import math
import os
import random

from docx.enum.text import WD_PARAGRAPH_ALIGNMENT as align

import generation.writer as writer

source_doc_path = os.path.dirname(os.path.abspath(__file__)) + "/texts/task12.docx"
p = 0.51
k = 4


def generate_task(target_doc_path):
    global p
    global k

    p = round(random.uniform(0.45, 0.55), 2)
    k = random.randint(3, 5)

    replacement_values = [p, k]

    writer.replace_placeholders_and_write_to_target(source_doc_path, target_doc_path, replacement_values)


def calculate_task(target_doc_path):
    global p
    global k

    q = 1 - p

    x = [_ for _ in range(k + 1)]
    p = [
        math.factorial(k)
        / (math.factorial(i)
           * math.factorial(k - i))
        * q ** i * p ** (k - i)
        for i in range(k + 1)
    ]

    ans = "12.  xi" + " " * 8
    for i in range(k + 1):
        ans += str(x[i]) + " " * 11
    ans += "\n" + " " * 7 + "pi  "
    for i in range(k + 1):
        ans += str(f'{p[i]:.4f}') + " " * 2

    mx = 0
    for i in range(k + 1):
        mx += x[i] * p[i]

    mx2 = 0
    for i in range(k + 1):
        mx2 += x[i] ** 2 * p[i]

    dx = mx2 - mx ** 2

    ans += "\n" + " " * 4 + "M(X) = " + str(round(mx, 4))
    ans += "\n" + " " * 4 + "D(X) = " + str(round(dx, 4))

    writer.write_text(target_doc_path,
                      ans,
                      "Arial", 14,
                      align.LEFT,
                      False)
