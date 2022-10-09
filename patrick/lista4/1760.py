# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1760

qtd_Npessoas = 0
soma_Idade = 0 
acima_Do_peso = 0
while qtd_Npessoas < 4 :
    I = int(input())
    K = float(input())
    soma_Idade = soma_Idade + I
    qtd_Npessoas = qtd_Npessoas + 1 
    if K >= 90 :
        acima_Do_peso = acima_Do_peso + 1 
i_Media = soma_Idade / 4

print("Qtd pessoas > 90 Kg: %i" %(acima_Do_peso))
print("Idade média: %.2f" %(i_Media))

