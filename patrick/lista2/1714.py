# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1714

P = float(input())
if P<20:
    print("Valor de venda: R$%.2f" %(P*0.45+P))
else:
    print("Valor de venda: R$%.2f" %(P*0.30+P))
