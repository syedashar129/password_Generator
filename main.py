## generates strong random passwords
import random

numOfPass = int(input('How many passwords do you want : '))
Length = int(input('How long do you want your password to be : '))


chars = 'abcdefghijklmnopqrstuvwxyz!@#$%^&*_+'


for pwd in range(numOfPass):
    password = ''
    for y in range(Length):
        password += random.choice(chars)

    print(str(pwd + 1) + '. ' + password)