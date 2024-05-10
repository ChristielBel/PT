import math
import os
import random

from docx.enum.text import WD_PARAGRAPH_ALIGNMENT as align

import generation.writer as writer

source_doc_path = os.path.dirname(os.path.abspath(__file__)) + "/texts/task2.docx"
first_val = 3/8
second_val = 2/8
third_val = 3/8
sum_val = first_val + second_val + third_val


def generate_task(target_doc_path):
    global first_val
    global second_val
    global third_val
    global sum_val

    first_val = random.randint(2, 6)
    second_val = random.randint(2, 6)
    third_val = random.randint(2, 6)

    replacement_values = [first_val, second_val, third_val]

    writer.replace_placeholders_and_write_to_target(source_doc_path, target_doc_path, replacement_values)


def calculate_task(target_doc_path):
    global first_val
    global second_val
    global third_val
    global sum_val

    sum_val = first_val + second_val + third_val
    first_val /= sum_val
    second_val /= sum_val
    third_val /= sum_val

    ans1 = math.pow(first_val, 3)
    ans2 = 3 * first_val * second_val * third_val

    writer.write_text(target_doc_path,
                      "2. а: " + f'{ans1:.5f}' + "\n    б: " + f'{ans2:.5f}',
                      "Arial", 14,
                      align.LEFT,
                      False)
