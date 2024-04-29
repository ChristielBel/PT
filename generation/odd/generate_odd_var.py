# List for all generating functions
task_functions = []


def generate_odd(check_values, document):
    # Starting generating new var
    for i in range(check_values.lenght):
        if check_values[i]:
            task_functions[i](document)
