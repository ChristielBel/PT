import os
import random

from docx.enum.text import WD_PARAGRAPH_ALIGNMENT as align

import generation.writer as writer

source_doc_path = os.path.dirname(os.path.abspath(__file__)) + "/texts/task14.docx"
x = {-5: 0.6, 1: 0.1, 2: 0.3}
y = {1: 0.3, 2: 0.7}


def generate_task(target_doc_path):
    global x
    global y

    x1 = random.randint(-5, -3)
    x2 = random.randint(1, 2)
    x3 = random.randint(x2 + 1, 4)
    px1 = round(random.uniform(0.1, 0.6), 1)
    px2 = round(random.uniform(0.1, 0.3), 1)
    px3 = round(1 - px1 - px2, 1)
    x = {x1: px1, x2: px2, x3: px3}

    y1 = random.randint(1, 2)
    y2 = random.randint(y1 + 1, 3)
    py1 = round(random.uniform(0.1, 0.6), 1)
    py2 = round(1 - py1, 1)
    y = {y1: py1, y2: py2}

    replacement_values = [x1, x2, x3, y1, y2, px1, px2, py1, py2]

    writer.replace_placeholders_and_write_to_target(source_doc_path, target_doc_path, replacement_values, "`")


def calculate_task(target_doc_path):
    global x
    global y

    ans = "14. 1) "

    mx = 0
    for i in x.keys():
        mx += i * x[i]

    my = 0
    for i in y.keys():
        my += i * y[i]

    mx2 = 0
    for i in x.keys():
        mx2 += i ** 2 * x[i]

    my2 = 0
    for i in y.keys():
        my2 += i ** 2 * y[i]

    dx = mx2 - mx ** 2
    dy = my2 - my ** 2

    ans += "M(X) = " + str(round(mx, 4))
    ans += "\n" + " " * 11 + "M(Y) = " + str(round(my, 4))
    ans += "\n" + " " * 11 + "D(X) = " + str(round(dx, 4))
    ans += "\n" + " " * 11 + "D(Y) = " + str(round(dy, 4))

    z1 = {}
    for i in x.keys():
        for j in y.keys():
            new_key = 2 * i + j
            z1[new_key] = round(z1.get(new_key, 0) + x[i] * y[j], 2)

    z2 = {}
    for i in x.keys():
        for j in y.keys():
            new_key = i * j
            z2[new_key] = round(z2.get(new_key, 0) + x[i] * y[j], 2)

    ans += "\n" + " " * 6 + "2)  z1i" + " " * 4
    for i in z1.keys():
        ans += str(i) + " " * 6
    ans += "\n" + " " * 13 + "pi  "
    for i in z1.values():
        ans += str(f'{i:.2f}') + " " * 2

    ans += "\n" + " " * 7 + "    z2i" + " " * 4
    for i in z2.keys():
        ans += str(i) + " " * 6
    ans += "\n" + " " * 13 + "pi  "
    for i in z2.values():
        ans += str(f'{i:.2f}') + " " * 2

    mz1 = 2 * mx + my
    mz2 = mx * my
    dz1 = 4 * dx + dy
    dz2 = mx2 * my2 - mx ** 2 * my ** 2

    ans += "\n" + " " * 6 + "3) M(Z1) = " + str(round(mz1, 4))
    ans += "\n" + " " * 10 + "M(Z2) = " + str(round(mz2, 4))
    ans += "\n" + " " * 10 + "D(Z1) = " + str(round(dz1, 4))
    ans += "\n" + " " * 10 + "D(Z2) = " + str(round(dz2, 4))

    writer.write_text(target_doc_path,
                      ans,
                      "Arial", 14,
                      align.LEFT,
                      False)
