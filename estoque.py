produto = 'café'
estoque = 56
venda=int(input('Venda: '))
if venda<=estoque:
    estoque-=venda
    print('estoque:',estoque)
else:
    print('Sem estoque')