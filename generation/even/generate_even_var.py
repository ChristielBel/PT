import generation.generate_var as generate_var
import generation.even.tasks.task1 as task1
import generation.even.tasks.task2 as task2
import generation.even.tasks.task3 as task3
import generation.even.tasks.task4 as task4
import generation.even.tasks.task5 as task5

# List for all generating functions
task_functions = [
    task1.generate_task,
    task2.generate_task,
    task3.generate_task,
    task4.generate_task,
    task5.generate_task
]
ans_functions = [
    task1.calculate_task,
    task2.calculate_task,
    task3.calculate_task,
    task4.calculate_task,
    task5.calculate_task
]

def generate_even(check_values, doc_path, ans_path, num):
    generate_var.generate_var(task_functions, ans_functions, check_values, doc_path, ans_path, num)
