import os
import random
from math import factorial

from docx.enum.text import WD_PARAGRAPH_ALIGNMENT as align

import generation.writer as writer

source_doc_path = os.path.dirname(os.path.abspath(__file__)) + "/texts/task_7.docx"

first_val = 50
second_val = 30
third_val = 20
fourth_val = 0.5
fifth_val = 0.6
sixth_val = 0.4


def generate_task(target_doc_path):
    global first_val
    global second_val
    global third_val
    global fourth_val
    global fifth_val
    global sixth_val

    fourth_val = round(random.uniform(0.5, 0.9), 2)
    fifth_val = round(random.uniform(0.6, 0.9), 2)
    sixth_val = round(random.uniform(0.4, 0.9), 2)

    replacement_values = [first_val, second_val, third_val, fourth_val, fifth_val, sixth_val]

    writer.replace_placeholders_and_write_to_target(source_doc_path, target_doc_path, replacement_values, "*")


def calculate_task(target_doc_path):
    global first_val
    global second_val
    global third_val
    global fourth_val
    global fifth_val
    global sixth_val

    ans1 = (first_val / 100) * fourth_val + (second_val / 100) * fifth_val + (third_val / 100) * sixth_val
    h1 = ((first_val / 100) * fourth_val) / ans1
    h2 = ((second_val / 100) * fifth_val) / ans1
    h3 = ((third_val / 100) * sixth_val) / ans1

    if h1 > h2 and h1 > h3:
        ans2 = h1
        ans3 = "из цемента"
    elif h2 > h3 and h2 > h1:
        ans2 = h2
        ans3 = "из амальгамы"
    elif h3 > h1 and h3 > h2:
        ans2 = h3
        ans3 = "из пластмассы"

    writer.write_text(target_doc_path,
                      "7. P(A)=" + f'{ans1:.15f}' + "\n" + f'{ans2:.15f}' + "\n" +ans3,
                      "Arial", 14,
                      align.LEFT,
                      False)
