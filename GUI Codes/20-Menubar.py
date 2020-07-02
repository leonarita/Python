from tkinter import *

root = Tk()
root.title("Menu in GUI")
root.geometry("250x100")

# Creating Menubar
menubar = Menu(root)
root.config(menu=menubar)
filemenu = Menu(menubar, tearoff=0)

# Creates File Menu In Menu Bar
menubar.add_cascade(label="File", menu=filemenu)

# Create Another Option In File Menu
menubar.add_command(label="New", command=None)

# Creating View Menu In Menubar
menubar.add_command(label="View")

# Creates Exit Menu, It Will Close Window While Click On It
menubar.add_command(label="Exit", command=root.destroy)

root.mainloop()