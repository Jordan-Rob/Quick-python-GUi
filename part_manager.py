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

# Parts List
Parts_list = Listbox(app, height=8, width=50)
Parts_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)


# scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)

# set scroll to listbox
Parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=Parts_list.yview)

# buttons
add_btn = Button(app, text='Add part', width=12, command=add_item)
add_btn.grid(row=2, column=0, pady=20)

Remove_btn = Button(app, text='Remove part', width=12, command=add_item)
Remove_btn.grid(row=2, column=1, pady=20)

update_btn = Button(app, text='update part', width=12, command=add_item)
update_btn.grid(row=2, column=2, pady=20)

Clear_btn = Button(app, text='Clear Input', width=12, command=add_item)
Clear_btn.grid(row=2, column=3, pady=20)


app.title('Part Manager')
app.geometry('700x350')

app.mainloop()
