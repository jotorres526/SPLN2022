import re
from xml import dom

with open("medicina.xml") as f:
    entries = dict()
    content = f.read()

# remover elementos vazios
content = re.sub(r"<(\w+)>\s+</\1>", "", content)

# remover páginas desnecessárias
content = re.sub(
    r".*<page number=\"20\" [^>]*>", "", content, flags=re.S, count=1)
content = re.sub(r"<page number=\"544\".*", "", content, flags=re.S, count=1)

content = re.sub(r'<text top=\"862\"[^>]*>.*?</text>', "", content)

content = re.sub(r"<text[^>]*>(.*?)</text>", r"\1", content, flags=re.S)

content = re.sub(r"<page[^>]*>", "", content)
content = re.sub(r"</page>", "", content)
content = re.sub(r"<fontspec[^>]*>", "", content)

content = re.sub(r"\n[ \t]*\n", "\n", content)
content = re.sub(r"V\nocabulario", "", content)


def clean(dirty_text):
    return re.sub(r"\n|</?i>", " ", dirty_text).strip()


def info_split(info):
    return re.split(r"\s*;\s*", info)


def processEntry(entry: str):
    entrada = dict()
    c = re.split(r'</b>', entry, maxsplit=1)
    m = re.fullmatch("\s*(\d+)\s*(.*?)\s*(\w+)", c[0])
    id = ''
    if m:
        #print("@1", m.groups())
        id = m.group(2)
        entrada['pos'] = m.group(3)
        entrada['id'] = m.group(1)
    else:
        id = c[0].strip()
        #print("@2", id)
        
    info = re.sub(r"\b(en|pt|es|la)\b", r"😀\1", c[1])
    info = re.sub(r"((?:SIN|Nota|VAR|Vid)\.-)", r"😎\1", info)

    domain = re.split(r"\s{2,}|\t", clean(
        re.search(r"[^😀😎]*", info)[0].strip()))
    trads = [(x[0], info_split(clean(x[1])))
             for x in re.findall(r"😀(\w+)([^😀😎]*)", info)]
    etc = [(x[0], info_split(clean(x[1])))
           for x in re.findall(r"😎(\w+)\.-([^😀😎]*)", info)]
    
    entrada['dominio'] = domain
    entrada['traducoes'] = trads
    entrada['etc'] = etc
    entries[id] = entrada


for entry in re.split(r'<b>', content)[1:]:
    processEntry(entry)


latexBody = ''

for entry in entries:
    latexBody += '\section{' + entry + '}\n'
    
    
print(latexBody)