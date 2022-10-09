# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1733

nome = input("")
quantidade_H_extra = float(input())

salario_Minimo = 1192.40
valor_H_extra = 10.00

salario_H_extra = quantidade_H_extra*valor_H_extra
salario_Bruto = 3*salario_Minimo+salario_H_extra

desconto_Inss = salario_Bruto*0.12 if salario_Bruto > 2.000 else salario_Bruto*0.05
desconto_Imposto_de_renda = salario_Bruto*0.20 if salario_Bruto > 2.500 else salario_Bruto
salario_Liquido = salario_Bruto-desconto_Inss-desconto_Imposto_de_renda

print("Nome: %s"%(nome));
print("Salário bruto: R$%.2f"%(salario_Bruto))
print("Salário líquido: R$%.2f"%(salario_Liquido))

