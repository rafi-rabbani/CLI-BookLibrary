import string 
import random

def str_random(panjang: int) -> str:
    stringnya = ''.join(random.choice(string.ascii_letters) for i in range(6))
    return stringnya