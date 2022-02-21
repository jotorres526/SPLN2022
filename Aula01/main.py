import re
# Perguntar o nome ao utilizador e escreve no stdout em maiúsculas
#nome = input("Introduzir nome: ")
#nome = nome.upper()
#print(nome)

# Função que recebe array de num e imprime apenas os pares
def pares(list):
    return [x for x in list if x % 2 == 0]

# Funçao que recebe o nome de um ficheiro e imprime as linhas de forma inversa
def inverteLinhas(file):
    with open(file) as f:
        lines = f.readlines()
        return lines[::-1]

print(''.join(inverteLinhas('hmm.txt')))

def lineFormat(line):
    line = re.sub(r'(\.+|[.,!?;:])', r' \1 ', line)
    acentos = {
        'ã': 'a',
        'í': 'i',
        'ç': 'c'
    }
    #line = ''.join([acentos.get(letra, letra) for letra in line])
    return line
    
# Separar palavras de pontuação com espaço, converter para maiuscula, remover pontuação
def fileFormat(file):
    with open(file) as f:
        lines = f.readlines()
        formattedLines = []
        for line in lines:
            formattedLines.append(lineFormat(line))
        return formattedLines        

# Recebe nome de ficheiro e imprime o numero de ocorrencias das 10 palavras mais frequentes
def mostCommon(file):
    with open(file) as f:
        
# Pegar dataset xml no git e extrair todos os nomes, no fim ordenar por num de ocorrencia de nomes completos e alfabeticamente