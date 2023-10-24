a = (input('Digite o valor atual do salário'))
b = (input('Digite o valor da porcentagem de reajuste'))

calculoDeReajuste = ((float(b)/100)*float(a))
CalculoDeSalario = (float(a)+float(calculoDeReajuste))

print(float(calculoDeReajuste))
print(float(CalculoDeSalario))