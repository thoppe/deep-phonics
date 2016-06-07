# Deep Phonics
[https://github.com/thoppe/deep-phonics](https://github.com/thoppe/arXiv2git)
----------
### [Travis Hoppe](http://thoppe.github.io/), [@metasemantic](https://twitter.com/metasemantic)
====

### Recurrent Neural Networks
!(figures/RNN_example.jpg)
Great for language modeling*. What's the next letter?
### `The cat in the ha`
  
&& *[RNN Science titles](https://github.com/thoppe/RNN_science_titles), DC Hack && Tell Round 26: [The Curious Camaraderie of Code]((http://dc.hackandtell.org/2015/11/16/round-26.html)
  
=====

### Can we train the network to learn how to spell?

!(figures/spelling_bee.mp4) Scripps spelling bee: academic bloodsport for kids

====*

### Secrect sauce?
Don't feed it sentences, give the network *randomized* word order.

destitution outshone perfidious intestate autumn upswing usury perennially 
cowgirl hovel chalet corrugated phantasmagoria xylophone union flippantly
craving willowy undersigned meningitis critically proofreader organist 
segment cape letter savanna minimalism defector midstream potentate 
blossom careless inherent confirmed exploratory lumberyard maverick 
discourtesy statistical leeway pecan execute eggbeater enshroud weatherize
mainsail greedily outgrow sample wall befit desperate jostle momentous 
blast mark acrimony loss benevolence bunion typhus subliminal refutation
inspire mischievousness lawlessness featherweight leisure drainpipe 
polo strangler radiance office encephalitis stupendously airlift 
slickly slacks dressy navigate duds pinch prime keep ammo deceptive
mafioso alternation overcast combative unbeknown photoelectric 

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

====
  
## Deep "spelling"

Wanted a consensus spelling of many words, but not too specialized.
Initial input from Wikipedia (freq > 500), too abstract.

Used 6of12 dictionaries, removing all proper nouns and acronyms.
Fed the words in randomized, repeated all words 4 times.
  
====
  
#  Thanks, you!
Say hello: [@metasemantic](https://twitter.com/metasemantic)