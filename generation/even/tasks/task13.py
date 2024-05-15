import os
import random
from math import exp
from math import factorial

from docx.enum.text import WD_PARAGRAPH_ALIGNMENT as align

import generation.writer as writer

source_doc_path = os.path.dirname(os.path.abspath(__file__)) + "/texts/task_13.docx"

first_val = 4000
second_val = 0.0002


def generate_task(target_doc_path):
    global first_val
    global second_val

    first_val = random.randint(200,450) * 10
    second_val = round(random.uniform(0.0002,0.0020), 4)
    replacement_values = [first_val, second_val]

    writer.replace_placeholders_and_write_to_target(source_doc_path, target_doc_path, replacement_values, "*")


def calculate_task(target_doc_path):
    global first_val
    global second_val

    l = first_val * second_val
    x = [_ for _ in range(5)]
    p = [
        ((l ** i
          * exp(-l))
         / factorial(i))
        for i in range(5)
    ]

    ans = "13. xi " + " " * 8
    for i in range(5):
        ans += str(x[i]) + " " * 11
    ans += "\n" + " " * 7 + "pi  "
    for i in range(5):
        ans += str(f'{p[i]:.3f}') + " " * 2

    mx = l
    ans += "\n" + " " * 4 + "M(X) = " + str(round(mx, 4))
    writer.write_text(target_doc_path,
                      ans,
                      "Arial", 14,
                      align.LEFT,
                      False)