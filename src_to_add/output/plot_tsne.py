import h5py, os
import numpy as np

import sys
k = int(sys.argv[1])

os.system('mkdir -p figures')

import seaborn as sns
sns.set_style('whitegrid')

f_h5 = 'states_{}.h5'.format(k)
h5 = h5py.File(f_h5,'r+')

T = h5["tsne"][:]
words = h5["words"][:]
N = words.shape[0]
print N

T /= np.abs(T.max(axis=0))
print T

tx,ty = T.T
fig, ax = sns.plt.subplots(1, 1, figsize=(12, 12))
ax.xaxis.set_ticklabels([])
ax.yaxis.set_ticklabels([])

sns.plt.scatter(tx,ty,color='b',s=10,alpha=0.75,zorder=10)

for i in range(N):
    ax.annotate(words[i], (tx[i],ty[i]),alpha=0.95,
                backgroundcolor=(1,1,1,.25))


sns.plt.xlim(tx.min(),tx.max())
sns.plt.ylim(ty.min(),ty.max()+0.1)
txt = "{}-letter dict words LSTM RNN; tSNE over final state".format(k)
sns.plt.title(txt,fontsize=18)
sns.despine(bottom=True,left=True)
sns.plt.tight_layout()

f_png = 'figures/tsne_{}.png'.format(k)
sns.plt.savefig(f_png,bbox_inches=0)
sns.plt.show()
