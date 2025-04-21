num1=float(input("digite o primeiro numero: "))
num2=float(input("digite o segundo numero: "))

operacao=input("escolha a operação (+,-,*,/): ")
if operacao=='+':
    resultado=num1+num2
elif operacao=='-':
    resultado=num1-num2
elif operacao=='*':
    resultado=num1*num2
elif operacao=='/':
    if num2 != 0:
        resultado=num1/num2
    else: 
        resultado="erro: divisão por zero não permitida"
else: 
    resultado="operação invalida. Escolha entre +,-,* ou /"

print ("resultado: ", resultado)
