#! /bin/bash
BERT_BASE_DIR="/root/workspace"
OUTPUT_DIR="/data2/bert_record"
python run_squad_multi_gpu.py \
  --vocab_file=$BERT_BASE_DIR/vocab/final_total_vocab.txt \
  --bert_config_file=$BERT_BASE_DIR/result_unigram/bert_config.json \
  --init_checkpoint=$BERT_BASE_DIR/result_unigram/model.ckpt-1300002\
  --do_train=True  \
  --train_file=$BERT_BASE_DIR/eval/koquad/KorQuAD_v1.0_train.json \
  --do_predict=True \
  --predict_file=$BERT_BASE_DIR/eval/koquad/KorQuAD_v1.0_dev.json\
  --do_lower_case=False \
  --train_batch_size=8\
  --learning_rate=8.5e-5 \
  --num_train_epochs=1.0 \
  --max_seq_length=384 \
  --doc_stride=128 \
  --output_dir=$OUTPUT_DIR/squad_base_result/output_unigram_1.3M \
  --use_tpu=False \
  --version_2_with_negative=False
