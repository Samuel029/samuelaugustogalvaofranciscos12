from temperatura import conversor_temperatura
from convnversordemedidas import conversor_medidas

print("Selecione a opção de conversão\n"
      "1. Centímetros para Metros\n"
      "2. Metros para Centímetros\n"
      "3. Celsius para Fahrenheit\n"
      "4. Fahrenheit para Celsius")

opcao = input("Digite sua opção: ")

if opcao == '1':
    cm = float(input("Digite o comprimento em centímetros: "))
    resultado = conversor_medidas.cm_para_metros(cm)
    print("O comprimento em metros é:", resultado, "m")
    
elif opcao == '2':
    metros = float(input("Digite o comprimento em metros: "))
    resultado = conversor_medidas.metros_para_cm(metros)
    print("O comprimento em centímetros é:", resultado, "cm")

elif opcao == '3':
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = conversor_temperatura.celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C é igual a {fahrenheit:2f}°F")
elif opcao == '4':
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        celsius = conversor_temperatura.fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F é igual a {celsius:.2f}°C")

else:
    print("Opção inválida. Por favor, escolha 1 ou 2.")