from os import lseek
import re


def limpaEntrada(entrada):
    cleaned = re.sub(r'\n|</?i>', ' ', entrada[1])
    return (entrada[0], cleaned.strip())

def infoSplit(entrada):
    split = re.split(r'\s*;\s*')
    return (entrada[0], split, entrada[1])

def trataEntrada(element):
    list = re.split(r'</b>', element)
    if len(list) < 2:
        return
    else:
        head, tail = list
    entry = re.search(r'(\d+)\s*(.*?)\s+(\w+)', head)
    if entry:
        #print('id=' + entry[1] + ' ga=' + entry[2] + ' pos=' + entry[3])
        pass
    else:
        #print(list[0].strip())
        pass
    info = re.sub(r'\b(en|pt|es|la)\b', r'@\1', list[1])
    info = re.sub(r'((:?SIN|Nota|VAR|ID)\.-)', r'£\1', info)
    domain = re.split(r'\s{2,}|\t', re.search(r'[^@£]*', info))
    translations = re.findall(r'@(\w+)([^@£]*)', info)
    etc = re.findall(r'£(\w+)\.-([^@£]*)', info)
    #translations = [limpaEntrada(x) for x in translations]
    #translations = [infoSplit(x) for x in translations]
    #etc = [limpaEntrada(x) for x in etc]
    #etc = [infoSplit(x) for x in etc]
    print("§: ", domain)
    print("@: ", translations)
    print("£: ", etc)


# 1 - substituir até à pagina 20 e após a pag 544
# 2 - deitar fora bolds vazios
# 3 - texto com font=8 em principio sao todos iguais
# 4 - deitar fora as tags de text
# 5 - deitar fora as pages
with open('dataset.xml') as f:
    text = f.read()
    # Limpeza inicial
    text = re.sub(r'^(.|\n)*<page number="20"', '', text)
    text = re.sub(r'<page number="544"(.|\n)*$', '', text)
    text = re.sub(r'<[bi]>\s*</[bi]>', '', text)
    text = re.sub(
        r'<text top="862" left="320|4" width="(23)|(15)" height="18" font="8">.*?</text>', 
        '', 
        text
    )
    text = re.sub(r'<text.*?>', '', text) # *? -> 
    text = re.sub(r'</text>', '', text)
    text = re.sub(r'<page.*?>', '', text)
    text = re.sub(r'</page>', '', text)
    text = re.sub(r'V\nocabolario', '', text)
     
    # Tratemento de termo -> dic com id, ga, es, pt, en,
    for element in re.split("<b>", text):
        #print("Entrada:\n" + element)
        trataEntrada(element)
