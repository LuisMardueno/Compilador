import time

st = time.time()

sum_x = 0
for i in range(100000):
    sum_x += i

time.sleep(3)

print("SUma de un millon de numeros", sum_x)

et = time.time()

tiempoenlazado = et - st
print("Tiempo de ejecucion:", tiempoenlazado, 'segundos')