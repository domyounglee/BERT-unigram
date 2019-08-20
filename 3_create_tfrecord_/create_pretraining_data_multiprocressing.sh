#!/bin/bash
BERT_BASE_DIR="/root/workspace"
INPUT_FILES="/root/workspace/train_corpus/512/total*"
export CUDA_VISIBLE_DEVICES=-1
for file in $INPUT_FILES
do 
	#echo ${file}
	FILENAME=`echo "$file" | cut -d "." -f1 | cut -d "/" -f6`

	echo ${FILENAME}
	python create_pretraining_data.py \
          --input_file=${file}\
	  --output_file=$BERT_BASE_DIR/bert_corpus/${FILENAME}_512.tfrecord \
	  --vocab_file=$BERT_BASE_DIR/2_unigram_result/final_total_vocab.txt \
	  --do_lower_case=False \
	  --max_seq_length=512 \
	  --max_predictions_per_seq=20 \
	  --masked_lm_prob=0.15 \
          --do_whole_word_mask=True \
	  --random_seed=12345 \
	  --dupe_factor=5 &
done
