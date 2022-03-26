import re

f = open("out.txt")
content = f.read()
sections = []

blocks = re.findall(r'(@[^@]+)', content)

def dominio(texto):
    print(texto)
    if texto == "['']":
        return ''
    else:
        return r'\\subsection{Dominio: ' + texto + '}'

for block in blocks:
    section = ''
    if re.search(r'@1', block):
        #print(block)
        pass
    else:
        section += re.sub(r'@2\s(.+)', r'\\section{\1}', block)
        section = re.sub(r'[😷😀😎]\s\[\'?\'?\]\n', r'', section)
        section = re.sub(r'😷\s(.+)', r'\\subsection{Dominio: \1}', section)
        section = re.sub(r'😀',  r'\\subsection{Traduções}', section)
        print(section)
# \'pt|es|en|la\', 

latexHead = r'''
\documentclass{article}
\usepackage[portuges]{babel
\usepackage[utf8]{inputenc}

\parindent=0pt
\parskip=2pt

\title{Dicionário Médico }
\author{João Torres - PG47345
        \\ Universidade do Minho
        \and
        José Reis - PG47385
        \\ Universidade do Minho
 }
\date{ 22 de março de 2022 }
'''

f.close()
