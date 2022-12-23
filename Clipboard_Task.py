import tkinter as tk

my_w = tk.Tk()
my_w.geometry("400x350")
my_w.title("cut_copy_paste.com")  # Adding a title
global data

l1 = tk.Label(my_w, text='Name:', font=20)  # added one Label
l1.grid(row=0, column=0, padx=2, pady=10)

e1 = tk.Text(my_w, font=20, height=4, width=28, bg='yellow')  # text box
e1.grid(row=0, column=1, columnspan=4)

def select_all():  # to select all text inside Text box
    e1.tag_add("sel", "1.0", "end")  # all text selected
    e1.tag_config("sel", background="green", foreground="red")

def cut_select():  # Cut the selection of text to clipboard
    global data
    if e1.selection_get():
        data = e1.selection_get()  # copy selected text to clipboard
        e1.delete('sel.first', 'sel.last')  # delete selected text

def copy_select():  # copy selected text to clipboard
    global data
    if e1.selection_get():
        data = e1.selection_get()  # copy selected text to clipboard

def paste_select():
    global data
    e2.insert(tk.END, data)  # Paste data from clipboard

b1 = tk.Button(my_w, text='Select All', command=lambda: select_all(),
               font=20, bg='lightgreen')
b1.grid(row=1, column=1, padx=2, pady=5)

b2 = tk.Button(my_w, text='Cut', command=lambda: cut_select(),
               font=20, bg='lightyellow')
b2.grid(row=1, column=2)

b3 = tk.Button(my_w, text='Copy', command=lambda: copy_select(),
               font=20, bg='lightblue')
b3.grid(row=1, column=3)

b4 = tk.Button(my_w, text='Paste', command=lambda: paste_select(),
               font=20, bg='cyan')
b4.grid(row=1, column=4)

e2 = tk.Text(my_w, font=20, height=4, width=28, bg='yellow')  # added one Entry box
e2.grid(row=2, column=1, columnspan=4, pady=10)

my_w.mainloop()