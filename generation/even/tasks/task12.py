import os
import random
from math import comb

from docx.enum.text import WD_PARAGRAPH_ALIGNMENT as align

import generation.writer as writer

source_doc_path = os.path.dirname(os.path.abspath(__file__)) + "/texts/task_12.docx"

val = 5
first_val = 4


def generate_task(target_doc_path):
    global first_val
    global val

    first_val = random.randint(3, 10)
    val = random.randint(1, 6)

    replacement_values = [val, first_val]

    writer.replace_placeholders_and_write_to_target(source_doc_path, target_doc_path, replacement_values, "*")


def calculate_task(target_doc_path):
    global first_val

    n = first_val + 1

    x = [0] * n
    p = [0] * n

    for i in range(first_val):
        x[i] = i
        p[i] = P(first_val, i)

    x[first_val] = first_val
    p[first_val] = P(first_val, first_val)

    ans = "12. xi " + " " * 8
    for i in range(n):
        ans += str(x[i]) + " " * 11
    ans += "\n" + " " * 7 + "pi  "
    for i in range(n):
        ans += str(f'{p[i]:.3f}') + " " * 2

    writer.write_text(target_doc_path,
                      ans,
                      "Arial", 14,
                      align.LEFT,
                      False)


def P(n, k):
    return comb(n, k) * ((1 / 6) ** k) * ((5 / 6) ** (n - k))