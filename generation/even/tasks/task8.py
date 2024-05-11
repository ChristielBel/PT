import os
import random
from math import comb

from docx.enum.text import WD_PARAGRAPH_ALIGNMENT as align

import generation.writer as writer

source_doc_path = os.path.dirname(os.path.abspath(__file__)) + "/texts/task_8.docx"

first_val = 5
second_val = 15


def generate_task(target_doc_path):
    global first_val
    global second_val

    first_val = random.randint(5,10)
    second_val = random.randint(15,25)

    replacement_values = [first_val, second_val]

    writer.replace_placeholders_and_write_to_target(source_doc_path, target_doc_path, replacement_values, "*")


def calculate_task(target_doc_path):
    global first_val
    global second_val


    ans1 = comb(4,2)*((first_val/(first_val+second_val))**2)*((second_val/(first_val+second_val))**2)

    writer.write_text(target_doc_path,
                  "8. " + f'{ans1:.15f}',
                  "Arial", 14,
                  align.LEFT,
                  False)
