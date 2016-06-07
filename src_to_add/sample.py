#from __future__ import print_function
import numpy as np
import tensorflow as tf
import tqdm

import argparse
import time
import os
from six.moves import cPickle

from utils import TextLoader
from model import Model

_GPU_mem_fraction = 0.15
gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=_GPU_mem_fraction)
CFG = tf.ConfigProto(gpu_options=gpu_options)


class RNN_sampler(object):

    def __init__(self, save_dir, word_buffer=5):

        self.save_dir = save_dir
        
        with open(os.path.join(save_dir, 'config.pkl'), 'rb') as f:
            saved_args = cPickle.load(f)
            
        with open(os.path.join(save_dir, 'chars_vocab.pkl'), 'rb') as f:
            self.chars, self.vocab = cPickle.load(f)

        self.word_buffer = word_buffer
        self.model = Model(saved_args, True)


    def __iter__(self):

        with tf.Session(config=CFG) as sess:
        
            tf.initialize_all_variables().run()
        
            saver = tf.train.Saver(tf.all_variables())
            ckpt = tf.train.get_checkpoint_state(self.save_dir)
            if ckpt and ckpt.model_checkpoint_path:
                saver.restore(sess, ckpt.model_checkpoint_path)

            while True:
                S = self.model.sample(sess,self.chars,self.vocab,
                                      self.word_buffer)
                for w,p in S:
                    yield w,p


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--save_dir', type=str, default='save',
                       help='model directory to store checkpointed models')

    parser.add_argument('--f_out', type=str, default='words.txt',
                       help='File to save results')

    parser.add_argument('-s', type=int, default=10,
                       help='number of samples')
    args = parser.parse_args()


    FOUT = open(args.f_out,'w')
    R = iter(RNN_sampler(args.save_dir))

    for k in tqdm.tqdm(range(args.s)):
        w,p = next(R)
        msg = "{:0.8f} {:12s}".format(p,w)
        print msg
        FOUT.write(msg+'\n')
