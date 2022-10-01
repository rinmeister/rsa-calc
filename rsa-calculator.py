#!/usr/bin/env python3

from math import gcd as gcd
from os import system, name
from random import randrange
from colorama import Fore, Style

'''gcd kan bepalen of twee integers co-primes zijn. Hij kijkt naar de modulo
als deze op 1 uitkomt dan is het getal door niets anders deelbaar en zijn
de twee integers dus co-primes'''

#Prime keys are given:
p = 17
q = 23
string_value = ''

#calculate neccessary variables for RSA:
n = p * q
z = (p-1)*(q-1)


def calcPublicKey(n):

    #randrange kan een random nummer uit een range halen. Bijvoorbeeld 
    #randrange(10)
    #haalt een waarde tussen 0 en 9.
    e = randrange(n)

    #De while zoekt net zolang naar een integer waarde e die een co-prime is 
    #van z. Als dat zo is dan stopt de loop.
    while gcd(e,z) != 1:
        e = randrange(n)

    print('public key is {},{}'.format(n,e))
    return(e)

def calcPrivateKey(e,z):
    ''' Berekenen van de private key.
    d moet een waarde zijn waarbij geldt dat (e*d) - 1 deelbaar moet zijn door
    z en waarbij er geen restwaarde is. Oftewel de waarde e*d -1 mod z is 0
    Om d te bepalen moet e*d in ieder geval al groter zijn dan z. De minimale 
    waarde van d is z/e afgerond op een heel getal. '''

    d  = randrange(round(z/e),500)
    while (((e*d)-1)%z != 0):
        d  = randrange(round(z/e),500)

    print('private key is {},{}'.format(n,d))
    return(d)

if __name__ == "__main__":
    #clear the screen. Different commands depending on OS.
    if name == 'posix':
        _ = system('clear')
    else:
        _ = system('cls')
    
    #calculate the public and private keys
    e = calcPublicKey(n)
    d = calcPrivateKey(e,z)
    text = input(Fore.GREEN + "Voer een woord in om te encrypten: ")
    ascii_values = []
    for character in text:
        ascii_values.append(ord(character))

    #Encryption
    cipher_values=[]
    for ascii in ascii_values:
        cipher_values.append(pow(ascii, e, n))
    print(f'{Style.RESET_ALL}encrypt met public key {n},{e} geeft: {Fore.RED}{cipher_values}{Style.RESET_ALL}')
    #decryption
    decrypted_values = []
    for cipher in cipher_values:
        decrypted_values.append(pow(cipher, d, n))

    #write to character
    for character in decrypted_values:
        string_value = '{}{}'.format(string_value, chr(character))

    print(f'decrypt met private key {n},{d} geeft: {Fore.GREEN}{string_value}{Style.RESET_ALL}')
