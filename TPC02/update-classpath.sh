#/bin/env bash
for file in `find $HOME/stanford-corenlp-4.4.0 -name "*.jar"`; 
do
    export CLASSPATH="$CLASSPATH:`realpath $file`"; 
done