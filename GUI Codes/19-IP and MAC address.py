import tkinter as tk
from tkinter.messagebox import showinfo
import socket
from getmac import getmac

win = tk.Tk()
win.config(bg="#F1C40F")
win.title("Find IP and MAC Address")


def ip():
    hostname = socket.gethostname()
    ip_add = socket.gethostbyname(hostname)
    showinfo("IP Address", f"IP Address : {ip_add}")


def mac():
    mac_add = getmac.get_mac_address()
    showinfo("MAC Address", f"MAC Address : {mac_add}")


ip_button = tk.Button(win, text="Show IP Address", bg="#000000", fg="#F1C40F", font=("times new roman", 16, "bold"), command=ip)
mac_button = tk.Button(win, text="Show MAC Address", bg="#000000", fg="#F1C40F", font=("times new roman", 16, "bold"), command=mac)

ip_button.pack()
mac_button.pack()

win.mainloop()