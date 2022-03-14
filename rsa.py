import time
print("введите 2 простых числа")
p = int(input())
q = int(input())
n = p * q
fi = (p - 1) * (q - 1)
lista = []
 
def eratosthenes(fi):                                      # функция возвращает список с простыми числами от 2 до fi
    sieve = list(range(fi + 1))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    return [value for value in sieve if value
            != 0]
 
for i in range(1, int(fi / 2) + 1):                         #цикл для нахождения множителей
    if fi % i == 0:
        lista.append(i)
 
def e (lista,eratosthenes):                                 #функция для удаления общий множителей
    sravnenie=list(set(lista) & set(eratosthenes))
    for i in sravnenie:
        eratosthenes.remove(i)
    return eratosthenes[0]
 
print("открытый ключ: ", n,e(lista,eratosthenes(fi)))
 
for i in range(1,10000):                                    #цикл для подбора d
        if (int(i)*e(lista, eratosthenes(fi)))%fi==1:
                    d=i
                    print("личный ключ = " ,n,i)
                    break
 
print("введите чилса/число которое хотите зашифровать")
val = int(input())
 
def encrypt(val,e,n):
    cypher=val**e%n
    return (cypher)
z=encrypt(val,e(lista, eratosthenes(fi)),n)             #зашифрованное сообщение
print("Сообщение в зашифрованном виде",z)
print("произошла дешифровка")
 
def decrypt(d,n,z):
    decr=z**d%n
    return (decr)
print(decrypt(d,n,z))
time.sleep(10)