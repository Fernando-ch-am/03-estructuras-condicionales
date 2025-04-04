#Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
#Definir la lista numeros_aleatorios 
#● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
#mediana es mayor que la moda.
#● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
#la mediana es menor que la moda.
#● Sin sesgo: cuando la media, la mediana y la moda son iguales.
from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
print(f"los numeros son: {numeros_aleatorios}")
moda=mode(numeros_aleatorios)
mediana=median(numeros_aleatorios)
media=mean(numeros_aleatorios)
if(media>mediana>moda):
    print("es sesgo positivo o a la derecha")
elif(media<mediana<moda):
    print("es sesgo negativo o a la izquierda")
elif(media==mediana==moda):
    print("sin sesgo")