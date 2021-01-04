import re
import pandas as pd

dfT = pd.read_json('./data/df_tucholsky.json',lines=True)

dfT

#dfT.text.apply(lambda x: textLength(x))

text.strip().startswith('Der')

titleM = dfT['title'].str.contains('Krieg') 
yearM = dfT['year'] > 1930

dfT[(titleM & yearM)]

dfT[dfT.title.str.contains('Krieg')]

# Tucholskys output over the years

df1 = dfT.groupby('year').size()#.plot()

words = ['Weltbühne', 'Tucholsky', 'Panter', 'Hauser','Wrobel','Tiger']
dataframes = []
for word in words:
    dataframes.append(dfT[dfT.text.str.contains(word)].groupby('year').size())

len(dataframes)

dataframes[1]

dfRes = pd.concat(map(lambda x: x/df1, dataframes),axis=1).rename(columns={x:word for x,word in enumerate(words)})

dfRes.head(2)

dfRes.plot()

dfT.groupby('year').get_group(1917)

tempVol = []
for i, g in dfT.groupby('year'):
    tempVol.append((i,g.shape[0]))

weltb = []
dfWeltb = dfT[dfT.text.str.contains('Weltbühne')]
for i, g in dfWeltb.groupby('year'):
    weltb.append((i,g.shape[0]))

dfTOutput = pd.DataFrame(tempVol).set_index(0)

dfWeltbOutput = pd.DataFrame(weltb).set_index(0)

dfTOutput.merge(dfWeltbOutput,left_index=True,right_index=True,how='outer').plot.bar()

## How much did he write? 

Count words in each text, find the most common used words.

from collections import Counter

def textLength(row):
    return len(re.findall("\w+",row))

def countWords(row):
    allWords = re.findall("\w+",row)
    counts = Counter(allWords)
    total = len(allWords)
    resTemp = {k: v / total for k, v in counts.items()}
    res = {k: v for k, v in sorted(resTemp.items(), key=lambda item: item[1],reverse=True)}
    return res

dfT['textLength'] = dfT.text.apply(lambda row: textLength(row))

dfT

dfT['wordOccurance'] = dfT.text.apply(lambda row: countWords(row))

#dfT.wordOccurance.iloc[23]

You can easily manipulate data and the view on it, simply change mean to median or sum.

#dfT[['year','textLength']]

dfT[['year','textLength']].groupby('year').median().plot.bar()

What happend in 1912, 1927, 1931?

print(dfT[dfT.year == 1931].text.iloc[2])

dfT.to_hdf('./data/df_tucholsky_meta.hd5','tucholsky_meta')