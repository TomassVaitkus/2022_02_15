import pandas as pd

open('naujas_uzduociai.txt', 'a').write(str(pd.DataFrame([{i: str(open('uzduociai.txt', 'r').read()).count(i) for i in str(open('uzduociai.txt', 'r').read())}]).transpose().reset_index().rename({'index': 'Char', 0: 'Aperence'}, axis=1).sort_values('Aperence').reset_index(drop=True)))

