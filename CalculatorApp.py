from tkinter import *

root = Tk()
root.geometry("350x350")
root.resizable(0,0)
root.title("Calculator")

def btn_clk(val):
    global exp
    exp = exp + str(val)
    input_text.set(exp)

def btn_clr():
    global exp
    exp = ""
    input_text.set("")
    
def btn_eq():
    global exp
    res = str(eval(exp))
    input_text.set(res)
    exp = ""

exp = ""
input_text = StringVar()

input_frame = Frame(root,width=350, height=50,)
input_frame.pack(side=TOP)

input_field = Entry(input_frame,bg='BLACK',fg='WHITE',font=('arial',18,'bold'),textvariable=input_text,width=50,justify=RIGHT)
input_field.grid(row=0,column=0)
input_field.pack(ipady=10)

btn_frame = Frame(root,width=350,height=295)
btn_frame.pack(ipady=10)

clr = Button(btn_frame,text="CE",width=22,height=3,command=lambda:btn_clr()).grid(row=0,column=0,columnspan=2,padx=1,pady=0)
div = Button(btn_frame,text="/",width=10,height=3,command=lambda:btn_clk("/")).grid(row=0,column=3,padx=1,pady=1)
mod = Button(btn_frame,text="%",width=10,height=3,command=lambda:btn_clk("%")).grid(row=0,column=2,padx=1,pady=1)

seven = Button(btn_frame,text="7",width=10,height=3,command=lambda:btn_clk("7")).grid(row=1,column=0,padx=1,pady=1)
eight = Button(btn_frame,text="8",width=10,height=3,command=lambda:btn_clk("8")).grid(row=1,column=1,padx=1,pady=1)
nine = Button(btn_frame,text="9",width=10,height=3,command=lambda:btn_clk("9")).grid(row=1,column=2,padx=1,pady=1)
mul = Button(btn_frame,text="x",width=10,height=3,command=lambda:btn_clk("*")).grid(row=1,column=3,padx=1,pady=1)

four = Button(btn_frame,text="4",width=10,height=3,command=lambda:btn_clk("4")).grid(row=2,column=0,padx=1,pady=1)
five = Button(btn_frame,text="5",width=10,height=3,command=lambda:btn_clk("5")).grid(row=2,column=1,padx=1,pady=1)
six = Button(btn_frame,text="6",width=10,height=3,command=lambda:btn_clk("6")).grid(row=2,column=2,padx=1,pady=1)
sub = Button(btn_frame,text="-",width=10,height=3,command=lambda:btn_clk("-")).grid(row=2,column=3,padx=1,pady=1)

one = Button(btn_frame,text="1",width=10,height=3,command=lambda:btn_clk("1")).grid(row=3,column=0,padx=1,pady=1)
two = Button(btn_frame,text="2",width=10,height=3,command=lambda:btn_clk("2")).grid(row=3,column=1,padx=1,pady=1)
three = Button(btn_frame,text="3",width=10,height=3,command=lambda:btn_clk("3")).grid(row=3,column=2,padx=1,pady=1)
add = Button(btn_frame,text="+",width=10,height=3,command=lambda:btn_clk("+")).grid(row=3,column=3,padx=1,pady=1)

zero = Button(btn_frame,text="0",width=10,height=3,command=lambda:btn_clk("0")).grid(row=4,column=0,padx=1,pady=1)
point = Button(btn_frame,text=".",width=10,height=3,command=lambda:btn_clk(".")).grid(row=4,column=1,padx=1,pady=1)
equals = Button(btn_frame,text="=",width=22,height=3,bg='ORANGE',fg='WHITE',command=lambda:btn_eq()).grid(row=4,column=2,columnspan=2,padx=1,pady=1)

root.mainloop()
