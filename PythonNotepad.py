import Tkinter
from Tkinter import *
from ScrolledText import *
import tkFileDialog
import tkMessageBox

root = Tkinter.Tk(className="My Text Editor")
root.configure(background='green')
textPad = ScrolledText()
textPad.pack(fill='both', expand=1)
file = ''
# Clears Text Area for new Document
def filenew():
    if tkMessageBox.askokcancel(title="Clean Window", message="Do you want to clear your data?"):
        textPad.delete(1.0, END)

# Open File Menu Item
def fileopen():
    global file
    file = tkFileDialog.askopenfile(mode='r',title="Select a file")
    if file != None:
        contents = file.read()
        textPad.insert('1.0',contents)


# Save As File Menu Item
def filesave():
    savefile = tkFileDialog.asksaveasfile(mode='w',title="Save", defaultextension=".txt")
    if savefile != None:
        data = str(textPad.get(1.0,END))
        savefile.write(data)



# Exit File Menu
def exit():
    root.destroy()
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
filemenu.add_command(label="Save", command=filesave)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit)
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=dummy)
#end Texpad Top Menu



root.mainloop()





