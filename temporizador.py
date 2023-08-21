import time

print ("20 minutos = 1200 segundos")
t = input("Digite o tempo (em segundos): ")

if t.isdigit():
    t = int(t)
else:
    print('Tempo inválido')
    quit()

while t: 
  minutos, segundos = divmod(t, 60)
  timer = 'Tempo restante: {:02d}:{:02d}'.format(minutos, segundos)
  print(timer, end="\r")
  time.sleep(1)
  t = t - 1

print('O TEMPO ACABOU')

