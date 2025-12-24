lista_preco = [1000, 3000, 2500, 4000, 5000]

#imposto
#aliquota1 IR = 0.2, se preco < 2000, acima disso e 0.3
#aliquota2 iSS = 0.15
#aliquota3 CSLL = 0.05

def calcular_imposto_total(preco):
    if preco <= 2000:
        imposto_ir = 0.2 * preco
    else:
        imposto_ir = 0.3 * preco
    imposto_iss = 0.15 * preco
    imposto_csll = 0.05 * preco
    imposto_total = imposto_ir + imposto_iss + imposto_csll
    return imposto_total
    return imposto_ir    

for preco in lista_preco: 
    imposto_total = calcular_imposto_total(preco)
    imposto_ir = calcular_imposto_total(preco)
    print(f'O imposto total sobre o produto de preco R${preco:.2f}: e R${imposto_total:.2f}')

nova_lista_precos = [2000, 1500, 3000, 4000, 500]
for preco in nova_lista_precos: 
    imposto_total = calcular_imposto_total(preco)
    imosto_ir = calcular_imposto_total(preco)
    print(f'O imposto total sobre o produto de preco R${preco:.2f}: e R${imposto_total:.2f}')