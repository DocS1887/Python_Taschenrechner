import tkinter as tk

app = tk.Tk()


button_one = tk.Button(app,text="1")
button_two = tk.Button(app,text="2")
button_three = tk.Button(app,text="3")
button_four = tk.Button(app,text="4")
button_five = tk.Button(app,text="5")
button_six = tk.Button(app,text="6")
button_seven = tk.Button(app,text="7")
button_eight = tk.Button(app,text="8")
button_nine = tk.Button(app,text="9")
button_equal = tk.Button(app, text="=")
button_plus = tk.Button(app, text="+")
button_minus = tk.Button(app, text="-")
button_mal = tk.Button(app, text="*")
button_share = tk.Button(app, text=":")
button_comma = tk.Button(app, text=".")
button_zero = tk.Button(app, text="0")
button_double_zero = tk.Button(app, text="00")
button_plus_minus = tk.Button(app, text="+/-")

button_clear = tk.Button(app, text="C")

button_one.place(x=20, y=200, width=50, height=50)
button_two.place(x=75, y=200, width=50, height=50)
button_three.place(x=130, y=200, width=50, height=50)
button_plus_minus.place(x=185, y=200, width=50, height=50)
button_clear.place(x=240, y=200, width=50, height=50)

button_four.place(x=20, y=255, width=50, height=50)
button_five.place(x=75, y=255, width=50, height=50)
button_six.place(x=130, y=255, width=50, height=50)

button_seven.place(x=20, y=310, width=50, height=50)
button_eight.place(x=75, y=310, width=50, height=50)
button_nine.place(x=130, y=310, width=50, height=50)

button_comma.place(x=20, y=365, width=50, height=50)
button_double_zero.place(x=130, y=365, width=50, height=50)
button_zero.place(x=75, y=365, width=50, height=50)
button_plus_minus.place(x=185, y=200, width=50, height=50)

button_equal.place(x=240, y=365, width=50, height=50)
button_plus.place(x=185, y=310, width=50, height=105)
button_minus.place(x=185, y=255, width=50, height=50)
button_mal.place(x=240, y=255, width=50, height=50)
button_share.place(x=240, y=310, width=50, height=50)




if __name__ == "__main__":
    app.title("Taschenrechner 2000")
    app.geometry("310x450+50+50")
    app.mainloop()