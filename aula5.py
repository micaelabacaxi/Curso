lista_vendas = [1000, 3000, 2500, 4000, 5000]
meta_venda = 1500
percentual = 0.2

if lista_vendas[1] > meta_venda:
    bonus = lista_vendas[1] * percentual
    print(f'BONUS DE VENDAS DE: {bonus:.2f} reais')
else: 
    print('SEM BONUS DE VENDAS')    





#para  cada item na lista_vendas
for venda in lista_vendas:
# igual a estrutura condicional if se tudo que esta indentado abaixo sera repetido inumeras vezes
# se nao estiver indentado nao faz parte do for e nao e repetido
    if venda >= meta_venda:
        bonus = percentual * venda
    else: 
        if venda < meta_venda:
            print("venda abaixo da meta, sem bonus")
    
    print(f"Parabens voce ganhou um bonus de R${bonus:.2f} reais")



    faturamento = input("Qual o os seus faturamentos mensais? ")
faturamento =  faturamento.split(",")

meta = 2000

for lucro in faturamento: 
    lucro = int(lucro.strip())
    if lucro >= meta:
        print(f"Parabéns! Você bateu a meta com um faturamento de R${lucro:.2f}")
    else:
        if lucro < meta:
            print(f"Infelizmente você não bateu a meta. Seu faturamento foi de R${lucro:.2f}")