import tkinter as tk
from tkinter import messagebox, filedialog


class MyApp:
    def __init__(self, root, title_font, regular_font):
        self.root = root
        self.root.title("Генератор")
        self.root.geometry("900x500")
        self.title_font = title_font
        self.regular_font = regular_font

        self.entry_var = tk.IntVar()
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
        for i in range(17):
            checkbox = tk.Checkbutton(checkbox_frame, height=2, width=10, text=f"Задание {i + 1}", font=self.regular_font)
            checkbox.grid(row=i // 5, column=i % 5, sticky="w")

        print(tk.BooleanVar().get())

        # Button to save file
        save_button = tk.Button(self.root, text="Сгенерировать", font=self.regular_font, command=self.save_file)
        save_button.pack(pady=20)

    def save_file(self):
        # Dialog for saving file
        filename = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Текстовые файлы", "*.docx")])
        if filename:
            var_count = self.entry_var.get()

            for i in range(var_count):
                # Open base files
                # Every function edits and adds its task to the output file
                # If corresponding check is checked
                1

            messagebox.showinfo("Файл сохранен", "Файл был успешно сохранен.")


# Create the Tkinter application window
tk_root = tk.Tk()
app = MyApp(tk_root, "Arial 21 bold", "Arial 15")
tk_root.mainloop()
