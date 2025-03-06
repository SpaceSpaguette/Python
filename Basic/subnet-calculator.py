'''mode import == import your custom IPv4 address
mode == gen generate unigue custom IPv4 address'''
import string
l = 1
if l == 1:
    imported_adress = "10.10.10"
    #mask = input("Enter your IPv4 mask: ")
    #Conver adress to list
    adress = []
    buffer = ""
    for x in range(len(imported_adress)):
        if imported_adress[x] == ".":
            print(imported_adress[x])
        else:
            buffer += imported_adress[x]
    adress.append(bin(int(buffer))[2:])
print(buffer)
print(adress)
print(x)