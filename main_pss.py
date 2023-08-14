from password_generator import *
from encrypt_decrypt import *
import mysql.connector

print("New User (enter 1 if you haven't used it before)\nOld user (enter 2 if you have already saved passwords in this manager)")
choice = int(input())

if choice == 1:
    print("Save your Password!\tWarning: If you have saved passwords in this already then it will all vanish by opting for this option, but if you are a new user, you can proceed\nProceed to save password? [y/n]")
    ch = input()
    while ch != 'y' and ch != 'n':
        print("Please enter correct choice, either 'y' or 'n'")
        ch = input()

    if ch == 'y':
        key=generate_key()
        iv=generate_IV()
        db = mysql.connector.connect(host="localhost", user="root", password="123", database="test")
        cur = db.cursor()
        t = (iv, key)  # Store IV along with the encrypted key
        s = """INSERT INTO t_encrypt (iv, data) VALUES (%s, %s)"""
        cur.execute(s, t)
        db.commit()
        db.close()
        print("Enter website")
        website=input()
        print("Enter username")
        username=input()
        print("Enter 1 write your password or enter 2 to generate strong password by us if you wish! you don't have to remember")
        resp = int(input())
        while resp!=1 and resp!=2:
            print("Please enter correct choice")
            resp = int(input())
            if resp == 1:
                pswrd = input("Enter your password")
                encryption(website,username,pswrd)
            elif resp==2:
                p = psswrd_gen()
                print(p)
                encryption(website,username,p)

        print("Password is saved successfully for the given website and username")
    elif ch == 'n':
        pass

elif choice == 2:
    print("Enter 1 to save your new password\nEnter 2 to generate a password\nEnter 3 to show your saved password\nEnter 4 to update your  password\nEnter 5 to delete a password from your saved passwords\nEnter 0 to stop")
    ch = int(input())
    while ch != 0:
        if ch == 1:
            # Implementation to save a new password
            print("Enter website")
            website=input()
            print("Enter username")
            username=input()
            print("Enter 1 to write your password or enter 2 to generate strong password by us if you wish! you don't have to remember")
            resp = int(input())
            while resp!=1 and resp!=2:
                print("Please enter correct choice")
                resp = int(input())
                if resp == 1:
                    pswrd = input("Enter your password")
                    encryption(website,username,pswrd)
                elif resp==2:
                    p = psswrd_gen()
                    print(p)
                    encryption(website,username,p)
        elif ch == 2:
            p = psswrd_gen()
            print(p)
        elif ch == 3:
            # Implementation to show password
            website = input("Enter the website for which you have to check: ")
            username = input("Enter the username for which you have to check: ")
            pasword = decryption(website,username)
            print(pasword)
            pass
        elif ch == 4:
            # Implementation to update password
            website = input("Enter the website for which you have to update: ")
            username = input("Enter the username for which you have to update: ")
            print("Enter 1 to write your password or enter 2 to generate strong password by us if you wish! you don't have to remember")
            resp = int(input())
            while resp!=1 and resp!=2:
                print("Please enter correct choice")
                resp = int(input())
                if resp == 1:
                    pswrd = input("Enter your password: ")
                    update(website,username,pswrd)
                elif resp==2:
                    p = psswrd_gen()
                    print(p)
                    update(website,username,p)
            pass
        elif ch == 5:
            # Implementation to delete password
            website = input("Enter the website for which you have to delete: ")
            username = input("Enter the username for which you have to delete: ")
            delete(website,username)
            print("password deleted for given website")
        else:
            print("Please enter a correct choice")
        ch = int(input())
