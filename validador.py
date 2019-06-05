
def validador(entrada):
    validadoresEntrada = ['[', '{', '(']
    pilha = []

    if type(entrada) != str:
        print(type(entrada))
        return False

    for c in entrada:
        if validadoresEntrada.__contains__(c):
            pilha.append(c)
            print(pilha)
        elif c == ']':
            if pilha[len(pilha) - 1] == '[':
                pilha.pop()
                print(pilha)
            else:
                return False
        elif c == '}':
            if pilha[len(pilha) - 1] == '{':
                pilha.pop()
                print(pilha)
            else:
                return False
        elif c == ')':
            if pilha[len(pilha) - 1] == '(':
                pilha.pop()
                print(pilha)
            else:
                return False
    
    if len(pilha) > 0:
        return False
    else: 
        return True

            
entrada = "{0011[2 () [] {}]}22([(())])"
print(validador(entrada))
