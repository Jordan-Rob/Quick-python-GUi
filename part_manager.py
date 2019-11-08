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

app.title('Part Manager')
app.geometry('700x350')

app.mainloop()
