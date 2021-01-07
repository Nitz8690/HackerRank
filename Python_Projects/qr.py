import pyqrcode
from random import randint
value = randint(0,99)

def qrcode():
    q=pyqrcode.create(input("Enter the word or link which QR code you want to generate: \n"))
    q.png('qrcode'+ str(value) +'.png',scale=6)
    print('QR generated')

if __name__=='__main__':
    qrcode()
