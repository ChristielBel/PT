import math
import os
import random

from docx.enum.text import WD_PARAGRAPH_ALIGNMENT as align
from scipy import integrate

import generation.writer as writer

source_doc_path = os.path.dirname(os.path.abspath(__file__)) + "/texts/task20.docx"
first_val = 3/32
second_val = 0.0625
alpha = -3
beta = 3

def generate_task(target_doc_path):
    global first_val
    global second_val
    global alpha
    global beta

    coef = random.randint(1, 5)
    first_val = 0.5 * coef
    second_val = 0.0625 * coef
    alpha = -0.5 * random.randint(1, 3)
    beta = 0.5 * random.randint(1, 5)

    replacement_values = [coef, coef, alpha, beta]

    writer.replace_placeholders_and_write_to_target(source_doc_path, target_doc_path, replacement_values, "`")


def calculate_task(target_doc_path):
    global first_val
    global second_val
    global alpha
    global beta

    fst_cf = first_val * 2
    sc_cf = second_val * 4

    f = ("f(x) = 0, x≤0\n"
         "          f(x) = " + str(fst_cf) + "*x - " + str(sc_cf) + "*x^3, 0<x≤2\n"
                                                                    "          f(x) = 0, x>4\n")

    ans = "20. 1) " + f

    mx = integrate.quad(mx_func, 0.0, 2.0, args=(fst_cf, sc_cf))[0]
    mx2 = integrate.quad(mx2_func, 0.0, 2.0, args=(fst_cf, sc_cf))[0]
    dx = mx2 - mx ** 2

    ans += "      3) "
    ans += "M(X) = " + str(round(mx, 4))
    ans += "\n" + " " * 10 + "D(X) = " + str(round(dx, 4))
    ans += "\n" + " " * 10 + "σ(X) = sqrt(" + str(round(dx, 4)) + ")"

    p = func(beta, first_val, second_val) - func(alpha, first_val, second_val)

    ans += "\n      4) " + str(round(p, 4))

    writer.write_text(target_doc_path,
                      ans,
                      "Arial", 14,
                      align.LEFT,
                      False)


def func(x, fst_cf, sc_cf):
    return fst_cf * x ** 2 - sc_cf * x ** 4


def mx_func(x, fst_cf, sc_cf):
    return fst_cf * x ** 2 - sc_cf * x ** 4


def mx2_func(x, fst_cf, sc_cf):
    return fst_cf * x ** 3 - sc_cf * x ** 5
