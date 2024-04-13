saldo=0
user=0
ops=4
cont = 3
extrato=[saldo]
print(extrato)
while ops != 0:   
    print("="*10,"BANCO FAEL","="*10)
    print("""
    digite uma opção a baixo""")
    ops=int(input("""
    [ 1 ] Sacar
    [ 2 ] Depositar
    [ 3 ] Visualizar Extrato
    [ 0 ] Sair
    """))

    if ops == 1:       
        print("="*10,"SAQUE","="*10)
        if cont < 1 :
            print("limite maximo de de saque diario atingidos")
            
        else:
            print("seu saldo atual é de R$ {:.2f}".format(saldo))
            if saldo < 1 :
                print("saldo insuficiente para ser sacado")
            else:
                user=float(input("digite o valor a ser sacado \nR$ "))
                while user < 1:
                        print("é nescessario inserir um valor positivo")
                        user=float(input("digite novamente o valor a ser sacado \nR$ "))
                while user > 500:
                        print("saque maximo permitido é de R$ 500,00")
                        user=float(input("digite novamente o valor a ser sacado \nR$ "))
                if saldo>=user:
                    saldo-=user
                    saq=("\033[1;31m - {:.2f} \033[m".format(user))
                    extrato.append(saq)                
                    print("-")
                    print("saque realizado com sucesso")
                    cont-=1
                else:
                    print("saldo insuficiente para esse saque")
        
            
    elif ops == 2:
        user=float(input("digite o valor a ser depositado \nR$ "))
        if user <0:
            print("é nescessario inserir um valor positivo")
            user=float(input("digite novamente o valor a ser depositado \nR$ "))
            while user <0:
                print("é nescessario inserir um valor positivo")
                user=float(input("digite novamente o valor a ser depositado \nR$ "))        
        saldo+=user
        dep=("\033[1;32m + {:.2f} \033[m".format(user))
        extrato.append(dep) 
        print("deposito realizado com sucesso") 

    elif ops == 3:
        print("="*10,"EXTRATO","="*10)
        for c in range (len(extrato)):
            print(extrato[c])
        print("seu saldo atual é de R$ {:.2f}".format(saldo))

    elif ops == 0:
        print("obrigado! , volte sempre")
    else:
        print("opção invalida, tente novamente")        
        
        
            
            
