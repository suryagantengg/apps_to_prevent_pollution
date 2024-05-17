import random

#x = int(input('masukan panjang sandi = '))
def gen_pass(pass_length):
    karakter="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    sandi=" "
    for i in range(pass_length):
        sandi += random.choice(karakter)
    print(sandi)
gen_pass(10)