import re
import collections
from typing import Collection

with open("ABM_807.txt", encoding="UTF-8") as f:
    result = {}
    lines = f.readlines()
    for line in lines:
        casamento = re.search(
            r"Registo de casamento n\.º \d+: ((?:\w+\s?)+) c\.c\. ((?:\w+\s?)+)", line)
        batizado = re.search(
            r"Registo de batismo n\.º \d+: ((?:\w+\s?)+) \. Pai: ((?:\w+\s?)+) ; Mãe: ((\w+\s?)+)", line)
        if casamento:
            str1 = casamento.group(1).strip()
            str2 = casamento.group(2).strip()
            result[str1] = result.setdefault(str1, 0) + 1
            result[str2] = result.setdefault(str2, 0) + 1
        elif batizado:
            str1 = batizado.group(1).strip()
            str2 = batizado.group(2).strip()
            str3 = batizado.group(3).strip()
            result[str1] = result.setdefault(str1, 0) + 1
            result[str2] = result.setdefault(str2, 0) + 1
            result[str3] = result.setdefault(str3, 0) + 1
    result = collections.OrderedDict(sorted(result.items()))
    for name in result:
        print(name + ": " + str(result[name]))