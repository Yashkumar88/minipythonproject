from tkinter import *
root =Tk()
root.title('YK CALCULTORS')
root.iconbitmap('calculator.ico')
root.geometry('280x380')
root.configure(background='black')

# varibles
first=second=third=operator=None

# button functions
def get_digit(digit):
    current = result_label['text']
    new = current +str(digit)
    result_label.config(text=new)
# clear function
def clear():
    result_label.config(text='')
# operators
def get_operaors(op):
    global first,operator
    first=int(result_label['text'])
    operator=op
    result_label.config(text='')
# get results
def get_result():
    global first,second,third,operator
    second =int(result_label['text'])
    if operator == '+':
        result_label.config(text=str(first+second))
    elif operator == '-':
        result_label.config(text=str(first-second))
    elif operator == '*':
        result_label.config(text=str(first*second))
    else:
        if second== 0:
            result_label.config(text='error')
        else:
            result_label.config(text=str(first/second))



result_label =Label(root,text='',fg='white',bg='black',font=('verdana',30,'bold'))
result_label.grid(row=0,column=0,columnspan=10,pady=(50,25),sticky='w')
# 7
btn7 =Button(root,text='7',fg='white',bg='green',font=('verdana',14,'bold'),width=5,height=2,command=lambda :get_digit(7))
btn7.grid(row=1,column=0)
#8
btn8 =Button(root,text='8',fg='white',bg='green',font=('verdana',14,'bold'),width=5,height=2,command=lambda :get_digit(8))
btn8.grid(row=1,column=1)
#9
btn9 =Button(root,text='9',fg='white',bg='green',font=('verdana',14,'bold'),width=5,height=2,command=lambda :get_digit(9))
btn9.grid(row=1,column=2)
# add
btn_add =Button(root,text='+',fg='white',bg='green',font=('verdana',14,'bold'),width=5,height=2,command=lambda :get_operaors('+'))
btn_add.grid(row=1,column=3)
#4
btn4 =Button(root,text='4',fg='white',bg='green',font=('verdana',14,'bold'),width=5,height=2,command=lambda :get_digit(4))
btn4.grid(row=2,column=0)
#5
btn5 =Button(root,text='5',fg='white',bg='green',font=('verdana',14,'bold'),width=5,height=2,command=lambda :get_digit(5))
btn5.grid(row=2,column=1)
# 6
btn6 =Button(root,text='6',fg='white',bg='green',font=('verdana',14,'bold'),width=5,height=2,command=lambda :get_digit(6))
btn6.grid(row=2,column=2)
#sub
btn_sub =Button(root,text='-',fg='white',bg='green',font=('verdana',14,'bold'),width=5,height=2,command=lambda :get_operaors('-'))
btn_sub.grid(row=2,column=3)
#1
btn1 =Button(root,text='1',fg='white',bg='green',font=('verdana',14,'bold'),width=5,height=2,command=lambda :get_digit(1))
btn1.grid(row=3,column=0)
#2
btn2 =Button(root,text='2',fg='white',bg='green',font=('verdana',14,'bold'),width=5,height=2,command=lambda :get_digit(2))
btn2.grid(row=3,column=1)
#3
btn3 =Button(root,text='3',fg='white',bg='green',font=('verdana',14,'bold'),width=5,height=2,command=lambda :get_digit(3))
btn3.grid(row=3,column=2)
#*
btn_mul=Button(root,text='*',fg='white',bg='green',font=('verdana',14,'bold'),width=5,height=2,command=lambda :get_operaors('*'))
btn_mul.grid(row=3,column=3)
#0
btn0 =Button(root,text='0',fg='white',bg='green',font=('verdana',14,'bold'),width=5,height=2,command=lambda :get_digit(0))
btn0.grid(row=4,column=0)
#=
btn_equ =Button(root,text='=',fg='white',bg='green',font=('verdana',14,'bold'),width=5,height=2,command=get_result)
btn_equ.grid(row=4,column=1)
#/
btn_div =Button(root,text='/',fg='white',bg='green',font=('verdana',14,'bold'),width=5,height=2,command=lambda :get_operaors('/'))
btn_div.grid(row=4,column=2)
#c
btn_c =Button(root,text='c',fg='white',bg='green',font=('verdana',14,'bold'),width=5,height=2,command=lambda :clear())
btn_c.grid(row=4,column=3)
root.mainloop()
