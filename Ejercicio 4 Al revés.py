from posixpath import split
from tkinter import N


frase = input('Introdusca una frase: ')
num = list(frase)
for i in num[::-1]:
    print(i)