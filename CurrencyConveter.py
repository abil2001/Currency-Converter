from currency_converter import CurrencyConverter
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import OptionMenu, StringVar

c = CurrencyConverter()

# Creating main window
window = tk.Tk()
window.geometry("500x600+100+100")
window.title("Currency Converter")
window.configure(bg="#202630")
window.resizable(False, False)
window.attributes('-alpha', 0.95)

# Adding window icon
window.iconbitmap("images.ico")

# Creating body frame
body = tk.Frame(window, bg="#202630", bd=10, relief="groove")
body.pack(expand=True, fill="both", padx=10, pady=10)


# Creating header label
header = tk.Label(body, text="Currency Converter", font=("Times", 20, "underline bold"), bg="#202630", fg="White")
header.pack(pady=20)

# Creating image label
img = ImageTk.PhotoImage(Image.open("download.png").resize((100, 100)))
img_label = tk.Label(body, image=img, bg="#202630", fg="#202630")
img_label.pack()

# Creating input widgets
amount_label = tk.Label(body, text="Amount to be converted: ", font=("Times", 16, "bold"), bg="#202630", fg="White")
amount_label.pack(pady=10)
amount_entry = tk.Entry(body, font=("Arial", 14, "bold"))
amount_entry.pack(pady=10)

options_frame = tk.Frame(body, bg="#202630")
options_frame.pack(pady=10)
from_label = tk.Label(options_frame, text="From:", font=("Arial", 14, "bold"), bg="#202630", fg="White")
from_label.pack(side=tk.LEFT, padx=10)
from_var = StringVar(value="INR")
from_menu = OptionMenu(options_frame, from_var, *c.currencies,
                       command=lambda x: from_menu.config(width=max([len(i) for i in c.currencies]) + 2))
from_menu.config(bg="#00BFFF", font=("Arial", 14, "bold"))
from_menu["menu"].config(bg="#34495E",  fg="White", font=("Arial", 14, "bold"))
from_menu.pack(side=tk.LEFT, padx=10)

to_label = tk.Label(options_frame, text="To:", font=("Arial", 14, "bold"), bg="#202630", fg="White")
to_label.pack(side=tk.LEFT, padx=10)
to_var = StringVar(value="EUR")
to_menu = OptionMenu(options_frame, to_var, *c.currencies,
                     command=lambda x: to_menu.config(width=max([len(i) for i in c.currencies]) + 2))
to_menu.config(bg="#00BFFF", font=("Arial", 14, "bold"))
to_menu["menu"].config(bg="#34495E", fg="White", font=("Arial", 14, "bold"))
to_menu.pack(side=tk.LEFT, padx=10)

# Creating conversion and exit buttons
button_frame = tk.Frame(body, bg="#202630")
button_frame.pack(pady=20)
convert_button = tk.Button(button_frame, text="Convert", font=("Arial", 14, "bold"), bg="#4CAF50", fg="Black",
                           command=lambda: convert(amount_entry.get(), from_var.get(), to_var.get()))
convert_button.pack(side=tk.LEFT, padx=10)
exit_button = tk.Button(button_frame, text="Exit", font=("Arial", 14, "bold"), bg="#F44336", fg="Black",
                        command=lambda: window.destroy())
exit_button.pack(side=tk.LEFT, padx=10)

# Creating result label
result_label = tk.Label(body, font=("Arial", 16, "bold"), bg="#202630")
result_label.pack(pady=20)


def convert(amount, from_currency, to_currency):
    try:
        result = c.convert(amount, from_currency, to_currency)
        result_label.config(text=f" \n {amount} {from_currency} = {result:.2f} {to_currency}  \n ", font=("Arial", 14, "bold"), bg="#202630", fg="White", bd=10, relief="groove")
        result_label.pack(expand=True, fill="none", padx=5, pady=5)
    except:
        result_label.config(text="  \n Error: Invalid input \n Please enter the correct input. \n ", font=("Arial", 14, "bold"), bg="#202630", fg="White", bd=10,  relief="groove")
        result_label.pack(expand=True, fill="none", padx=5, pady=5)


# Starting main loop
window.mainloop()
