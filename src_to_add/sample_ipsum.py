import numpy as np

cutoff_percentile = 10

dir_input = 'data/12dicts/American/'
dir_samples = 'output/12dict/'

#dir_input = 'data/wiki_words/'
#dir_samples = 'output/large_wiki/'

#dir_input = 'data/12dicts/American/'
#dir_samples = 'output/12dict_short/'

primer_text = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam cursus ligula ultrices, semper orci eu, porttitor nulla. Phasellus ut velit eu neque dignissim tempus. Proin tincidunt molestie tellus sit amet cursus. Vivamus id nisl sed sapien egestas vehicula a et magna. Nullam rhoncus ut nulla non aliquet. Mauris commodo nec libero ac elementum. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vestibulum cursus diam vitae dolor pharetra tempus. XXX

Mauris egestas tellus ipsum, nec iaculis ipsum vulputate vitae. Vivamus lectus justo, condimentum vehicula nisi nec, placerat scelerisque velit. Donec luctus arcu nunc, eget euismod mi fringilla nec. Maecenas mattis finibus finibus. Cras eleifend mi lectus, ut condimentum purus tincidunt a. Curabitur et justo lacus. Sed mattis nisl sit amet nisl efficitur venenatis. Donec purus turpis, aliquam et molestie at, condimentum a ex. Quisque id justo convallis lacus facilisis pharetra et eu metus. Vivamus non purus nec mauris volutpat convallis. Interdum et malesuada fames ac ante ipsum primis in faucibus. Praesent gravida ut sapien mattis hendrerit. Donec urna libero, tristique a malesuada in, viverra eget arcu. XXX

In ac elementum urna. Pellentesque sodales neque vestibulum feugiat volutpat. Cras in ultrices lorem, venenatis cursus massa. Fusce at augue dolor. Nulla non lacinia turpis. In a facilisis sapien, a suscipit lorem. Quisque velit diam, congue ut massa eget, aliquam dictum justo. Suspendisse lacus eros, posuere ac odio non, vehicula pharetra purus. Suspendisse potenti. Cras tristique semper est eget bibendum. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. XXX

Nam enim arcu, fermentum vitae ligula sed, scelerisque ultricies nisi. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus viverra velit et aliquet tempor. Pellentesque ut dui at massa tempus auctor non nec turpis. In hac habitasse platea dictumst. Phasellus et erat nec lorem congue ullamcorper quis non lacus. Curabitur vel sem laoreet ante vulputate vehicula id vitae augue. Nulla erat mauris, ornare vel metus vel, suscipit hendrerit risus. Nullam lectus sem, molestie sed posuere id, euismod a tortor. Integer sed ante dapibus, feugiat ligula eget, maximus velit. Vivamus finibus sagittis lectus vitae tempus. Integer pharetra neque nulla, ut tempor libero eleifend accumsan. Nam rhoncus, massa eget iaculis pulvinar, ligula metus auctor diam, varius pellentesque metus leo eu odio. Cras id vulputate nibh. XXX
'''

import pattern.en
from view_words import load_sampled_words



C = load_sampled_words(dir_input, dir_samples)

for n in C:
    if n<2: continue
    if len(C[n]) == 0:
        continue
    
    Z = C[n]
    idx = Z.in_corpus == False

    if not len(Z[idx]) or not len(Z[~idx]):
        continue

    
    # Find the "interesting" words near the front of the corpus
    cutoff_score = np.percentile(Z[~idx].score,cutoff_percentile)

    C[n] = Z[(idx) & (Z.score<cutoff_score)]
    print cutoff_score, len(C[n])

text = pattern.en.tokenize(primer_text)#,tags=False,chunks=False)
ret = []

for sentence in text:

    for token in sentence.split():

        is_title_case = token[0] == token[0].upper()
        if not token.isalpha():
            ret.append(token)
            continue

        if len(token) in [0,1,2]:
            continue
        
        if token == 'XXX':
            ret.append('\n')
            continue
        


        n = len(token)
        word = C[n].sample(n=1).index.values[0]

        if is_title_case:
            word = word.title()

        ret.append(word)
        
text = ' '.join(ret)
text = text.replace(' .','.')
text = text.replace(' ,',',')
text = text.replace('\n ','\n')


print text


