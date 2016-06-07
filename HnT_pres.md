# Deep Phonics
[https://github.com/thoppe/deep-phonics](https://github.com/thoppe/deep-phonics)
----------
### [Travis Hoppe](http://thoppe.github.io/), [@metasemantic](https://twitter.com/metasemantic)
====

### Recurrent Neural Networks
!(figures/RNN_example.jpg)
Great for language modeling*. What's the next letter?
### `The cat in the ha`
  
&& *[RNN Science titles](https://github.com/thoppe/RNN_science_titles), DC Hack && Tell Round 26: [The Curious Camaraderie of Code]((http://dc.hackandtell.org/2015/11/16/round-26.html)
  
=====*

### Can we train the network to learn how to spell?

!(figures/spelling_bee.mp4) Scripps spelling bee: academic bloodsport for kids

====*

### Secret sauce?
Don't feed it sentences, give the network *randomized* word order.

destitution outshone perfidious intestate autumn upswing usury
cowgirl hovel chalet corrugated phantasmagoria xylophone union
craving willowy undersigned meningitis critically proofreader 
segment cape letter savanna minimalism defector midstream 
blossom careless inherent confirmed exploratory lumberyard
discourtesy statistical leeway pecan execute eggbeater enshroud
mainsail greedily outgrow sample wall befit desperate jostle 
blast mark acrimony loss benevolence bunion typhus subliminal
inspire mischievousness lawlessness featherweight leisure 
polo strangler radiance office encephalitis stupendously 
slickly slacks dressy navigate duds pinch prime keep ammo
mafioso alternation overcast combative unbeknown 

====

## "Deep" spelling
LSTM RNN (modeled after [char-rnn](https://github.com/karpathy/char-rnn) by Karparthy)
Coded in `tensorflow`, deep learning library by Google.
Train time, ~4 hours on a GTX 980.
  
+ `layers=2`
+ `width=1024`
+ `batch_size=50`
+ `seq_length=15`
+ `num_epochs=30`

====*
  
## Deep "spelling"

Wanted a consensus spelling of many words, but not too specialized.
Initial input from Wikipedia (freq > 500), too abstract.

Used 6of12 dictionaries, removing all proper nouns and acronyms.
Fed the words in randomized, repeated all words 4 times.

Sample words from the network and see what happens...!?

====

## Score words
As you push words through the network, each letter selected gives a probability. Assign a _score_ to each word s = -log(prod(p))
!(figures/word_distributions.png)<<height:600px>>
  
====
### Sampled seven letter words
Imaginary words
    twigwee  4.044358     False
    uncoorn  4.178008     False
    eminate  4.240006     False
    wizable  4.249013     False
    icillic  4.320535     False
    rigtory  4.334869     False
    titting  4.543220     False
    upbland  4.549292     False
    idlener  4.578380     False
    gumborn  4.607096     False
Real words    
    untruth  2.792500      True
    ringlet  3.114211      True
    missing  3.312544      True
    trumpet  3.356997      True
    mestizo  3.444021      True
    
    roadway  14.202039      True
    stupefy  14.227516      True
    dismiss  14.672120      True
    nightly  14.861044      True
    tsunami  15.432922      True
    cantata  15.943768      True

====

## RNN Ipsum
  
Trappe curient hectar loads, jit trucket haddy kleptoman wooel. Libelor ransor metis, edificently cocklesh wize hoo, furthorn sumptuously marma. Grote reeker welf joal, ison unmovel bridesman orn. Cordoner thromb laburna kowhead. Jets scoutman ballry, ostraciders agogy wilfulate a. Immortent ordan whick. Ovi bystan toge jit meni coby viscounce drychange. Askay smilt voodom, reunity hairdoor, gnorthiness ex. Spasion aquet sagebruch knavi sagebruch meniment diora. Grimlet orn askay ful earant chiropon impobiacy. Chainous harpistry olean yiem easth arrayo menorama. Warthoge buryard jaunch remoss golfhound. Raker drak rheost, everywork dreamable, axister coby nill.

====
Cluster words on the network *imprint* after a word is pushed through.
!(figures/tsne_10.png) <<height:700px>> tSNE shows distinct clusters of spelling patterns, `-ible`
====*
Cluster words on the network *imprint* after a word is pushed through.
!(figures/tsne_9.png) <<height:700px>> tSNE shows distinct clusters of spelling pattern, `-tive`
====*
Cluster words on the network *imprint* after a word is pushed through.
!(figures/tsne_8.png) <<height:700px>> tSNE shows distinct clusters of spelling patterns, `-ous`
  
====*

    
#  Thanks, you!
Say hello: [@metasemantic](https://twitter.com/metasemantic)