import generation.generate_var as generate_var
import generation.even.tasks.task1 as task1

# List for all generating functions
task_functions = [
]
ans_functions = [
    task1.calculate_task,
]

def generate_even(check_values, doc_path, ans_path, num):
    generate_var.generate_var(task_functions, ans_functions, check_values, doc_path, ans_path, num)
