# [2503] n8
#

#
# * over-writing a url will update contents of the original pinboard
#   content without warning. use below to retrieve original data when accidentally
#   used same url for [2503] and [2403] . . . 
#

import pandas as pd


print("process pinboard :")


df = pd.read_json("../nviii-pinboard_export.2024.12.07_01.04.json")

print(df)
print(df.columns)

for i, url in enumerate(df['href']):
    if url.endswith("evening"):
        print(df.iloc[i])
        extended = df.at[i, 'extended']
        print(extended)

