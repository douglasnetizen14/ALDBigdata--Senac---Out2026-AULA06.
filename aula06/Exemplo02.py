valor = float(input("valor da venda:  "))

print('''
[1]- pix  - (12% de desconto)
[2]- debito  - (8% de desconto)
[3] credito  - (5% de desconto)
[4] - din   - (15% de desconto)

''')

desconto = 0 
opcao =  int(input("ops escolhida:   "))

match opcao:
    case 1:
        print('pix')
        desconto = valor *0.12
    
    case  2:
         print('debito')
         desconto = valor *0.08

    case  3:
        print('credito')
        desconto = valor *0.05

    case  4:
            print('din')
            desconto = valor *0.15

if operação == True:
# if desconto != 0:
#     
     valor_final = valor - desconto
     print(f'preço:  {valor}')
     print(f'desconto:  {desconto}')
     print(f'total a pagar:  {valor_final}')

else:
     print('pfr, outra ops') 



        

  
 
