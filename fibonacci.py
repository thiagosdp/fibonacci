def repete_funcao(): # funcao criada para repetir a funcao de fibonacci, nome da funcao e "repete_funcao" e estamos utilizando funcao vazia.
    
    def fibonacci(limite): # definifimos o nome da funcao como "fibonacci", e parametro "limite" para chegar no elemento da sequencia fibonacci.
        x = int(input("\nDigite um número inteiro para somar com o segundo: ")) # quanto nesta sintaxe e na que ha abaixo, solicita ao usuario o primeiro numero que sera somado com o segundo que ha abaixo.
        y = int(input("\nDigite um número inteiro para somar com o primeiro: ")) # quanto nesta sintaxe e na que ha abaixo, solicita ao usuario o primeiro numero que sera somado com o segundo que ha abaixo.
        fibonacci_1 = [x,y] # foi criado um lista para armazenar a x e y que iniciaria a sequencia de fibonacci.
        for z in range(limite - 2): # neste laco de repeticao ha o limite informado ao usuario que sera controlado por z, ja que temos dois elemento x e y devemos reduzir aqui com - 2.
            fibonacci_1.append(fibonacci_1[-2] + fibonacci_1[-1]) # aqui adicionara com append a soma com elementos anterior com o seguinte, como a sequencia.
            print("\n",fibonacci_1) # nesse sintaxe mostrar toda soma ate o limite informado da sequencia.
            
        linha = int(input('\nDigite a linha que deseja mostra da sequência Fibonacci: ')) # o usuario ira informar qual elemento da sequencia que ele deseja imprimir.
        print('\nO elemento da linha é:',fibonacci_1[linha]) # aqui mostrará o elemento que esta armazenado na lista criada.

        armazena_valores = open("c:/users/acer/desktop/banco.txt","a") # foi criado um arquivo txt que sera armazenado tudo na frente dos outros dados.
        valores_texto = [] # esta lista armazenara todas informacoes que for adionada a ele.
        valores_texto_1 = """A sequência """ # foi armanenado o que ha dentro """ """.
        valores_texto_2 = """ e o elemento """ # foi armanenado o que ha dentro """ """.
        valores_texto_3 = (fibonacci_1[linha]) # foi armanenado o elemento que ha dentro da primeira lista criada.
        valores_texto.append(valores_texto_1) # foi adionado em valores_texto o texto que ha em valores_texto_1.
        valores_texto.append(str(fibonacci_1)) # foi adionado em valores_texto e transformado o valor int que ha fibonacci_1 em string.
        valores_texto.append(valores_texto_2) # foi adionado em valores_texto o texto que ha em valores_texto_2.
        valores_texto.append(str(valores_texto_3))# foi adionado em valores_texto e transformado o valor int que ha fibonacci_1 em string.
        armazena_valores.writelines(valores_texto) # nesta sintaxe sera escrito no  arquivo armazena_valores tudo que foi armazenado em valores_texto, foi necessario usar writelines para escrever todas linhas.
        armazena_valores.close() # o arquivo armazena_valores foi fechado e criado.
    
    limite = int(input("\nDigite a posição do número inteiro que deseja chegar (Fibonacci): ")) # o usuario ira informar o limite da sequencia.
    print(fibonacci(limite)) # nesta sintaxe vai chamar a funcao com o valor de limite armazenado.
    
    escolha = str(input("\nDeseja executar o código novamente? se não digite qualquer letra: ")) # o usuario devera informa se quer executar o codigo ou nao.
    while escolha == 'sim' or escolha == 's' or escolha == 'Sim' or escolha == 'SIm' or escolha == 'SIM': # todas condicoes que o usuario pode usar par continuar o codigo
        return repete_funcao() # se o usuario deseja continuar nessa sintaxe voltara a executar a funcao de fibonacci.
    print("\nThe end.") # informma que o codigo acabou.
repete_funcao() # chamada a funcao repete_funcao.
