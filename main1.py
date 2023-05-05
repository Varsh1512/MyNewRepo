from tkinter import *

window = Tk()
window.title('Assignment 5.5')
window.minsize(width=700, height=500)
new_label = Label(text='Label-1', font= ('Helvetica',25, 'italic'))
new_label.pack()
new_label['text']='New text'
new_label.config(text='Initial text')

def button_fun():
    new_label.config(text='Button got clicked.')

button=Button(text = 'Click here', command=button_fun)
button.pack()

window.mainloop()
