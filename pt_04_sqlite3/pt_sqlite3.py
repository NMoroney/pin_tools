# [2503] n8
#

import pandas as pd


print("pt - sqlite3 :")

path_json = "../pt_02_split_json/"
name_json = "nviii-pinboard_export.2024.12.07_01.04_b.json"

df = pd.read_json(path_json + name_json)

print(df)

name_tsv = name_json[:-4] + "tsv"
df.to_csv(name_tsv, sep='\t', index=False)

