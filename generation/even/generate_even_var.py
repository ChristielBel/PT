import generation.generate_var as generate_var

# List for all generating functions
task_functions = [
]
ans_functions = [
]


def generate_even(check_values, doc_path, ans_path, num):
    generate_var.generate_var(task_functions, ans_functions, check_values, doc_path, ans_path, num)
