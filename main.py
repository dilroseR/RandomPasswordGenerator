import numpy as np
from tkinter import *

root=Tk()
root.title("Random Password Generator")
root.geometry("550x400+400+250")
lblText=Label(root,text="Enter the password length required:",font=("Georgia",13,"bold italic"))
entLength=Entry(root,bd=4,font=("Arial",15,"bold italic"))
lblReminder=Label(root,text="NOTE: Minimum password length should be of 10 or more characters",font=("Georgia",10,"bold italic"))
lblHead=Label(root,text="Generated Password consists of random : ",font=("Georgia",12,""))
lblHead1=Label(root,text="- lowercase and uppercase letters",font=("Georgia",12,""))
lblHead2=Label(root,text="- digits and special symbols like: *, ! , # , @",font=("Georgia",12,""))
lblText.pack(pady=20)
entLength.pack(pady=15)
lblReminder.pack(pady=20)
lblHead.place(x=10,y=200)
lblHead1.place(x=10,y=230)
lblHead2.place(x=10,y=260)

"""
def password(s):
    ALPHA_LIST=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    alpha_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    num_list=['0','1','2','3','4','5','6','7','8','9']
    symbols=['*','!','#','@']
    if s==10:
        st=""
        while len(st)<=10:
            s1=ALPHA_LIST[np.random.randint(0,len(ALPHA_LIST))]
            st=st+s1
            s2=alpha_list[np.random.randint(0,len(alpha_list))]
            st=st+s2
            if len(st)==10:
                break
            s3=num_list[np.random.randint(0,len(num_list))]
            st=st+s3
            s4=symbols[np.random.randint(0,len(symbols))]
            st=st+s4
            
    return st


m=int(input())
ans=password(m)
print(ans)
"""
root.mainloop()