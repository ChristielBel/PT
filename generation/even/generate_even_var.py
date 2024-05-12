import generation.generate_var as generate_var
import generation.even.tasks.task1 as task1
import generation.even.tasks.task2 as task2
import generation.even.tasks.task3 as task3
import generation.even.tasks.task4 as task4
import generation.even.tasks.task5 as task5
import generation.even.tasks.task6 as task6
import generation.even.tasks.task7 as task7
import generation.even.tasks.task8 as task8
import generation.even.tasks.task9 as task9
import generation.even.tasks.task10 as task10
import generation.even.tasks.task11 as task11
import generation.even.tasks.task12 as task12
import generation.even.tasks.task13 as task13
import generation.even.tasks.task14 as task14
import generation.even.tasks.task15 as task15
import generation.even.tasks.task16 as task16

# List for all generating functions
task_functions = [
    task1.generate_task,
    task2.generate_task,
    task3.generate_task,
    task4.generate_task,
    task5.generate_task,
    task6.generate_task,
    task7.generate_task,
    task8.generate_task,
    task9.generate_task,
    task10.generate_task,
    task11.generate_task,
    task12.generate_task,
    task13.generate_task,
    task14.generate_task,
    task15.generate_task,
    task16.generate_task,
]
ans_functions = [
    task1.calculate_task,
    task2.calculate_task,
    task3.calculate_task,
    task4.calculate_task,
    task5.calculate_task,
    task6.calculate_task,
    task7.calculate_task,
    task8.calculate_task,
    task9.calculate_task,
    task10.calculate_task,
    task11.calculate_task,
    task12.calculate_task,
    task13.calculate_task,
    task14.calculate_task,
    task15.calculate_task,
    task16.calculate_task,
]


def generate_even(check_values, doc_path, ans_path, num):
    generate_var.generate_var(task_functions, ans_functions, check_values, doc_path, ans_path, num)
