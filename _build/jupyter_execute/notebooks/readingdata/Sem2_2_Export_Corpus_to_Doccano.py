

import re
import pandas as pd

dfT = pd.read_hdf('./data/df_tucholsky_meta.hd5')

## Export text to Doccano format


dfPart = dfT.copy()# dfT[dfT.year == 1917]

def createMeta(row):
    cols = ['ids','year','title','textLength']
    return {x:row[x] for x in cols}

meta =  dfPart.apply(lambda row: createMeta(row),axis=1)
labels = dfPart.text.apply(lambda x: [])

dfPart.insert(1,'meta',meta)
dfPart.insert(2,'labels',labels)

dfPart.head(2)

dfPart = dfPart.drop(['year','ids','title','wordOccurance'],axis=1)

Select only those texts, which contain the german word for war `Krieg`

dfWar = dfPart[dfPart.text.str.contains('\sKrieg\s')]

dfWar.shape

Export this dataset to JSON line format. 

dataLAbels = pd.read_json('./data/doccano_corpus.json1',lines=True)

dfWar.to_json('./data/warCorpusTucholsky.jsonl',orient='records',lines=True)


dfWar[dfWar.textLength < 3000]

dfWar.labels.iloc[0] = dataLAbels.labels.iloc[0]

dfWar[dfWar.textLength < 3000][:100].to_json('./data/warCorpusTucholsky.jsonl',orient='records',lines=True)

