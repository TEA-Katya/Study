import tkinter as tk
from tkinter import ttk, messagebox, filedialog

#Калькулятор
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        op = operator_var.get()
        result_text = ""

        if op == '+':
            result_text = str(num1 + num2)
        elif op == '-':
            result_text = str(num1 - num2)
        elif op == '*':
            result_text = str(num1 * num2)
        elif op == '/':
            if num2 == 0:
                result_text = "Я запрещаю вам делить на 0!"
            else:
                result_text = str(num1 / num2)
        else:
            result_text = "Выберите операцию"
    except ValueError:
        result_text = "Введите числа"
    label_result.config(label_result.config(text="Результат: " + result_text))

# Чекбоксы
def show_checkbox_selection():
    selected = []
    if cb_var1.get(): selected.append("1")
    if cb_var2.get(): selected.append("2")
    if cb_var3.get(): selected.append("3")

    if selected:
        messagebox.showinfo("Ваш выбор", f"Вы выбрали: {', '.join(selected)}")
    else:
        messagebox.showinfo("Ваш выбор", "Ничего не выбрано")

#Текстовый редактор
def load_text_from_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                text_editor.delete(1.0, tk.END)
                text_editor.insert(tk.END, file.read())
        except Exception as e:
            messagebox.showerror("Ошибка загрузки", f"Не удалось загрузить файл: {e}")

#Ukfdyjt jryj
root = tk.Tk()
root.title("Терехова Екатерина А.")

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both', padx=10, pady=10) # Отступы


tab1 = ttk.Frame(notebook)
notebook.add(tab1, text='Калькулятор')

entry_num1 = ttk.Entry(tab1, width=10)
entry_num1.pack(pady=5)

operator_var = tk.StringVar(root)
operator_var.set('+') # Значение по умолчанию
operator_menu = ttk.Combobox(tab1, textvariable=operator_var, values=['+', '-', '*', '/'], state='readonly', width=5)
operator_menu.pack(pady=5)

entry_num2 = ttk.Entry(tab1, width=10)
entry_num2.pack(pady=5)

calc_button = ttk.Button(tab1, text='Вычислить', command=calculate)
calc_button.pack(pady=10)

label_result = ttk.Label(tab1, text='Результат: ')
label_result.pack(pady=5)

tab2 = ttk.Frame(notebook)
notebook.add(tab2, text='Чекбоксы')

cb_var1, cb_var2, cb_var3 = tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar()

ttk.Checkbutton(tab2, text='1', variable=cb_var1).pack(pady=5, anchor='w')
ttk.Checkbutton(tab2, text='2', variable=cb_var2).pack(pady=5, anchor='w')
ttk.Checkbutton(tab2, text='3', variable=cb_var3).pack(pady=5, anchor='w')

ttk.Button(tab2, text='Показать выбор', command=show_checkbox_selection).pack(pady=15)

tab3 = ttk.Frame(notebook)
notebook.add(tab3, text='Текст')

text_editor = tk.Text(tab3, wrap='word', height=10, width=50)
text_editor.pack(expand=True, fill='both', padx=10, pady=10)

#Меню для загрузки файла
menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Загрузить текст", command=load_text_from_file)

root.mainloop()
