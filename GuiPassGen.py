from random import *
from tkinter import *
"""
It will import every function from random 
class.
"""

num="0123456789" #Set of numbers.
alphanum = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" #Set of alphanum.
spalphanum = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ@$*" #Set of special,alpha,number.

# passlen = int(input("Enter the length of the password.\n")) #Length of password as per user.
# randPass = []  #It will store random password.

# print("Select the type of password \n1. Numbers\n2. Alphanumeric\n3. Special Alphanumeric\n")
# Selecttype = int(input())

# if Selecttype == 1:
#     for i in range(passlen):
#         randPass.append(choice(num))

# elif Selecttype == 2:
#     for i in range(passlen):
#         randPass.append(choice(alphanum))

# else:
#     for i in range(passlen):
#         randPass.append(choice(spalphanum))

# result = "".join(randPass)

# print("Your random password is: "+result,"\n")

def Create_Pass():

    TheChoice = Tchoice.get()

    if TheChoice == "":
        resultBox.delete(0.0,END)
        resultBox.insert(END, "\n Select the type you would like")

    length = int(pass_length.get())
    randPass = []

    for i in range(length):
        randPass.append(choice(TheChoice))

    result = "".join(randPass)

    TheResult = "\n *** Your Password is: "+result+" ***\n"

    resultBox.delete(0.0,END)
    resultBox.insert(END,TheResult)

window = Tk()
window.geometry("800x500")
window.title("Nikhil Password Generator")

ProgName = Label(window, font = ('Courier New',15,'bold'),text='Password Generator ^_^',fg = "blue")
ProgName.grid(row=1,column=3,padx=200,pady=30)

ChooseType = Label(window, font =('Courier New',15,'bold'),text="Choose a type among the 3.")
ChooseType.place(relx=.03, rely= .25)

Tchoice = StringVar()
NumChoice = Radiobutton(window, font =('corbel',10,'italic'),text = "Numeric",variable = Tchoice,value= num)
NumChoice.place(relx=.10, rely= .35)

AlphaNumChoice = Radiobutton(window, font =('corbel',10,'italic'),text = "Alpha Numeric",variable = Tchoice,value= alphanum)
AlphaNumChoice.place(relx=.10, rely= .4)

SpecialChoice = Radiobutton(window, font =('corbel',10,'italic'),text = "Special Alpha Numeric",variable = Tchoice,value= spalphanum)
SpecialChoice.place(relx=.10, rely= .45)

size = Label(window, text= "Size", font=('Copperplate Gothic',10,'bold'))
size.place(relx=.65 , rely = .35)

pass_length =Spinbox(window, from_=8, to = 100)
pass_length.place(relx=.73,rely=.35)
pass_length.config(state= "readonly")

GenButton = Button(window, text= "Generate", command = Create_Pass)
GenButton.place(relx=.45, rely= .55)

resultBox = Text(window, height = 6, width = 70)
resultBox.place(relx=.06 , rely=.7)


window.mainloop()