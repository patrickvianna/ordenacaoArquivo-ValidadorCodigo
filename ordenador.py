def TryParseInt(elem):
    try:
        int(elem)
        return True
    except ValueError:
        return False

def TryParseFloat(elem):
    try:
        float(elem)
        return True
    except ValueError:
        return False

def IsNumber(elem):
    if TryParseInt(elem):
        return 1
    elif TryParseFloat(elem):
        return 2
    else:
        return 0

def ParseNumber(elem):
    if TryParseInt(elem):
        return int(elem)
    elif TryParseFloat(elem):
        return float(elem)
    else:
        raise ValueError('Os valores informados precisam ser do tipo int ou float.')

def ordenador():
    lista = []
    arquivo = open("paraOrdenar.txt") 

    linha = arquivo.readline()

    while(linha):
        linha = ParseNumber(linha)
        lista.append(linha)
        linha = arquivo.readline()

    arquivo.close()

    lista.sort()
    del lista[0:len(lista)-10]
    print(lista)

ordenador()

