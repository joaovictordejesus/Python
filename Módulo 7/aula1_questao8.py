def calcular_digito(cpf, multiplicadores):
    soma = sum(int(cpf[i]) * multiplicadores[i] for i in range(len(multiplicadores)))
    resto = soma % 11
    return '0' if resto < 2 else str(11 - resto)

def validar_cpf():
    cpf = input("Digite o CPF (XXX.XXX.XXX-XX): ").replace('.', '').replace('-', '')
    if len(cpf) != 11:
        print("CPF inválido")
        return

    multiplicadores1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    multiplicadores2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

    primeiro_digito = calcular_digito(cpf[:9], multiplicadores1)
    segundo_digito = calcular_digito(cpf[:9] + primeiro_digito, multiplicadores2)

    if cpf[-2:] == primeiro_digito + segundo_digito:
        print("Válido")
    else:
        print("Inválido")

validar_cpf()