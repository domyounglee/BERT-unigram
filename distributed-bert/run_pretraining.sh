#! /bin/bash
BASE_DIR="/root/workspace"
python run_pretraining.py \
    --input_file=/data2/bert_record/*512.tfrecord \
    --output_dir=$BASE_DIR/result_unigram  \
    --do_train=True \
    --do_eval=True \
    --bert_config_file=$BASE_DIR/result_unigram/bert_config.json \
    --train_batch_size=8 \
    --max_seq_length=512 \
    --max_predictions_per_seq=20 \
    --num_train_steps=1300000 \
    --num_warmup_steps=4000 \
    --learning_rate=5.0e-5 \
    --save_checkpoints_steps=50000 \
    --num_gpus=8 \
    --stage=2 \
    --prev_global_step=900000 \

