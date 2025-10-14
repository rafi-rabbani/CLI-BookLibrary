import string 
import random

def str_random(panjang: int) -> str:
    kode = ''.join(random.choice(string.ascii_letters) for i in range(panjang))
    return kode