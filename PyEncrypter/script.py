import random

class ObjInit:
    def __init__():
        pass

    def decrypt(data):
        findata = decrypt_1(data)
        return findata

    def encrypt(data):
        finaldata = encrypt_1(data)
        return finaldata

charset = """ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_-!@#'"$%^&*()/?.,<>{[}]\|+=`~¦:;¬£€§®©℗ĀāǍǎĂăÁáÂâÃãÀàÄäÅåĄąÆæɐʙĆćɑɒɓɔĊċČčĐđÇçĎďɗɖĈĉÐðʤʣĒēĚěĔĕÉéÊêĖėęĘëËèÈɜʚɘɞɛəɠĞĜĢġĠʩɚɝĝɣɦʜɪɥĥĤɤğģʯĦħɧɩĭĬǐǏīĪÍÌìíÎÏïîĨİıĩĮįɨɫĴĵĸʞķĶʝɟĳĲĽľʟʪĹĺĻļɭɮĿŀŁłɬʫÑñɱɰŃńŅņŋŊňŇŉɯṆṅŌōǑǒɳɴÓóÔôöÖòÒɲŎŏØøɸɹɺʠœŒõÕŐőɵɷɶʃʁʀɻŕŔŘřɼɽſßŖŗɾɿʅʂŧŦşŞśŚŠšŢţþÞʦʧʨŝŜŪūǓǔŬŭũ"""


def encrypt_1(data):
    len_data = int(len(data))
    data_en1 = ""
    for i in range(len_data):
        enchar = data[i]
        rawpos = charset.find(enchar)
        if len(str(rawpos)) == 1:
            finalpos = "00"+str(rawpos)
        elif len(str(rawpos)) == 2:
            finalpos = "0"+str(rawpos)
        else:
            finalpos = rawpos
        data_en1 += str(finalpos)
    data_en1 = str(9) + data_en1
    finaldata = encrypt_2(data_en1)
    return finaldata

def encrypt_2(data):
    len_data = int(len(data))
    divnum = str(9) * int(len_data//2)
    rem = int(data) % int(divnum)
    divdata = int(data) - int(rem)
    quotient = str(int(divdata) // int(divnum))
    if len(str(quotient)) < 2:
        quotient = str(0) + str(quotient)
    divlen = str(len(divnum))
    remlen = str(len(str(rem)))
    if len(divlen) == 1:
        divlen = str(000) + str(divlen)
    if len(remlen) == 1:
        remlen = str(000) + str(remlen)
    data_en2 = str(quotient) + str(rem) + str(remlen) + str(divlen)
    finaldata = encrypt_3(data_en2)
    return finaldata

def encrypt_3(data):
    keylist = ["spEDtYPR12", "sPONgeb0B9", "uNdERwATer", "poTterhEaD", "gRgEnotFOUND", "volkswagen", "YoUTuBe925", "%8ms7up(39"]
    en3_support = random.choice(keylist)
    data_en3 = ""
    for i in range(len(data)):
        num = data[i]
        data_en3 += en3_support[int(num)]
    data_en3 = str(keylist.index(en3_support)) + data_en3
    return data_en3

def decrypt_1(data):
    final_de1 = ""
    keylist = ["spEDtYPR12", "sPONgeb0B9", "uNdERwATer", "poTterhEaD", "gRgEnotFOUND", "volkswagen", "YoUTuBe925", "%8ms7up(39"]
    keyval = int(data[0])
    key = keylist[keyval]
    for i in range(1, len(data)):
        dechar = data[i]
        dechar2 = key.find(dechar)
        final_de1 = final_de1 + str(dechar2)
    finaldata = decrypt_2(final_de1)
    return finaldata

def decrypt_2(data):
    len = data[-2:]
    remlen = data[-4:-2]
    data_rev = str(data).replace(str(len), "")
    data_rev = str(data_rev).replace(str(remlen), "")
    ninenum = str(9) * int(len)
    remlen = int(remlen)
    remlen -= remlen * 2
    rem = data_rev[remlen:]
    quo = str(data_rev).replace(rem, "")
    final_de2 = (int(quo) * int(ninenum)) + int(rem)
    finaldata = decrypt_3(final_de2)
    return finaldata

def decrypt_3(data):
    de3_rawdata = str(data).replace("9", "")
    len_data = int(len(str(de3_rawdata)))
    de3_count = len_data
    de3_count -= de3_count * 2
    de3_count2 = de3_count
    de3_count += 3
    data_de3 = ""
    for i in range(len_data//3):
        if de3_count == 0:
            dechar = de3_rawdata[de3_count2 : ]
        else:
            dechar = str(de3_rawdata)[de3_count2 : de3_count]
        char = charset[int(dechar)]
        data_de3 += char
        de3_count2 = de3_count
        de3_count += 3
    return data_de3