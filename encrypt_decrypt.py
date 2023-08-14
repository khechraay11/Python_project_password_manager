from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode
import mysql.connector


def generate_key():
    salt=get_random_bytes(32)
    password = "psswrd@08"
    key = PBKDF2(password, salt, 32)
    return key

# Generate a random initialization vector
def generate_IV():
    iv = get_random_bytes(AES.block_size)
    return iv

def encryption(website,username,pswrd):
    db = mysql.connector.connect(host="localhost", user="root", password="123", database="test")
    cur = db.cursor()
    q = """SELECT * FROM t_encrypt"""
    cur.execute(q)
    result = cur.fetchone()
    for rec in result:
        iv, key = rec
    cipher = AES.new(key, AES.MODE_CBC, iv)
    cipher_data = cipher.encrypt(pad(pswrd, AES.block_size))
    t = (website,username,cipher_data)
    s = """INSERT INTO t_data (website,username,psswrd) VALUES (%s, %s, %s)"""
    cur.execute(s, t)
    db.commit()
    cur.close()
    db.close()

def decryption(website,username):
    db = mysql.connector.connect(host="localhost", user="root", password="123", database="test")
    cur = db.cursor()
    q = """SELECT * FROM t_encrypt"""
    cur.execute(q)
    result = cur.fetchone()
    for rec in result:
        iv, key = rec

    t = (website,username)
    s = """SELECT psswrd FROM t_data where website = %s AND username = %s """
    cur.execute(s, t)
    result2 = cur.fetchone()
    for x in result2:
        cipher_data=x
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(cipher_data), AES.block_size)
    cur.close()
    db.close()
    return decrypted_data.decode('utf-8')

def delete(website,username):
    db = mysql.connector.connect(host="localhost", user="root", password="123", database="test")
    cur = db.cursor()
    t = (website,username)
    s="""DELETE FROM t_data WHERE website = %s AND username = %s"""
    cur.execute(s, t)
    db.commit()
    cur.close()
    db.close()

def update(website,username,pswrd):
    db = mysql.connector.connect(host="localhost", user="root", password="123", database="test")
    cur = db.cursor()
    q = """SELECT * FROM t_encrypt"""
    cur.execute(q)
    result = cur.fetchall()
    for rec in result:
        iv, key = rec
    cipher = AES.new(key, AES.MODE_CBC, iv)
    cipher_data = cipher.encrypt(pad(pswrd, AES.block_size))
    t = (cipher_data,website,username)
    s = """UPDATE t_data SET psswrd = %s WHERE website = %s AND username = %s """
    cur.execute(s, t)
    db.commit()
    cur.close()
    db.close()