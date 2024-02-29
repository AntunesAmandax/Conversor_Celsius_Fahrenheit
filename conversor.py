print("Bem-vindo ao conversor de escalas Celsius/Fahrenheit!")
res = input("Qual a unidade de medida que será convertida, Celsius ou Fahrenheit?")

if res.lower() == "fahrenheit":
 f = float(input("Escreva aqui o grau Farenheit: "))
 celcius = ((5/9)*(f-32))
 print("O resultado é " + str(celcius)+ " ºC")
elif res.lower() == "celsius":
 c = float(input("Escreva aqui o grau Celsius: "))
 fahrenheit = (c*(9/5)+32)
 print("O resultado é "+ str(fahrenheit)+ " ºF")
else:
 print("Escolha inválida. Por favor, escolha 'fahrenheit' ou 'celsius'.")