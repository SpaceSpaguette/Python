buffer =""
maxlength = 4

for y in range(16**maxlength):
    random = hex(y)
    for x in range(4-len(str(random[2:]))):
        buffer += "0"
    buffer += random[2:]
    print(buffer)
    buffer = ""
    print(y)
#Loop ends here
