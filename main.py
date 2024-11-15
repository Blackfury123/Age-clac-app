import tkinter as tk

def convert_length():
    length_in_inches = float(text_entry.get())
    length_in_cm = length_in_inches * 2.54
    result_label.config(text=f"{length_in_cm:.2f} cm")

window = tk.Tk()
window.title("Length Converter")

label = tk.Label(window, text="Enter length in inches:")
label.pack()
text_entry = tk.Entry(window)
text_entry.pack()

convert_button = tk.Button(window, text="Convert", command=convert_length)
convert_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
