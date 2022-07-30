from gmssl import sm3,func
import random
import time
def Birthday_Attack(num,length):
    ran1=hex(random.randint(0,pow(2,length*4)))[2:].zfill(length)
    ran11=bytes(ran1,encoding='utf-8')
    ran1_hash=sm3.sm3_hash(func.bytes_to_list(ran11))[:length]
    for j in range(num):
        ran2=hex(random.randint(0,pow(2,length*4)))[2:].zfill(length)
        ran22=bytes(ran2,encoding='utf-8')
        ran2_hash=sm3.sm3_hash(func.bytes_to_list(ran22))[:length]
        if ran1_hash==ran2_hash:
            if ran2!=ran1:
                print('success!')
                print('The same hash pair is:',ran1,'and ',ran2)
                return True
    print('fail!')
    return False


Birthday_Attack(pow(2,64),4)