from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# Initialize tkinter token with the root widget
root = Tk()
style = ttk.Style(root)
#adjust the path here according to your local env
root.call('lappend', 'auto_path', 'C:/Users/miniconda3/envs/test/awthemes-10.2.1')
root.call('package', 'require', 'awdark')
current_theme = style.theme_use('awdark')
root.iconphoto(False, PhotoImage(file="icon.ico"))

# Configuration Specifications
label = Label(root, width=768)
#adjust the path here according to your locak env
img = Image.open(r"C:\\Users\\miniconda3\\envs\\test\\sample.png")
label.img = ImageTk.PhotoImage(img)
label['image'] = label.img
label.grid(sticky='nsew')
label.grid_propagate(0)
label.rowconfigure(0, weight=0)
label.rowconfigure((4,5,6,7,8), weight=3)
label.rowconfigure((1,2,3), weight=1)
label.columnconfigure((0,4), weight=0)
label.columnconfigure((1,2), weight=1)

# Calling Label Widget with the specified IP
ttk.Label(label, text="Your IP: ").grid(row = 1, column = 1, sticky='se', padx=20)
e1 = ttk.Entry(label)
e1.place(anchor=CENTER)
e1.grid(row = 1, column = 2, sticky='sw')

# Initializing Radiobutton Widget
R1 = ttk.Radiobutton(label, text="Option 1", variable=IntVar(), value=1)
R2 = ttk.Radiobutton(label, text="Option 2", variable=IntVar(), value=2)
R1.place(relx=0.5, rely=0.5, anchor=CENTER)
R2.place(relx=0.5, rely=0.5, anchor=CENTER)
R1.grid(row = 2, column = 1, columnspan=2, sticky='s', pady= 10)
R2.grid(row = 3, column = 1, columnspan=2, sticky='n')

root.geometry("768x600")
root.configure(bg="#151515")
root.minsize(768,600)
root.maxsize(768,600)
root.title("VCallZer")

root.mainloop() # root widget call
