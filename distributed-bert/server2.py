# -*- coding:utf-8 -*-
# Author: hankcs
# Date: 2019-04-14 21:47

import os
import json

import tensorflow as tf

os.environ['CUDA_VISIBLE_DEVICES'] = '1'

os.environ['TF_CONFIG'] = json.dumps({
    'cluster': {
        'worker': ['localhost:5000', 'localhost:5001']
    },
    'task': {'type': 'worker', 'index': 1}
})

tf.contrib.distribute.run_standard_tensorflow_server().join()
