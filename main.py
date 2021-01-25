import numpy as np
from tkinter import *
from tkinter.messagebox import *


root=Tk()
root.title("Random Password Generator")
root.geometry("550x400+400+250")


def password():
    try:
        s=int(entLength.get())
        if s<=0:
            showerror("Wrong input","password length must be > 0")
        else:
            ALPHA_LIST=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
            alpha_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
            num_list=['0','1','2','3','4','5','6','7','8','9']
            symbols=['*','!','#','@']

            st=""
            while len(st)<=s:
                s1=ALPHA_LIST[np.random.randint(0,len(ALPHA_LIST))]
                st=st+s1
                if len(st)==s:
                    break
                s2=alpha_list[np.random.randint(0,len(alpha_list))]
                st=st+s2
                if len(st)==s:
                    break
                s3=num_list[np.random.randint(0,len(num_list))]
                st=st+s3
                if len(st)==s:
                    break
                s4=symbols[np.random.randint(0,len(symbols))]
                st=st+s4
                if len(st)==s:
                    break
            showinfo("Random Generated Password: ",st)   
    
    except:
        showerror("Wrong input","only integers allowed")
        
    finally:
        entLength.delete(0,END)
        entLength.focus()



lblText=Label(root,text="Enter the password length required:",font=("Georgia",13,"bold italic"))
entLength=Entry(root,bd=4,font=("Arial",15,"bold italic"))
btnGenerate=Button(root,text="Generate",font=("Georgia",10,""),command=password)
lblReminder=Label(root,text="NOTE: Minimum password length should be of 10 or more characters",font=("Arial",10,"bold italic"))
lblHead=Label(root,text="Generated Password consists of random : ",font=("Georgia",12,""))
lblHead1=Label(root,text="- lowercase and uppercase letters",font=("Georgia",12,""))
lblHead2=Label(root,text="- digits and special symbols like: *, ! , # , @",font=("Georgia",12,""))
lblLast=Label(root,text="* Kindly note the password once generated",font=("times new roman",15,"bold"))
lblText.pack(pady=20)
entLength.pack(pady=15)
btnGenerate.pack(pady=15)
lblReminder.pack(pady=20)
lblHead.place(x=10,y=240)
lblHead1.place(x=10,y=270)
lblHead2.place(x=10,y=300)
lblLast.place(x=10,y=350)


root.mainloop()