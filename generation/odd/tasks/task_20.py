import math
import os
import random
import sympy as sy

from docx.enum.text import WD_PARAGRAPH_ALIGNMENT as align
from sympy import symbols, Eq, solve

import generation.writer as writer

source_doc_path = os.path.dirname(os.path.abspath(__file__)) + "/texts/task20.docx"
first_val = 3/32
a = -2
b = 2
c = 4
alpha = -3
beta = 3

def generate_task(target_doc_path):
    global first_val
    global a
    global b
    global c
    global alpha
    global beta

    a = random.randint(-10, -1)
    b = random.randint(0, 4)
    c = random.randint(5, 10)

    x = symbols('x')
    y = symbols('y')
    equation = (sy.integrate(y*(x+2), (x, a, b)) + sy.integrate(y*(x-4)**2, (x, b, c))) - 1
    val = sy.solve(equation, y)
    first_val = val[0]

    alpha = a-1
    beta = random.randint(a+1,c)

    formula = "∫_{-∞}^{+∞} f(x)dx = 1"
    replacement_values = [formula,a, first_val,a,b,first_val,b,c,c,alpha,beta]

    writer.replace_placeholders_and_write_to_target(source_doc_path, target_doc_path, replacement_values, "!")


def calculate_task(target_doc_path):
    global first_val
    global a
    global b
    global c
    global alpha
    global beta

    x = symbols('x')
    y1 = first_val * (x+2)
    y2 = first_val*(x-4)**2
    f1 = sy.simplify(sy.integrate(y1, (x, a, x)))
    f2 = sy.simplify(sy.integrate(y1, (x, a, b)) + sy.integrate(y2, (x, b, x)))

    f = ("F(x) = 0, x ≤ "+str(a)+"\n"
         "      F(x) = " + str(f1) + ", " + str(a) + " < x ≤ " + str(b) + "\n"
         "      F(x) = " + str(f2) + ", " + str(b) + " < x ≤ " + str(c) + "\n"
         "      F(x) = 1, x > " + str(c) + "\n"
         )

    ans = "20. "

    mx = sy.integrate(x * first_val * (x+2), (x, a, b)) + sy.integrate(x * first_val * (x-4)**2, (x, b, c))
    mx2 = sy.integrate(first_val * (x+2) * x * x, (x, a, b)) + sy.integrate(x * x * first_val * (x-4)**2, (x, b, c))
    dx = mx2 - mx ** 2
    sigma = sy.sqrt(dx)

    if (a > alpha):
        e1 = 0
    elif (a < alpha < b):
        e1 = f1.subs(x, alpha)
    elif (b < alpha < c):
        e1 = f2.subs(x, alpha)
    else:
        e1 = 1

    if (a > beta):
        e2 = 0
    elif (a < beta < b):
        e2 = f1.subs(x, beta)
    elif (b < beta < c):
        e2 = f2.subs(x, beta)
    else:
        e2 = 1
    p = e2 - e1

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