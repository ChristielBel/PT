import os
import random

from docx.enum.text import WD_PARAGRAPH_ALIGNMENT as align

import generation.writer as writer

source_doc_path = os.path.dirname(os.path.abspath(__file__)) + "/texts/task7.docx"
first_val = 30
second_val = 50
third_val = 100 - first_val + second_val
first_p = 0.5
second_p = 0.7
third_p = 0.6


def generate_task(target_doc_path):
    global first_val
    global second_val
    global third_val
    global first_p
    global second_p
    global third_p

    first_val = random.randint(1, 4)
    second_val = random.randint(3, 8 - first_val)
    first_val *= 10
    second_val *= 10
    third_val = 100 - first_val - second_val
    first_p = round(random.uniform(0.4, 0.8), 1)
    second_p = round(random.uniform(0.4, 0.8), 1)
    third_p = round(random.uniform(0.4, 0.8), 1)

    replacement_values = [first_val, second_val, first_p, second_p, third_p]

    writer.replace_placeholders_and_write_to_target(source_doc_path, target_doc_path, replacement_values)


def calculate_task(target_doc_path):
    global first_val
    global second_val
    global third_val
    global first_p
    global second_p
    global third_p

    s = first_val + second_val + third_val
    ph1 = first_val / s
    ph2 = third_val / s
    ph3 = third_val / s

    cashew = ph1 * first_p
    farming = ph2 * second_p
    cane = ph3 * third_p

    total_prob = cashew + farming + cane

    cashew /= total_prob
    farming /= total_prob
    cane /= total_prob

    if cashew > farming and cashew > cane:
        ans = "Сбор кешью"
    elif farming > cane:
        ans = "Животноводство"
    else:
        ans = "Сбор сахарного тростника"

    writer.write_text(target_doc_path,
                      "7. " + ans,
                      "Arial", 14,
                      align.LEFT,
                      False)
