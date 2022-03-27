#/bin/env bash
java -mx3g edu.stanford.nlp.pipeline.StanfordCoreNLP -outputFormat json -file input.txt
java -mx3g edu.stanford.nlp.pipeline.StanfordCoreNLP -file input.txt