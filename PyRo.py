import os

import requests

import time

import sys

import urllib

vreq = requests.get('https://proud-quickest-dungeon.glitch.me/')

localversion = '0.5'

currentversion = vreq.text

def updatenotice():
    print('Out Of Date, Please Update')

    print(f'Local Version: {localversion}')

    print(f'Available Version: {currentversion}')

    print('The Program Will Now Exit!')

    time.sleep(5)

    sys.exit()

if currentversion != localversion:
                              updatenotice()

else:
    print('You Are All Up To Date! Continuing With Start Up!')


def search(mminput):
    sreq = requests.get()


    
print('Welcome To PyNsrLib! A Open Source Library For Python Projects!')

print(f'PyNsrLib Version: {localversion}')

mminput = input('What Catagory Of Project Would You Like To Look For?')


