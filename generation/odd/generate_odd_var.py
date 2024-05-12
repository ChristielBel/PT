import generation.generate_var as generate_var
import generation.odd.tasks.task_1 as task_1
import generation.odd.tasks.task_2 as task_2
import generation.odd.tasks.task_3 as task_3
import generation.odd.tasks.task_4 as task_4
import generation.odd.tasks.task_5 as task_5
import generation.odd.tasks.task_6 as task_6
import generation.odd.tasks.task_7 as task_7
import generation.odd.tasks.task_8 as task_8
import generation.odd.tasks.task_9 as task_9
import generation.odd.tasks.task_10 as task_10
import generation.odd.tasks.task_11 as task_11
import generation.odd.tasks.task_12 as task_12
import generation.odd.tasks.task_13 as task_13
import generation.odd.tasks.task_14 as task_14
import generation.odd.tasks.task_15 as task_15
import generation.odd.tasks.task_16 as task_16
import generation.odd.tasks.task_17 as task_17

# List for all generating functions
task_functions = [
    task_1.generate_task,
    task_2.generate_task,
    task_3.generate_task,
    task_4.generate_task,
    task_5.generate_task,
    task_6.generate_task,
    task_7.generate_task,
    task_8.generate_task,
    task_9.generate_task,
    task_10.generate_task,
    task_11.generate_task,
    task_12.generate_task,
    task_13.generate_task,
    task_14.generate_task,
    task_15.generate_task,
    task_16.generate_task,
    task_17.generate_task
]
ans_functions = [
    task_1.calculate_task,
    task_2.calculate_task,
    task_3.calculate_task,
    task_4.calculate_task,
    task_5.calculate_task,
    task_6.calculate_task,
    task_7.calculate_task,
    task_8.calculate_task,
    task_9.calculate_task,
    task_10.calculate_task,
    task_11.calculate_task,
    task_12.calculate_task,
    task_13.calculate_task,
    task_14.calculate_task,
    task_15.calculate_task,
    task_16.calculate_task,
    task_17.calculate_task
]


def generate_odd(check_values, doc_path, ans_path, num):
    generate_var.generate_var(task_functions, ans_functions, check_values, doc_path, ans_path, num)
