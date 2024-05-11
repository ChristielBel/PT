import os
import tkinter as tk
from tkinter import messagebox

import docx

import generation.odd.generate_odd_var as odd_gen


class MyApp:
    def __init__(self, root, title_font, regular_font):
        self.root = root
        self.root.title("Генератор")
        self.root.geometry("900x500")
        self.title_font = title_font
        self.regular_font = regular_font
        self.check_vals = []
        self.entry_var = tk.IntVar()
        self.entry_var.set(1)
        self.create_widgets()

    def create_widgets(self):
        # Frame to contain the entry field
        entry_frame = tk.Frame(self.root)
        entry_frame.pack(pady=20)

        # Label for the entry field
        entry_label = tk.Label(entry_frame, text="Количество вариантов:", font=self.title_font)
        entry_label.grid(row=0, column=0)

        # Entry field
        entry_field = tk.Entry(entry_frame, textvariable=self.entry_var)
        entry_field.grid(row=0, column=1)

        # Frame to contain the checkboxes
        checkbox_frame = tk.Frame(self.root)
        checkbox_frame.pack(pady=20)

        # Create 17 checkboxes with sequential tasks
        for i in range(20):
            val = tk.BooleanVar()
            checkbox = tk.Checkbutton(
                checkbox_frame,
                height=2,
                width=10,
                text=f"Задание {i + 1}",
                font=self.regular_font,
                variable=val,
            )

            checkbox.select()
            checkbox.grid(row=i // 5, column=i % 5, sticky="w")
            self.check_vals.append(val)

        # Checkbox to check/uncheck all checkboxes
        check_var = tk.BooleanVar()
        check_all_checkbox = tk.Checkbutton(
            self.root,
            text="Выделить все",
            font=self.regular_font,
            variable=check_var,
            command=lambda: self.check_uncheck_all(check_var)
        )
        check_all_checkbox.select()
        check_all_checkbox.pack()

        # Button to save file
        save_button = tk.Button(self.root, text="Сгенерировать", font=self.regular_font, command=self.save_file)
        save_button.pack(pady=20)

    def save_file(self):
        # Delete old files if they exist
        try:
            os.remove("Варианты.docx")
            os.remove("Ответы.docx")
        except OSError:
            pass

        # Create files for vars and answers
        path_var = "Варианты.docx"
        path_ans = "Ответы.docx"
        doc1 = docx.Document()
        doc2 = docx.Document()
        doc1.save(path_var)
        doc2.save(path_ans)

        var_count = self.entry_var.get()

        for i in range(var_count):
            # Create base files
            # Every function edits and adds its task to the output file
            # If corresponding check is checked

            odd_gen.generate_odd(self.check_vals, os.path.abspath(path_var), os.path.abspath(path_ans), i + 1)
            i += 1
            if i < var_count:
                # even_gen.generate_even(self.check_vals, os.path.abspath(path_var), os.path.abspath(path_ans), i+1)
                1

        messagebox.showinfo("Файл сохранен", "Файл был успешно сохранен.")

    def check_uncheck_all(self, check_var):
        for checkbox in self.check_vals:
            checkbox.set(check_var.get())


# Create the Tkinter application window
tk_root = tk.Tk()
app = MyApp(tk_root, "Arial 21 bold", "Arial 15")
tk_root.mainloop()
