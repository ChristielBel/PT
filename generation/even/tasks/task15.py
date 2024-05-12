import os
import random

from docx.enum.text import WD_PARAGRAPH_ALIGNMENT as align

import generation.writer as writer

source_doc_path = os.path.dirname(os.path.abspath(__file__)) + "/texts/task_15.docx"

first_val = 0.001
second_val = 50


def generate_task(target_doc_path):
    global first_val
    global second_val

    replacement_values = [first_val, second_val]

    writer.replace_placeholders_and_write_to_target(source_doc_path, target_doc_path, replacement_values, "*")


def calculate_task(target_doc_path):
    global first_val
    global second_val

    f = (" F(X) = 0, x <= 0\n"
         "      F(X) = " + str(round(first_val, 4)) + "*e^(-x*" + str(round(first_val, 4)) + ")" + ", 0 < x <= 1\n")

    mx = 1 / first_val

    ans = "15."
    ans += f
    ans += " " * 6 + "M(X) = " + str(round(mx, 4))

    writer.write_text(target_doc_path,
                      ans,
                      "Arial", 14,
                      align.LEFT,
                      False)
