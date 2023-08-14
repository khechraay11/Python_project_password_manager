import secrets
import random
def psswrd_gen():
    u_case_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    l_case_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    digits = ['0','1','2','3','4','5','6','7','8','9']
    special_char = ['!','@','#','$','%','^','&','*']
    psw_list = u_case_list + l_case_list + digits + special_char
    random.shuffle(psw_list)
    length = random.randint(8,11)
    password_list =[]
    for count in range(0,length + 1):
        password_list.append(secrets.choice(psw_list))
        random.shuffle(psw_list)
    req = True
    number = 0
    ualpha = 0
    lalpha = 0
    spec_char = 0
    while req:
        for str in password_list:
            if ord(str) >=65 and ord(str) <=90:
                ualpha+=1
            elif ord(str) >=97 and ord(str) <=122:
                lalpha+=1 
            elif ord(str) >=48 and ord(str) <=57:
                number+=1
            else:
                spec_char+=1
        if ualpha!=0 and lalpha!=0 and number !=0 and spec_char !=0:
            req =False
        else:
            if ualpha == 0:
                password_list[random.randint(0,len(password_list)-1)] = secrets.choice(u_case_list)
            elif lalpha == 0:
                password_list[random.randint(0,len(password_list)-1)] = secrets.choice(l_case_list)
            elif number == 0:
                password_list[random.randint(0,len(password_list)-1)] = secrets.choice(digits)
            elif spec_char ==0:
                password_list[random.randint(0,len(password_list)-1)] = secrets.choice(special_char)

    password = ""
    for  s in password_list:
        password += s             

    return password
#psswrd_gen()