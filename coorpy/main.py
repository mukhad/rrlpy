import sys

with open('calibr.txt', 'r',encoding='cp1251') as f:
    cont = f.readlines()

print("file encoding: ", f.encoding)
print("type(contents): ", type(cont))

print(cont)
print(len(cont))


with open('3c147.hst', 'r',encoding="866") as fhst:
    conthst = fhst.readlines()
print(conthst)
