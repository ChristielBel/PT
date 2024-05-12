import math
import os
import random

from docx.enum.text import WD_PARAGRAPH_ALIGNMENT as align

import generation.writer as writer

source_doc_path = os.path.dirname(os.path.abspath(__file__)) + "/texts/task15.docx"
mx = 5000
alpha = 7000
beta = 10000


def generate_task(target_doc_path):
    global mx
    global alpha
    global beta

    mx = random.randint(3, 5) * 1000
    alpha = random.randint(6, 8) * 1000
    beta = random.randint(9, 11) * 1000

    replacement_values = [mx, alpha, beta]

    writer.replace_placeholders_and_write_to_target(source_doc_path, target_doc_path, replacement_values, "`")


def calculate_task(target_doc_path):
    global mx
    global alpha
    global beta

    l = 1 / mx

    ans = math.exp(-l * alpha) - math.exp(-l * beta)

    writer.write_text(target_doc_path,
                      "15. " + f'{ans:.5f}',
                      "Arial", 14,
                      align.LEFT,
                      False)
