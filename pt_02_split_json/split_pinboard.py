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


def pin_url_ends_with(s):
    for i, url in enumerate(df['href']):
        if url.endswith("evening"):
            print(df.iloc[i])
            extended = df.at[i, 'extended']
            print(extended)


def pin_tags_include(s):
    q1 = '§'
    idx = []
    for i, ts in enumerate(df['tags']):
        if s in ts:
            idx.append(i)
            print(df.at[i, 'description'])

    print(str(len(idx)))


def pin_split_tags_dont_include(s):
    q1 = '§'
    idx = []
    for i, ts in enumerate(df['tags']):
        if s in ts:
            idx.append(i)

    df.drop(idx, inplace=True)
    df.reset_index(drop=True, inplace=True)

    print(df.columns)

    print(df)

    df.to_json("nviii-pinboard_export.2024.12.07_01.04_b.json")



# pin_url_ends_with("evening")
pin_tags_include('ⓈJC')
# pin_tags_include('§')
# pin_split_tags_dont_include('§')


