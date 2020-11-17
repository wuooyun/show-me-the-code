#!/usr/bin/env python3
from collections import OrderedDict

filepath = r"C:\Users\Yun\Downloads\python-3.9.0-docs-text\library\code.txt"

dict_words = OrderedDict()
with open(filepath,'r') as f:
    words = f.read().lower().replace('\n','').split(' ')
set_words =  set(words)
set_words.remove('')
for word in set_words:
    dict_words[word] = words.count(word)

print(sorted(dict_words.items(), key = lambda kv:(kv[1], kv[0])))


