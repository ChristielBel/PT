from docx.enum.text import WD_PARAGRAPH_ALIGNMENT as align
import generation.odd.tasks.task1.task_1 as task_1
import generation.odd.tasks.task2.task_2 as task_2
import generation.odd.tasks.task3.task_3 as task_3
import generation.odd.tasks.task4.task_4 as task_4
import generation.odd.tasks.task5.task_5 as task_5
import generation.odd.tasks.task6.task_6 as task_6
import generation.odd.tasks.task7.task_7 as task_7
import generation.odd.tasks.task8.task_8 as task_8
import generation.odd.tasks.task9.task_9 as task_9
import generation.odd.tasks.task10.task_10 as task_10
import generation.odd.tasks.task11.task_11 as task_11
import generation.odd.tasks.task12.task_12 as task_12
import generation.odd.tasks.task13.task_13 as task_13
import generation.odd.tasks.task14.task_14 as task_14
import generation.odd.tasks.task15.task_15 as task_15
import generation.odd.tasks.task16.task_16 as task_16
import generation.odd.tasks.task17.task_17 as task_17

import generation.writer as writer

# List for all generating functions
task_functions = [
    task_1.generate_task,
    task_2.generate_task,
    task_3.generate_task,
    task_4.generate_task
]
ans_functions = [
    task_1.calculate_task,
    task_2.calculate_task,
    task_3.calculate_task,
    task_4.calculate_task
]


def generate_odd(check_values, doc_path, ans_path, num):
    # Writing header
    if num == 1:
        header = "Вариант " + str(num)
    else:
        header = "Вариант " + str(num) + '\n'

    writer.write_text(doc_path, header, "Arial", 14, align.CENTER, True)
    writer.write_text(ans_path, header, "Arial", 14, align.CENTER, True)

    # Starting generating new var
    for i in range(len(task_functions)):
        if check_values[i].get():
            task_functions[i](doc_path)
            ans_functions[i](ans_path)
