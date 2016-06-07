import numpy as np
from tqdm import tqdm
import h5py
import sys

k = int(sys.argv[1])
#k = 10

cutoff = 10**10

f_h5 = 'states_{}.h5'.format(k)
h5 = h5py.File(f_h5,'r+')
score = h5['score'][:]
states = h5['states']
words = h5['words'][:]

N = states.shape[0]
N,lets,dim = states.shape

if "tsne" in h5:
    print "Already computed, exiting"
    exit()

tsne_h5 = h5.require_dataset("tsne",
                             shape=(N,2),
                             dtype=np.float32)

representation_h5 = h5.require_dataset("representation",
                             shape=(N,dim),
                             dtype=np.float32)

print "total states", states.shape[0]
states = states[:cutoff, -1:, :]

# words, letters, dimension
N,lets,dim = states.shape
print states.shape

# Normalize
norms   = np.linalg.norm(states, axis=2)
for i in range(N):
    norm = np.linalg.norm(states[i],axis=1)
    states[i] /= norm.reshape(-1,1)

total_state = np.sum(states, axis=1)
#norms = np.linalg.norm(total_state,axis=1)
#total_state /= norms.reshape(-1,1)

X = total_state

from sklearn.manifold import TSNE
clf = TSNE(init='pca',method='exact')
print "Computing TSNE"
T = clf.fit_transform(X)

tsne_h5[:T.shape[0],:] = T
representation_h5[:X.shape[0],:] = X


'''
import seaborn as sns
tx,ty = T.T

fig, ax = sns.plt.subplots(1, 1, figsize=(12, 12))
#sns.plt.scatter(tx,ty)

for i in range(N):
    ax.annotate(words[i], (tx[i],ty[i]),alpha=0.95)

sns.plt.xlim(tx.min(),tx.max())
sns.plt.ylim(ty.min(),ty.max())
sns.plt.show()

print T
'''


from scipy.spatial import cKDTree
T = cKDTree(X)

for i,j in T.query_pairs(0.70):
    x,y = X[i],X[j]
    print i,j, words[i], words[j], np.linalg.norm(x-y)

