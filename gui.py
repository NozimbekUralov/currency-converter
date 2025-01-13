import tkinter, json

import constants, utils

root = tkinter.Tk()

root.title("Currency Converter")

root.geometry("400x300")
root.config(background="white")

header = tkinter.Frame(root)
header.config(background="white")
header.pack(side=tkinter.TOP)

body = tkinter.Frame(root)
body.config(background="white")
body.pack()

response = utils.load_data()
codes = utils.find_available(response)

def convert():
    from_code = selected_code.get()
    res = utils.converter(
        from_code=from_code,
        amount=float(entry.get()),
        list_of_currencies=response
    )

    res = utils.format_num(res)
    
    label.config(text=f"{str(res)} UZS")

tkinter.Label(
    header, text="Valyuta konvertori", 
    foreground="black", background="white", 
    font=("Arial", 34)
).grid(row=0, column=0)

selected_code = tkinter.StringVar(root, "USD")
tkinter.OptionMenu(
    body, selected_code, *codes,
).grid(row=1, column=0)

entry = tkinter.Entry(
    body, width=10,
    foreground="black", background="white", 
    font=("Arial", 20),
)
entry.grid(row=1, column=1)

tkinter.Button(
    body, text="Convert", 
    foreground="black", background="white", 
    font=("Arial", 18),
    height=1,
    command=convert
).grid(row=1, column=2)

tkinter.Label(
    body, text=f"result:", 
    foreground="black", background="white", 
    font=("Arial", 20)
).grid(row=2, column=0)

label = tkinter.Label(
    body, text="", 
    foreground="black", background="white", 
    font=("Arial", 20)
)
label.grid(row=2, column=1)



try: 
    root.mainloop()
except KeyboardInterrupt:
    root.destroy()