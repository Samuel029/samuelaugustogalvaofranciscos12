class conversor_medidas:
    def __init__(self) -> None:
        pass

def cm_para_metros(cm):
    metros = cm / 100
    return metros

def metros_para_cm(metros):
    cm = metros * 100
    return cm

print("Selecione a opção de conversão:")
print("1. Centímetros para Metros")
print("2. Metros para Centímetros")

opcao = input("Digite sua opção (1 ou 2): ")

if opcao == '1':
    cm = float(input("Digite o comprimento em centímetros: "))
    resultado = cm_para_metros(cm)
    print("O comprimento em metros é:", resultado, "m")
    
elif opcao == '2':
    metros = float(input("Digite o comprimento em metros: "))
    resultado = metros_para_cm(metros)
    print("O comprimento em centímetros é:", resultado, "cm")

else:
    print("Opção inválida. Por favor, escolha 1 ou 2.")