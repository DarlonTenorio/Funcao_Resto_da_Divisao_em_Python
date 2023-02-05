dividendo = int(input("Informe o dividendo: "))
divisor = int(input("Informe o divisor: "))

def modulo(dividendo, divisor):
    return dividendo - (dividendo // divisor) * divisor

resto = modulo(dividendo, divisor)
print("O resto da divisão é:", resto)
