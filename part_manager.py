from tkinter import *

# create a window object
app = Tk()

# part
part_text = StringVar()
part_label = Label(app, text='Part Name', font=('bold', 14), pady=20)
part_label.grid(row=0, column=0)

part_entry = Entry(app, width=25, textvariable=part_text)
part_entry.grid(row=0, column=1)

# customer
customer_text = StringVar()
customer_label = Label(app, text="Customer", font=('bold', 14))
customer_label.grid(row=0, column=2)

customer_entry = Entry(app, width=25, textvariable=customer_text)
customer_entry.grid(row=0, column=3)

# Retailer
Retailer_text = StringVar()
Retailer_label = Label(app, text="Retailer", font=('bold', 14))
Retailer_label.grid(row=1, column=0)

Retailer_entry = Entry(app, width=25, textvariable=Retailer_text)
Retailer_entry.grid(row=1, column=1)


# Price
Price_text = StringVar()
Price_label = Label(app, text="Price", font=('bold', 14))
Price_label.grid(row=1, column=2)

Price_entry = Entry(app, width=25, textvariable=Price_text)
Price_entry.grid(row=1, column=3)

app.title('Part Manager')
app.geometry('700x350')

app.mainloop()
