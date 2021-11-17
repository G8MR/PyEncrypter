def encrypt(data):
    layer1 = """ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_-!@#'"$%^&*()"""
    en1_length = int(len(data))
    en1_data = ""
    for i in range(0,en1_length):
        x = int(layer1.index(data[i]))
        if x < 10:
            x = str(0)+str(x)
        en1_data = en1_data + str(x)
    return en1_data    

def decrypt(data):
    layer1 = """ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_-!@#'"$%^&*()"""
    decoded = ""
    data = str(data)
    y = 0
    for i in range(0, len(data)//2):
        x = layer1[int(str(data[y])+str(data[int(y)+1]))]
        decoded = str(decoded)+str(x)
        y += 2
    return decoded
    

x = encrypt("hiya!")
print(x)
y = decrypt(x)
print(y)