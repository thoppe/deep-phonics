import os
import itertools

sample_rate = 50000
chains_n = 5

#save_dir = 'save'
#output_dir = 'output_dir'

#save_dir = 'save_large_wiki'
#output_dir = 'output/large_wiki'

#save_dir = 'save_12dict'
#output_dir = 'output/12dict'

save_dir = 'save_12dict_short'
output_dir = 'output/12dict_short'


os.system('mkdir -p {}'.format(output_dir))
def run(n):
    args = {
        "f_out" : "{}/words_{}".format(output_dir,n),
        "sample_rate" : sample_rate,
        "save_dir" : save_dir,
    }
    cmd = bcmd.format(**args)
    os.system(cmd)
    return n


bcmd = ('python sample.py -s {sample_rate} '
        '--save_dir {save_dir} --f_out {f_out}')

ITR = itertools.imap(run, range(chains_n))

import multiprocessing
MP = multiprocessing.Pool()
ITR = MP.imap(run, range(chains_n))


list(ITR)

