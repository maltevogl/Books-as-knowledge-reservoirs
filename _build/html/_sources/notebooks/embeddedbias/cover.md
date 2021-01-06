# Embedded bias

  - How to deal with words in mathematical models?

  > represent words with numbers!

## Word embeddings

### bag-of-words

  - make list of occurring words and give them numbers ordered by frequency
    - 'the' -> `1`
    - 'it' -> `2`
    - ...
    - 'embedding' -> `23579`

  - Problems:
    - huge _one-hot-vectors_
    - hard to train
    - no context embedded

### Unsupervised word-vectors

  - use word and its context in reduced vector space (e.g. 300 dim.)
    - train model such that similar context leads to similar vectors

  - Pro: Semantics partly encoded in numbers
  - Problems:
    - large and very clean corpora necessary
    - computational hard


### General problems

  - No result for out-of-corpus words
  - Bad for specific language of e.g. scientific terms

## Bias in embeddings

  - Word embeddings are based on contemporary texts
  - If specific words occur in a limited set of contexts, bias translates from text to numbers
    - 'man' occurs with 'doctor', but 'woman' occurs with 'nurse'
    - 'black' occurs with 'criminal'
    - 'muslim' with 'radical'

## Bias exercise

  - Exercise
    - experiment with GloVe embeddings

## Reducing bias

  ![Basic idea, source _deeplearning.ai_](./assets/bias_vector.png)

## Can we use ML to detect bias ?

  - Pre-process Tucholsky corpus with NLP tools
  - Train GloVe on Tucholsky

  - Exercise:
    - Can we see a bias in Tucholsky's language?

## Intellectual dept of software

We have stepped in the area of _unknown software_ and silently started using programs without understanding them

This has lots of interesting implications and philosophical dimensions!

- Cory Doctorow [Blog-Post](https://boingboing.net/2019/07/28/orphans-of-the-sky.html)
  - Technology on top of other technology hides technological dept
- Jonathan Zittrain [New Yorker Article](https://www.newyorker.com/tech/annals-of-technology/the-hidden-costs-of-automated-thinking)
  - Main argument: AI is applied science and limits basic research
- Tyler Vigen [Collection of Correlations](http://www.tylervigen.com/spurious-correlations)
  - More data creates also more spurious correlations
