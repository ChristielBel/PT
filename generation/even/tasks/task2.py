import os
import random
from math import comb
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT as align

import generation.writer as writer

source_doc_path = os.path.dirname(os.path.abspath(__file__)) + "/texts/task_2.docx"

first_val = 20
second_val = 10
third_val = 6
fourth_val = 5


def generate_task(target_doc_path):
    global first_val
    global second_val
    global third_val
    global fourth_val

    first_val = random.randint(18, 30)
    second_val = random.randint(8, 20)
    third_val = random.randint(6, 10)
    fourth_val = random.randint(5, 8)

    if third_val == second_val or third_val == (second_val - 1):
        third_val -= 1

    replacement_values = [first_val, second_val, third_val, fourth_val]

    writer.replace_placeholders_and_write_to_target(source_doc_path, target_doc_path, replacement_values, "*")


def calculate_task(target_doc_path):
    global first_val
    global second_val
    global third_val
    global fourth_val

    ans1 = (comb(third_val, 3) * comb(first_val - third_val, 2)) / comb(first_val, 5)
    ans2 = (comb(second_val, 2) * comb(second_val - third_val, 2) * comb(third_val, 1)) / comb(first_val, 5)

    writer.write_text(target_doc_path,
                      "2. а: " + f'{ans1:.15f}' + "\n    б: " + f'{ans2:.15f}',
                      "Arial", 14,
                      align.LEFT,
                      False)
