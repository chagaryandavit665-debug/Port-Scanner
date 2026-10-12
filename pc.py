import socket

target_ip = input("Введите IP адрес целегого хоста (XXX.XXX.XXX.XXX):")
print("-------------------------------------------------")
port1 = int(input('Введи диапазон портов <<ОТ>>:'))
port2 = int(input('Введи диапазон портов <<ДО>>:'))
print("-------------------------------------------------")
print('Идет сканирование портов...')
n = 0
openports = []
for p in range(port1,port2 + 1):

    sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sckt.settimeout(30)  
    result = sckt.connect_ex((target_ip, p))

    if result == 0:
        openports.append(p)
        n+=1
        
    sckt.close() 

if n == 0:
    print(f"Все порты в диопазоне {port1}-{port2} закрыты!!")
else:
    print(f"Открыты порт(ы)-{openports}")
