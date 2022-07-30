from random import*
import sm3
import time

def Birthday_attack(n):
    for i in range(2**16):
        msg = "".join([choice("0123456789abcdef") for i in range(8)])
        cipher1=sm3.SM3("1141514f",sm3.IV)
        cipher2=sm3.SM3(msg,sm3.IV)
        if(cipher2[:int(n/4)]==cipher1[:int(n/4)]):    
            print('msg:',msg)
            print('plain:',cipher1)
            print('cipher:',cipher2)
            return
    print('Failed')
    

if __name__ == '__main__':
    start = time.time()
    Birthday_attack(16)
    end = time.time()
    time = end - start
    print('time:', time, 's')