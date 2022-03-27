#!/bin/env bash

pushd ~
wget http://nlp.stanford.edu/software/stanford-corenlp-latest.zip
unzip stanford-corenlp-latest.zip
/bin/rm stanford-corenlp-latest.zip
popd