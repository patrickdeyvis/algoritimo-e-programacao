# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1759

anoAtual = int(input())
anoBase = 2005
salario = 1000
porc = 0.015
if anoAtual >= 2006 :
    while anoAtual > anoBase:
        salario = salario + (salario * porc)
        porc = porc + 0.010
        anoBase = anoBase + 1 
    print("Salário atual: R$%.2f" %(salario))
else:
    print("O ano informado deverá ser > 2005!")

