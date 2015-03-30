import Tkinter
from Tkinter import *
from ScrolledText import *
import tkFileDialog
import tkMessageBox

root = Tkinter.Tk(className="My Text Editor")
root.configure(background='green')
textPad = ScrolledText()
textPad.pack(fill='both', expand=1)

# Clears Text Area for new Document
def filenew():
    if tkMessageBox.askokcancel(title="Clean Window", message="Do you want to clear your data?"):
        textPad.delete(1.0, END)

# Open File Menu Item
def fileopen():
    file = tkFileDialog.askopenfile(mode='rb',title="Select a file")
    if file != None:
        contents = file.read()
        textPad.insert('1.0',contents)
        file.close()

# Save As File Menu Item
def filesaveas():
    file = tkFileDialog.asksaveasfile(mode='w',title="Save As", defaultextension=".txt")
    if file != None:
        data = str(textPad.get(1.0,END))
        file.write(data)
        file.close()

# Menu Item Place Holder To Prove Functionality
def dummy():
    print "Some stuff."



# Textpad Top Menu
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=filenew)
filemenu.add_command(label="Open", command=fileopen)
filemenu.add_command(label="Save", command=dummy)
filemenu.add_command(label="Save As", command=filesaveas)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=dummy)
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=dummy)
#end Texpad Top Menu



root.mainloop()





