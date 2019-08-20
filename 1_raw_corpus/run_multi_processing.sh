#! /bin/bash

FILES=./splited_corpus_namu/*

for file in $FILES
do 
    #echo ${file}
    FILENAME=`echo "$file" | cut -d "." -f2`
    cat ${file} | python3 pos_tagger_mecab_sejong.py >> .${FILENAME}.pos &
done

