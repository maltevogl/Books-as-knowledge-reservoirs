# Natural Language Processing

## NLP

  > __NLP__: Natural language processing tries to understand, interpret and manipulate human language.

  - In Python: _nltk_ or _spacy_ package  
  - Routines for _parts-of-speech_ tagging, _named-entity-recognition_, _tokenization_ and more

## Basic concepts and routines

  For a given text:

  - Recognize the sentence boundaries
  - In each sentence, find all tokens (i.e. words without punctuation)
  - _Lemmatization_ and _Stemming_ describe the process to find roots of words
    - Lemma of _went_ is _go_, or for nouns _mice_ becomes _mouse_
    - Stemm is part of word which does not change, e.g. the stem of _produced_ is _produc_ because of words like _production_
  - Identify parts of speech (_nouns_,_verbs_, ..) for every lemmatized word


### Sentences

```{panels}
  - Recognize the sentence boundaries
---
    import pandas as pd
    import nltk
    data = pd.read_json('./data/df_tucholsky.json', lines=True)
    text = data.text.iloc[0]

    sentences = nltk.sent_tokenize(text)

    sentences[0]

    # outputs gives
    'Der Floh Im Departement du Gard – ganz richtig, da, wo Nîmes liegt und der Pont du Gard: im südlichen Frankreich – da saß in einem Postbüro ein älteres Fräulein als Beamtin, die hatte eine böse Angewohnheit: sie machte ein bißchen die Briefe auf und las sie.'
```

### Tokens

```{panels}
  - Recognize the sentence boundaries
  - In each sentence, find all tokens
    - could be words only
    - or including punctuation

---

    import pandas as pd
    import nltk
    data = pd.read_json('./data/df_tucholsky.json', lines=True)
    text = data.text.iloc[0]

    sentences = nltk.sent_tokenize(text)
    nltk.word_tokenize(sentences[0])

    # outputs gives
    ['Der','Floh','Im','Departement','du','Gard','–','ganz','richtig',',','da',',','wo','Nîmes',
    'liegt','und','der','Pont','du','Gard',...]
 ```

### Lemmatization

```{panels}
  - Recognize the sentence boundaries
  - In each sentence, find all tokens
  - _Lemmatization_ to find roots of token
    - Lemma of _goes_ is _go_, or for nouns _mice_ becomes _mouse_

---

    import nltk
    lemmatizer = nltk.stem.WordNetLemmatizer()
    lemmatizer.lemmatize('goes')

    # output gives
    'go'
 ```

### Stemming

```{panels}
  - Recognize the sentence boundaries
  - In each sentence, find all tokens
  - _Stemming_ to find roots of tokens
    - Stemm is part of token which does not change, e.g. the stem of _produced_ is _produc_


---

    import nltk
    stemmer = nltk.stem.SnowballStemmer('english')
    stemmer.stem('produced')

    # output gives
    'produc'
 ```

### Lemmatization or Stemming

- Stemming simpler, rule based process
- Lemmatization computational more expensive, based on dictionaries


```{panels}

Strongly language dependent

  - Larger corpora mostly English, thus poorer results for less frequent languages
  - For example: No German lemmatizer in standard NLTK

---

Related links:

  - Leipzig Corpus Miner ([LCM](http://www.epol-projekt.de/tools-nlp/leipzig-corpus-miner-lcm/))
  - Erlangen University [Corpus-Linguistik](https://www.linguistik.phil.fau.de/resources/demos/)
    - Hanover Tagger [Source](https://github.com/wartaal/HanTa)
  - Classical Languages Tool Kit [CLTK](http://cltk.org)
  - [ConceptNet](http://conceptnet.io/)
 ```

### Parts of Speech

```{panels}
  - Recognize the sentence boundaries
  - In each sentence, find all tokens
  - _Lemmatization_ or _Stemming_ to find roots of tokens
  - Identify parts of speech (_nouns_,_verbs_, ..) for every transformed token

---

    import spacy
    nlp = spacy.load('de_core_news_md')
    doc = nlp(text) # loaded with Pandas, as before
    tokens = [(token.lemma_,token.pos_) for token in doc]
    tokens[:10]

    # output gives
    [('\n\n                              ', 'SPACE'),
    ('der', 'DET'),
    ('Floh', 'NOUN'),
    ('\n\n                              ', 'SPACE'),
    ('Im', 'ADP'),
    ('Departement', 'NOUN'),
    ('du', 'PROPN'),
    ('Gard', 'PROPN'),
    ('–', 'PUNCT'),
    ('ganz', 'ADV')]
 ```

### Key concepts

  - Concordance
    - visually ordered list of searched word in context
    - derived from that: Find words with similar context or return the shared context of two or more words
  - Collocations
    - words that often occur together, e.g. "crystal clear" or "nuclear family"
  - Expanded version: _"n-grams"_
    - groups of n words or characters, e.g. character bi-grams "cr", "ri", "is", "st", "ta", "al"
