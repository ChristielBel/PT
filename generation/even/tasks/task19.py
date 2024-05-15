import os
import random
import sympy as sy

from docx.enum.text import WD_PARAGRAPH_ALIGNMENT as align
from sympy import symbols

import generation.writer as writer

source_doc_path = os.path.dirname(os.path.abspath(__file__)) + "/texts/task_19.docx"

a = 3
k = 1

def generate_task(target_doc_path):
    global a
    global k

    k = random.randint(1, 20)
    a = a * k
    replacement_values = [k]

    writer.replace_placeholders_and_write_to_target(source_doc_path, target_doc_path, replacement_values, "!")


def calculate_task(target_doc_path):
    global a

    x = symbols('x')
    f1 = sy.simplify(sy.integrate((k*a)/x**4, (x, 1, x)))

    f = ("F(X) = 0, x <= 1\n"
         "      F(X) = " + str(f1) + ", x > 1 \n")

    ans = "19. "
    ans += f

    writer.write_text(target_doc_path,
                      ans,
                      "Arial", 14,
                      align.LEFT,
                      False)