from stanfordcorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP(r'stanford-corenlp-4.4.0')

sentence = input('Sentence: ')

print('Tokenize:', nlp.word_tokenize(sentence))
print('Part of Speech:', nlp.pos_tag(sentence))
print('Named Entities:', nlp.ner(sentence))
print('Constituency Parsing:', nlp.parse(sentence))
print('Dependency Parsing:', nlp.dependency_parse(sentence))

nlp.close()