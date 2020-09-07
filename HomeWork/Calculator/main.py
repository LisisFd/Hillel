import tkinter as tk


class Calculator:
    def __init__(self, master):
        mas = ['+', '-', '*', '/']
        self.master = master
        self.first_entry_num = tk.Entry(self.master, width=10)
        self.second_entry_num = tk.Entry(self.master, width=10)
        self.l = tk.Entry(self.master, bg='black', fg='white', width=20)
        self.first_entry_num.pack()
        self.second_entry_num.pack()
        for i in mas:
            button = tk.Button(self.master, text=i, command=self.createButtonOperation(i))
            button.pack(side='left')

        self.l.pack()

    def createButtonOperation(self,i):
        #first_num =
        #second_num = self.second_entry_num.get()
        #print(first_num, second_num)
        try:
            self.l.insert(0, eval(self.first_entry_num.get() + "+" + self.second_entry_num.get()))
        except:
            pass
root = tk.Tk()

first_cal = Calculator(root)

root.mainloop()