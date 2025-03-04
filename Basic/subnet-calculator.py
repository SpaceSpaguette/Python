'''mode import == import your custom IPv4 address
mode == gen generate unigue custom IPv4 address'''
import string

if input("Gen or import") == "Import":
    imported_adress = input("Enter your IPv4 address: ")
    mask = input("Enter your IPv4 mask: ")
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