'''
# Close words in activation space (last activation only)

273 562 taught height 0.659404
58 1720 millet omelet 0.688043
1250 1830 girder foster 0.69831
941 943 subway sugary 0.692039
70 1443 poison popgun 0.663278
899 1186 bomber goober 0.649339
932 1206 cancan catnap 0.688852
295 1910 hooker heifer 0.688765
877 962 jacket fillet 0.699056
18 153 tickle cuddle 0.68164
375 1771 gambol symbol 0.688402
1363 1883 toffee golfer 0.696158
687 1609 vanity sanity 0.66418
250 1578 coffer cancer 0.688614
734 740 totter roster 0.651146
1506 1541 sudden sullen 0.642558
1291 1395 pimply pebbly 0.694431
1278 1505 grotto gringo 0.693624
1293 1933 castor captor 0.487855
1581 1640 except inject 0.68732
571 985 parley pearly 0.68799
73 1468 beater gaiter 0.678473
1127 1220 canard aboard 0.681541
261 1337 curdle curlew 0.675444
429 627 helper mailer 0.664748
489 1304 tartly neatly 0.687843
584 980 sprite splice 0.668795
41 123 parrot pallet 0.697654
461 1186 goiter goober 0.588922
499 979 attest detest 0.642893
210 610 exotic elicit 0.699686
1342 1660 boggle giggle 0.628065
1382 1389 borrow tallow 0.694959
169 479 packet patter 0.66274
653 949 inward inland 0.671918
233 1984 fealty fleecy 0.685142
153 509 cuddle cattle 0.69621
1227 1979 clause chisel 0.696218
411 1683 hamper hanger 0.613761
513 1683 hammer hanger 0.649597
899 1766 bomber rubber 0.679901
1509 1745 beaver carver 0.688369
1144 1473 lonely vilely 0.692789
1683 1874 hanger burger 0.66524
1865 1883 boozer golfer 0.688714
584 1484 sprite spirit 0.699282
927 1636 forked fondue 0.689186
81 514 menage voyage 0.696653
400 1895 scabby scanty 0.655799
1700 1891 racist jurist 0.665335
219 924 decant decamp 0.624438
572 920 chrome choice 0.681929
1202 1751 bookie bootie 0.542383
900 903 ballet mallet 0.608353
811 1124 vagary canary 0.690393
121 498 peahen hasten 0.680598
1372 1411 gibber limber 0.670751
38 1475 chapel chalet 0.622799
1571 1587 polish potash 0.631599
55 352 miller molder 0.636044
13 1643 muzzle hustle 0.688351
934 1801 purely hugely 0.670396
665 1880 newton ribbon 0.695978
1080 1509 meager beaver 0.697039
1320 1460 steady treaty 0.68104
177 354 dimple fumble 0.697926
1408 1776 bugler walker 0.677246
482 1031 report repast 0.652141
990 1155 blotch clutch 0.581612
571 1839 parley parcel 0.674193
169 1111 packet basket 0.559509
104 904 jasper jogger 0.674955
1250 1883 girder golfer 0.645133
775 1602 twitch swatch 0.669945
1590 1613 genome glamor 0.681664
977 1080 jester meager 0.677257
454 1411 dicker limber 0.699553
1108 1500 reaper rapier 0.694409
936 1519 cloudy creaky 0.666408
657 688 plaque plasma 0.698201
87 295 kicker hooker 0.645956
1028 1924 wicked wizard 0.695411
61 712 tether theyre 0.688203
176 1982 chilly clergy 0.683814
470 1584 abjure allude 0.659655
1062 1300 pickle pimple 0.602976
454 1017 dicker wicker 0.623214
1655 1935 nudism sadism 0.660914
685 1139 falter farmer 0.622198
104 1680 jasper garner 0.69397
944 1767 skewer weeder 0.671115
729 1643 hassle hustle 0.646436
695 842 cliche clingy 0.681699
1825 1979 tinsel chisel 0.683032
1643 1884 hustle tussle 0.628919
618 1465 dative votive 0.63926
87 1927 kicker barker 0.648394
1226 1428 spoken screen 0.693214
291 1425 adjust august 0.644065
151 153 cuddly cuddle 0.467423
90 1249 hanker larder 0.689869
927 1028 forked wicked 0.672123
510 1666 basely boldly 0.694347
1182 1878 hacker healer 0.661982
373 906 lather father 0.675715
690 1916 usable arable 0.635592
35 561 govern gopher 0.695714
806 1838 instil insole 0.692229
365 534 snooty snugly 0.673082
868 1927 hawker barker 0.655311
521 1710 jargon tycoon 0.681881
1830 1853 foster ticker 0.679732
409 1688 mostly lastly 0.648499
575 1048 blower bowler 0.606646
859 1142 outage uptake 0.676737
1683 1793 hanger tanner 0.698677
45 1493 voyeur velour 0.62395
474 789 cougar coitus 0.683261
1486 1674 damson coupon 0.690047
1177 1444 beetle bungle 0.67934
920 1979 choice chisel 0.698658
519 1261 knight naught 0.651477
179 524 pigsty smutty 0.686536
254 496 silver sinker 0.684172
1619 1856 deduct induct 0.616496
496 952 sinker talker 0.699086
280 757 pounce seance 0.685854
193 1108 reamer reaper 0.61384
636 1272 boiler bootee 0.68917
508 619 septet patent 0.690025
1288 1793 turner tanner 0.604916
347 1839 carrel parcel 0.66188
1447 1510 yearly wisely 0.654584
58 310 millet mullet 0.553844
207 1599 jungle tingle 0.593927
759 1250 keeper girder 0.684976
1532 1542 barbed barber 0.507087
118 1458 eyeful fitful 0.617743
789 1674 coitus coupon 0.685285
146 821 simper temper 0.66215
308 1486 damper damson 0.687532
479 1355 patter matted 0.650289
81 776 menage meddle 0.699922
242 1398 alpine famine 0.653901
154 1012 locket market 0.676268
1672 1910 heater heifer 0.5984
450 1899 hunger ranger 0.670993
761 1403 angora angina 0.630455
1599 1825 tingle tinsel 0.646644
822 1802 delete deluxe 0.6446
140 534 scuzzy snugly 0.660463
1030 1301 hooked hooves 0.656147
1449 1504 stream strain 0.672854
1184 1455 canvas cancel 0.694933
894 1628 invent intend 0.659044
190 404 doable gabble 0.65901
84 1151 tautly cutely 0.666343
180 650 damage ragged 0.691111
107 858 bunker geezer 0.687972
372 590 unsaid unsold 0.61575
173 1643 jumble hustle 0.661311
'''
