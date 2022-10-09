# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1761

valor = 1
valorTotal_produtos = 0
while valor != 0 :
    valor_produtos = float(input())
    if valor_produtos == 0 :
        valor = 0
        valorRecebido = float(input())
        troco = valorRecebido - valorTotal_produtos
    valorTotal_produtos = valorTotal_produtos + valor_produtos
    
print("Total da compra: R$%.2f" %(valorTotal_produtos))
print("Valor pago: R$%.2f" %(valorRecebido))
print("Troco: R$%.2f" %(troco))

