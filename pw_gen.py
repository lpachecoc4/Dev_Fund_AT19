import random 
import string

def pw_gen():
    len = random.randint(9,16)
    min_letters = string.ascii_lowercase
    upp_letters = string.ascii_uppercase
    nums = '0123456789'
    all_chars = min_letters + upp_letters + nums
    password = random.choice(min_letters) + random.choice(upp_letters) + random.choice(nums)
    pw = ''.join(random.choice(all_chars) for i in range(len-3))
    password = pw + password
    return password


x = pw_gen()
print(x)