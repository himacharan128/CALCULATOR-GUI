from tkinter import *
import random
from tkinter import messagebox as mb
class Calculator:
    
    def __init__(self,cal):
        self.cal=cal
        cal.title("Calculator")
        self.equation=Entry(cal, width=30, borderwidth=7)
        self.equation.grid(row=0, column=0, columnspan=10, padx=20, pady=20)

        self.createButton()
    
    def createButton(self):
       b0 = self.addButton(0)
       b1 = self.addButton(1)
       b2 = self.addButton(2)
       b3 = self.addButton(3)
       b4 = self.addButton(4)
       b5 = self.addButton(5)
       b6 = self.addButton(6)
       b7 = self.addButton(7)
       b8 = self.addButton(8)
       b9 = self.addButton(9)
       b_add = self.addButton('+')
       b_sub = self.addButton('-')
       b_mult = self.addButton('*')
       b_div = self.addButton('/')
       b_clear = self.addButton('C')
       b_lb = self.addButton('(')
       b_rb = self.addButton(')')
       b_less= self.addButton('<')
       b_power= self.addButton('^')
       b_equal = self.addButton('=')
    

       row1=[b_clear,b_lb,b_rb,b_less]
       row2=[b7,b8,b9,b_mult]
       row3=[b4,b5,b6,b_sub]
       row4=[b1,b2,b3,b_add]
       row5=[b_power,b0,b_equal,b_div]
       


       r=1
       for row in [row1, row2, row3, row4,row5]:
           c=0
           for buttn in row:
               buttn.grid(row=r, column=c, columnspan=1)
               c+=1
           r+=1

 
    def addButton(self,value):
        colour1=["orange","skyblue","hotpink","orange"]
        colour2=['white','yellow','light green','cyan4','light blue']
        back=random.choice(colour2)
        front=random.choice(colour1)
        return Button(self.cal, text=value,bg=back,fg=front, width=8,height=3
                      ,command = lambda: self.clickButton(str(value)))

    def clickButton(self,value):
        current_equation=str(self.equation.get())
        current_equation=current_equation.replace('^','**')
        if value == 'C':
            self.equation.delete(-1, END)
        elif value=='':
            mb.showerror('ERROR','enter something')
        elif value == '=':
            try:
                answer = str(eval(current_equation))
                self.equation.delete(-1, END)
                self.equation.insert(0, answer)
            except:
                mb.showerror('ERROR','PLEASE CHECK \n&\nenter proper equation!')
        else:
            self.equation.delete(0, END)
            self.equation.insert(-1, current_equation+value)


if __name__=='__main__':
    root = Tk()
    root.configure(bg='orange')
    my_gui = Calculator(root)
    root.mainloop()
