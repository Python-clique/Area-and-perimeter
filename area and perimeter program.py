from tkinter import *
root = Tk()
root.configure(bg = 'light blue')
n1 = IntVar()
n2 = IntVar()

def multiplication():
    m1 = n1.get()
    m2 = n2.get()
    m3 = m2 * m2
    label1 = Label(root , text = "Area is = %d" %m3 , bg = "light blue").place(relx = 0.3 , rely = 0.75 )
def perimeter():
    m1 = n1.get()
    m2 = n2.get()
    m3 = m1 + m2
    label2 = Label(root , text = "Perimeter = %d" %m3 , bg = "light blue").place(relx = 0.3 , rely = 0.75)
labeldisp1 = Label(root , text = "Length" , bg = "light blue").place(relx = 0 , rely = 0.3) 
labeldisp2 = Label(root , text = "Breadth" , bg = "light blue").place(relx = 0 , rely = 0.4)   
num1  = Entry(root , textvariable = n1).place(relx = 0.3 , rely = 0.3)
num2 = Entry(root , textvariable = n2).place(relx = 0.3 , rely = 0.4)    
multiplicationbutton = Button(root , text = "Area" ,command = multiplication).place(relx = 0.3 , rely = 0.6)  
perimeter = Button(root , text = "Perimeter" , command = perimeter).place(relx = 0.5 , rely = 0.6)  
root.geometry("200x200")
root.mainloop()
    