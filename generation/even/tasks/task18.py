import os
import random
import sympy as sy

from docx.enum.text import WD_PARAGRAPH_ALIGNMENT as align
from scipy.special import erf
from sympy import symbols
from math import pi

import generation.writer as writer

source_doc_path = os.path.dirname(os.path.abspath(__file__)) + "/texts/task_18.docx"

a = 1
b = 2
b2 = 2
c = 4
c2 = 4
alpha = -pi / 2
beta = -pi / 6


def generate_task(target_doc_path):
    global a
    global b
    global b2
    global c
    global c2
    global alpha
    global beta

    a = random.randint(1, 20)
    x = symbols('x')
    equation1 = a * x / 2 - 1
    solutions = sy.solve(equation1, x)
    b = solutions[0]

    equation2 = a * x / 2 - 1 - 1
    solutions = sy.solve(equation2, x)
    c = solutions[0]

    b2 = b
    c2 = c
    alpha /= a
    beta /= a

    replacement_values = [b, a, b2, c, c2, alpha, beta]

    writer.replace_placeholders_and_write_to_target(source_doc_path, target_doc_path, replacement_values, "!")


def calculate_task(target_doc_path):
    global a
    global b
    global c
    global alpha
    global beta

    x = symbols('x')
    y = a * ((x ** 2) / 2) * (1 - (x ** 2) / 8)
    yy = sy.simplify(y.diff(x))

    f = ("    f(X) = 0, x <= " + str(b) + "\n"
         "    f(X) = " + str(yy) + ", " + str(b) + " < x <=" + str(c) + "\n"
         "    f(X)=  0, x > " + str(c))

    mx = sy.integrate(x * yy, (x, 0, b))
    mx2 = sy.integrate(yy * x * x, (x, 0, b))
    dx = mx2 - mx ** 2
    sigma = sy.sqrt(dx)
    p = func(a,beta) - func(a, alpha)

    ans = "18. "
    ans += f + "\n"
    ans += str(mx) + "\n"
    ans += str(mx2) + "\n"
    ans += str(dx) + "\n"
    ans += str(sigma) + "\n"
    ans += str(p) + "\n"

    writer.write_text(target_doc_path,
                      ans,
                      "Arial", 14,
                      align.LEFT,
                      False)


def func(k, x):
    return k * x/2 - 1
