#/bin/env bash
#java -Xmx3g edu.stanford.nlp.pipeline.StanfordCoreNLP -outputFormat json -file input.txt
#java -Xmx3g edu.stanford.nlp.pipeline.StanfordCoreNLP -file input.txt
java -Xmx3g edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,ssplit,pos -file input.txt
