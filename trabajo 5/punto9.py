#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#resultado usando la función.
def celsius_a_fahrenheit(celsius): #°F = (°C × 9/5) + 32 
    return print(f"{celsius}° grados celcius son: {(celsius * 9 / 5) + 32}° fahrenheit")

celsius=int(input("ingrese una tempertura en celsius: "))
celsius_a_fahrenheit(celsius)