from tkinter import *
from tkinter.filedialog import askdirectory

window = Tk()

window.title("Welcome to jpg to pbm converter app")

window.geometry('350x200')

lbl = Label(window, text="1)Place files you want to convert in images\n2)click the CONVERT FILES button\n3)Collect your files from processed images folder")

lbl.grid(column=0, row=0)

def clicked():
    file_source = askdirectory(title='Select Source Folder') # shows dialog box and return the path
    file_destination = askdirectory(title='Select Destination Folder') # shows dialog box and return the path  
    import converter_final
    conv=converter_final.converter(file_source,file_destination)
    conv.main()
    lbl.configure(text="Processing files !!")

btn = Button(window, text="Convert files", command=clicked)

btn.grid(column=1, row=0)

window.mainloop()