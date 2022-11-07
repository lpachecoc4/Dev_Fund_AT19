import random 
import string

passwords = {}

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

def generate_pw(site):
    pw = pw_gen()
    password = (site,pw)
    passwords[site] = password
    print('New password for '+site+': '+pw)
    print('Password has been saved')

def get_pw(site):
    if passwords.get(site) != None :
        print(passwords.get(site))
    else:
        print("Password has not been created. Please create new password.")


while True:
    option = input("Write 1 to create new password, or write 2 to find a password already created. ")
    if option == "1":
        site = input('What is the website of the new password? ')
        generate_pw(site)
    elif option == "2":
        site = input('What is the name of the website? ')
        get_pw(site)
    else:
        print("Option not allowed.")