import collections
import numpy as np
import pandas as pd
import sys, glob, os

dir_input = 'data/wiki_words/'
dir_samples = 'large_output_dir/'

dir_input = 'data/12dicts/American/'
dir_samples = 'output/12dict_short/'

dir_input = 'data/12dicts/American/'
dir_samples = 'output/12dict/'


def load_sampled_words(dir_input, dir_samples):
    
    org_text = os.path.join(dir_input, "input.txt")
    words = set()
    with open(org_text) as FIN:
        for line in FIN:
            for item in line.strip().split():
                words.add(item)


    C = collections.defaultdict(dict)
    totals = collections.defaultdict(dict)

    gb = glob.glob(os.path.join(dir_samples,"words_*"))

    for f_word in gb:
        with open(f_word) as FIN:
            for line in FIN:
                try:
                    p,word = line.split()
                except:
                    break

                p = float(p)
                n = len(word)

                if word not in C[n]:
                    C[n][word] = 0
                    totals[n][word] = 0


                C[n][word] += p
                totals[n][word] += 1

    for n in C.keys():
        for w in C[n].keys():
            C[n][w] /= totals[n][w]


    for n in C.keys():
        df = pd.DataFrame.from_dict(C[n],orient='index')
        df = df.rename(columns={0:'score'}).sort_values('score')

        df['in_corpus'] = [x in words for x in df.index]
        C[n] = df
        #is_word =

    return C

if __name__ == "__main__":

    N = int(sys.argv[1])

    C = load_sampled_words(dir_input, dir_samples)

    Z = C[N]
    idx = Z['in_corpus']==True




    # Find the "interesting" words near the front of the corpus
    cutoff_score = np.percentile(Z[idx].score,99.9)
    print Z[(~idx) & (Z.score<cutoff_score)][:15]

    print Z[idx][:5]
    print Z[idx][-10:]


    #exit()

    import seaborn as sns

    bins = np.linspace(0,Z.score.max(),100)

    sns.distplot(Z[idx].score, bins=bins,label='real words')
    sns.distplot(Z[~idx].score, bins=bins,label='fake words')
    sns.plt.legend()
    sns.plt.show()


