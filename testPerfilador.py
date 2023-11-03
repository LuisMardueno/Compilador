import time
import cProfile
import pstats
st = time.time()
def add(x,y):
    resultado = 0
    resultado += x
    resultado += y
    return resultado

def fact(n):
    resultado = 1
    for i in range(1,n+1):
        resultado *= i
    return resultado

def mas_cosas():
    resultado = []
    for x in range(1000000):
        resultado.append(x ** 2)
#Si consideramos la cantidad de tiempo que utiliza para imprimir cada elemento
#Tenemos que evaluar si es nesecario cada impresion del elemento ya que en el perfilador es la funcion que mas tiempo utiliza
#Para demostracion quitar o agregar [-1] "Ultimo elemento de la lista" del return de la linea de abajo
    return resultado[-1]

def perder_tiempo():
    time.sleep(1)
    print("Perdiendo tiempo")

if __name__ == "__main__":
    with cProfile.Profile() as profile:
        print(add(100, 5000))
        print(fact(70))
        st = time.time()
        print(mas_cosas())
        et = time.time()
        tiempoenlazado = et - st
        print("Tiempo de ejecucion:", tiempoenlazado, 'segundos')
        perder_tiempo()
    
    resultados = pstats.Stats(profile)
    resultados.sort_stats(pstats.SortKey.TIME)
    resultados.print_stats()
    resultados.dump_stats("resultados.log")