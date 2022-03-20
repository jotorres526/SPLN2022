from os import lseek
import re


# Entrada:
#  5393  zume pancreático      m < /b >


# <i > Fisioloxía < /i >

# es
# <i > jugo pancreático < /i >

# en
# <i > pancreatic juice < /i >

# pt
# <i > suco pancreático < /i >

def trataEntrada(element):
    list = re.split(r'</b>', element)
    if len(list) < 2:
        return
    else:
        head, tail = list
    id = re.match(r'(\d+)\s*(.*?)\s+(\w+)$', head)
    if id:
        #print('id=' + id[1] + ' ga=' + id[2] + ' pos=' + id[3])
        pass


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
        print("Entrada:\n" + element)
        trataEntrada(element)
