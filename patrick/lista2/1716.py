# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1716

plano = input("")

salário_atual = float(input())

if plano=="A":
    print("Novo salário: R$%.2f" %(salário_atual+salário_atual*0.10))
elif plano=="B":
    print("Novo salário: R$%.2f" %(salário_atual+salário_atual*0.15))
elif plano=="C":
    print("Novo salário: R$%.2f" %(salário_atual+salário_atual*0.20))

