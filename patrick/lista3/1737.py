# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1737

quantidade_N = int(input())
soma = 0
if quantidade_N > 0:
    while quantidade_N > 0:
        x = float(input())
        soma = soma+x 
        quantidade_N = quantidade_N-1
    print("Soma dos números informados: %.2f" %soma)
else:
    print("Informe uma quantidade > 0!")
    
print("Fogo!")

