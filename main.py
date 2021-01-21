import numpy as np
def password(s):
    ALPHA_LIST=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    alpha_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    num_list=['0','1','2','3','4','5','6','7','8','9']
    symbols=['*','$','#','-']
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
    