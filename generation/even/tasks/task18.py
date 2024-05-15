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
c = 4
alpha = -pi / 2
beta = -pi / 6


def generate_task(target_doc_path):
    global a
    global b
    global c
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

    alpha /= a
    beta /= a

    replacement_values = [round(b,4), a, round(b,4), round(c,4), round(c,4), round(alpha,4), round(beta,4)]

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

    f = ("f(X) = 0, x <= " + str(b) + "\n"
         "      f(X) = " + str(yy) + ", " + str(b) + " < x <= " + str(c) + "\n"
         "      f(X) =  0, x > " + str(c))

    mx = sy.integrate(x * yy, (x, 0, b))
    mx2 = sy.integrate(yy * x * x, (x, 0, b))
    dx = mx2 - mx ** 2
    sigma = sy.sqrt(dx)
    p = func(a,beta) - func(a, alpha)

    ans = "18. "
    ans += f
    ans += "\n" + " " * 6 + "M(X) = " + str(round(mx, 4))
    ans += "\n" + " " * 6 + "D(X) = " + str(round(dx, 4))
    ans += "\n" + " " * 6 + "σ(X) = " + str(round(sigma, 4))
    ans += "\n" + " " * 6 + "P(" + str(round(alpha, 4)) + " < " + "X < " + str(round(beta, 4)) + ") = " + str(round(p, 4))

    writer.write_text(target_doc_path,
                      ans,
                      "Arial", 14,
                      align.LEFT,
                      False)


def func(k, x):
    return k * x/2 - 1
