def ImcCalculadora(Peso, AlturaEnMt):
    imc = Peso / (AlturaEnMt * AlturaEnMt)
    return imc

Peso = float(input("Ingrese su peso en kg"))
alturaEnCm = int(input("Ingrese su altura en cm"))
AlturaEnMt = alturaEnCm / 100

imc = ImcCalculadora(Peso, AlturaEnMt)

print("su IMC es de "+ str(imc))

if imc < 20:
    print("Esta delgado")
if imc >= 20 and imc < 26:
    print("Tiene un peso normal")
if imc >= 26 and imc < 30:
    print("Tiene sobrepeso")
if imc >= 30:
    print("Esta obeso")
    
print("HOLA MUNDO ANDO PROBADNDO GIT ESTA BUENO")