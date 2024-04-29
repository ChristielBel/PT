from docx.enum.text import WD_PARAGRAPH_ALIGNMENT as align
import generation.odd.tasks.task1.task_1 as task_1
import generation.writer as writer


# List for all generating functions
task_functions = [task_1.generate_task_1]
ans_functions = [task_1.calculate_task]


def generate_odd(check_values, doc_path, ans_path, num):
    # Writing header
    header = "Вариант " + str(num)
    writer.write_text(doc_path, header, "Arial", 14, align.CENTER, True)
    writer.write_text(ans_path, header, "Arial", 14, align.CENTER, True)

    # Starting generating new var
    for i in range(1):
        if check_values[i].get():
            task_functions[i](doc_path)
            ans_functions[i](ans_path)
