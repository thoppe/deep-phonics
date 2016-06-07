#from __future__ import print_function
import numpy as np
import tensorflow as tf
from tqdm import tqdm

import argparse,collections
import os
from six.moves import cPickle
from model import Model

import pandas as pd

_GPU_mem_fraction = 0.75
gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=_GPU_mem_fraction)
CFG = tf.ConfigProto(gpu_options=gpu_options)
#dir_input = 'data/wiki_words/'
dir_input = 'data/12dicts/American/'

org_text = os.path.join(dir_input, "input.txt")


class word_Model(Model):

    def word_sample_set(self, word_set, sess, chars, vocab):

        p_set = []
        state_set = []
        with sess.as_default():
            
            for word in word_set:
                
                # Always prime with the space
                prime = ' ' + word + ' '
                state = self.cell.zero_state(1, tf.float32).eval()
                P = []
                STATE = []

                for c0,c1 in zip(prime,prime[1:]):
            
                    x = np.zeros((1, 1))
                    x[0, 0] = vocab[c0]
                    
                    feed = {self.input_data: x, self.initial_state:state}
                    [probs, state] = sess.run([self.probs, self.final_state], feed)

                    next_letter_prob = probs[0][vocab[c1]]
                    most_probabale_letter = chars[np.argmax(probs[0])]
                    most_probabale_prob = probs[0][vocab[most_probabale_letter]]

                    #if c0 == ' ' and c1 == 't':
                    #    print c0,c1,most_probabale_letter,next_letter_prob, most_probabale_prob
                    STATE.append(state[0])
                    
                    P.append(next_letter_prob)

                prob = -(np.log(np.array(P)).sum())
                p_set.append(prob)
                
                state_set.append(np.vstack(STATE))
                
                                 

                print "Sampled", word, prob
                
        return p_set, np.array(state_set)
       

class RNN_sampler(object):

    def __init__(self, save_dir, word_buffer=5):

        self.save_dir = save_dir
        
        with open(os.path.join(save_dir, 'config.pkl'), 'rb') as f:
            saved_args = cPickle.load(f)
            
        with open(os.path.join(save_dir, 'chars_vocab.pkl'), 'rb') as f:
            self.chars, self.vocab = cPickle.load(f)

        self.word_buffer = word_buffer
        self.model = word_Model(saved_args, True)

        sess = tf.Session(config=CFG)

        init_op = tf.initialize_all_variables()
        sess.run(init_op)

        saver = tf.train.Saver(tf.all_variables())
        ckpt = tf.train.get_checkpoint_state(self.save_dir)
        if ckpt and ckpt.model_checkpoint_path:
            saver.restore(sess, ckpt.model_checkpoint_path)
            
        self.sess = sess

    def word_sample_set(self, word_set):

        p = self.model.word_sample_set(
            word_set,
            self.sess,
            self.chars,
            self.vocab,
        )
        return p


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--save_dir', type=str, default='save_12dict/',
                       help='model directory to store checkpointed models')
    parser.add_argument('N', type=int, default=12,
                       help='Length of words to compute')

    #parser.add_argument('--f_out', type=str, default='words.txt',
    #                   help='File to save results')

    #parser.add_argument('-s', type=int, default=10,
    #                   help='number of samples')
    args = parser.parse_args()

    
R = RNN_sampler(args.save_dir)

N = args.N

words = set()
with open(org_text) as FIN:
    for line in FIN:
        for item in line.strip().split():
            if len(item)==N:
                words.add(item)

words = list(words)[:]

print "Sampling ", len(words)
score,states = R.word_sample_set(tqdm(words))

import h5py

f_h5 = 'output/states_{}.h5'.format(N)
h5 = h5py.File(f_h5,'w')
h5['score'] = score
h5['states'] = states

dt = h5py.special_dtype(vlen=unicode)
h5.create_dataset("words", data=words, dtype=dt)
h5.close()

print states
