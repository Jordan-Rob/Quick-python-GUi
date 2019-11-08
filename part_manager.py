from tkinter import *

#create a window object
app = Tk()

#part
part_text = StringVar()
part_label = Label(app, text='part Name', font=('bold', 14), pady=20)
part_label.grid(row=0, column=0)

part_entry = Entry(app, width=25)
part_entry.grid(row=0, column=1)

app.title('Part Manager')
app.geometry('700x350')

app.mainloop()