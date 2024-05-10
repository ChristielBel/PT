import math
import os
import random

from docx.enum.text import WD_PARAGRAPH_ALIGNMENT as align

import generation.writer as writer

source_doc_path = os.path.dirname(os.path.abspath(__file__)) + "/texts/task13.docx"
n = 800
p = 0.004


def generate_task(target_doc_path):
    global p
    global n

    p = round(random.uniform(0.001, 0.005), 3)
    n = random.randint(7, 9) * 100

    replacement_values = [n, p]

    writer.replace_placeholders_and_write_to_target(source_doc_path, target_doc_path, replacement_values)


def calculate_task(target_doc_path):
    global p
    global n

    np = n * p
    x = [_ for _ in range(5)]
    p = [
        ((np ** i
          * math.exp(-np))
         / math.factorial(i))
        for i in range(5)
    ]

    ans = "13.  xi" + " " * 8
    for i in range(5):
        ans += str(x[i]) + " " * 11
    ans += "\n" + " " * 7 + "pi  "
    for i in range(5):
        ans += str(f'{p[i]:.4f}') + " " * 2

    mx = np
    ans += "\n" + " " * 4 + "M(X) = " + str(round(mx, 4))

    writer.write_text(target_doc_path,
                      ans,
                      "Arial", 14,
                      align.LEFT,
                      False)
