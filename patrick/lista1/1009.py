# https://www.beecrowd.com.br/judge/pt/problems/view/1009

Nome = input("")

Salario = float(input(""))

Vendas = float(input(""))

TOTAL = (Vendas * 15 / 100) + Salario

print("TOTAL = R$ %.2f" %(TOTAL))
