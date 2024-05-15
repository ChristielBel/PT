import os
import random
import sympy as sy

from docx.enum.text import WD_PARAGRAPH_ALIGNMENT as align
from sympy import symbols
from math import pi
from sympy import sqrt

import generation.writer as writer

source_doc_path = os.path.dirname(os.path.abspath(__file__)) + "/texts/task19.docx"

a = pi / 2
k = 1
b = -sqrt(2) / 2
c = sqrt(2) / 2


def generate_task(target_doc_path):
    global a
    global k

    k = random.randint(1, 20)
    a = a * k
    replacement_values = [k]

    writer.replace_placeholders_and_write_to_target(source_doc_path, target_doc_path, replacement_values, "!")


def calculate_task(target_doc_path):
    global a
    global b

    x = symbols('x')
    f1 = sy.simplify(sy.integrate(k / (a * sqrt(1 - x ** 2)), (x, b, x)))

    f = ("F(X) = 0, x <= " + str(b) + "\n"
         "      F(X) = " + str(f1) + ", " + str(b) + " < x <= " + str(c) + "\n"
         "      F(X)=  1, x > " + str(c) + "\n")

    ans = "19. "
    ans += f

    writer.write_text(target_doc_path,
                      ans,
                      "Arial", 14,
                      align.LEFT,
                      False)