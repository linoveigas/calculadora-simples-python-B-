num1=float(input("digite o primeiro numero: "))
num2=float(input("digite o segundo numero: "))

operacao=input("escolha a opera��o (+,-,*,/): ")
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
        resultado="erro: divis�o por zero n�o permitida"
else: 
    resultado="opera��o invalida. Escolha entre +,-,* ou /"

print ("resultado: ", resultado)
