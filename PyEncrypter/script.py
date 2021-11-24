class ObjInit:
    def __init__(self, data):
        self.layer1 = """ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_-!@#'"$%^&*()"""
    
    def encrypt(data):
        en1_length = int(len(data))
        en1_data = ""
        for i in range(0,en1_length):
            x = int(self.layer1.index(data[i]))
            if x < 10:
                x = str(0)+str(x)
            en1_data = en1_data + str(x)
        return en1_data    

    def decrypt(data):
        decoded = ""
        data = str(data)
        y = 0
        for i in range(0, len(data)//2):
            x = self.layer1[int(str(data[y])+str(data[int(y)+1]))]
            decoded = str(decoded)+str(x)
            y += 2
        return decoded
