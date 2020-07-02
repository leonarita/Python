from tkinter import *
import tkinter.messagebox


def save_data():
    try:
        fileD=open("deliveries.txt", "a")
        fileD.write("Depot\n")
        fileD.write("%s\n" % depot.get())
        fileD.write("Description\n")
        fileD.write("%s\n" % description.get())
        fileD.write("Address\n")
        fileD.write("%s\n" % address.get("1.0", END))
        depot.set("")
        description.delete(0, END)
        description.delete(0, END)
        address.delete("1.0", END)
    except Exception as ex:
        tkinter.messagebox.showerror("Error!", "Can't write to the file\n %s" % ex)


def read_depots(file):
    depots = []
    depots = ["Cambridge, MA", "Cambridge, UK", "Seattle, WA"]

    """
    depots_f = open(file)
    for line in depots_f:
        depots.append(line.rstrip())
    """
    return depots


app = Tk()
app.title('Head-Ex Deliveries')
Label(app, text="Depot:").pack()
depot = StringVar()
depot.set(None)

"""
Radiobutton(app, variable=depot, text="Cambridge, MA", value="Cambridge, MA").pack()
Radiobutton(app, variable=depot, text="Cambridge, UK", value="Cambridge, UK").pack()
Radiobutton(app, variable=depot, text="Seattle, WA", value="Seattle, WA").pack()

depot = StringVar()
depot.set(None)
OptionMenu(app, depot, "Cambridge, MA", "Cambridge, UK", "Seattle, WA").pack()
"""

options = read_depots("depots.txt")
OptionMenu(app, depot, *options).pack()

Label(app, text="Description:").pack()
description = Entry(app)
description.pack()
Label(app, text="Address:").pack()
address = Text(app)
address.pack()
Button(app, text="Save", command=save_data).pack()
app.mainloop()
