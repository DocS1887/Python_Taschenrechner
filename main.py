import tkinter as tk


app = tk.Tk()
app.geometry("150x220+50+50")
app.title("Taschenrechner")

# Liste der Buttonbeschriftung
gui_items = list()
button_values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '+', '-',
                 '*', '/', '=', 'AC']

calculation = str()


def add_button_value_to_calculation(value):
    global calculation

    # Überprüfung ob AC gedrückt wurde
    if value == 'AC':
        calculation = str()
        output_label['text'] = 'Bereit...'
        return
    # Überprüfung ob = gedrückt wurde
    if value == '=':
        calculate(calculation)
        calculation = str()
        return

    calculation = calculation + value
    output_label['text'] = calculation


def calculate(calc):
    try:
        result = eval(calc)
        print(result)
        output_label['text'] = result

    except Exception as e:
        print(e)
        output_label['text'] = "Error!"


def create_button(value):
    button = tk.Button(
        text=value, command=lambda: add_button_value_to_calculation(value))
    gui_items.append(button)


for val in button_values:
    create_button(val)

# Ergebnisausgabe
output_label = tk.Label(text="Bereit...")
output_label.grid(row=0, columnspan=10)

# Ausrichtung der Buttons 
column_count = 0
row_count = 1
max_columns = 3

for item in gui_items:
    item.grid(row=row_count, column=column_count)
    column_count += 1

    if column_count == max_columns:
        column_count = 0
        row_count += 1


if __name__ == '__main__':
    app.mainloop()
