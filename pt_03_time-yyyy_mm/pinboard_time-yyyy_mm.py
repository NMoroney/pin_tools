# [2503] n8
#

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


print("pinboard time :")

path_json = "../pt_02_split_json/"
name_json = "nviii-pinboard_export.2024.12.07_01.04_b.json"

df = pd.read_json(path_json + name_json)

# print(df)

yms = {}
for i, time_ in enumerate(df['time']):
    ym = time_.split('-')
    ym_txt = ym[0] + '_' + ym[1]
    if ym_txt in yms.keys():
        yms[ym_txt] += 1
    else :
        yms[ym_txt] = 1

# print(yms)

plt.scatter(yms.keys(), yms.values())
plt.xlabel("Year and Month")
plt.ylabel("Pins per Month")

keys = list(yms.keys())
plt.xticks(keys[::12], rotation=45)
plt.subplots_adjust(bottom=0.2)
ax = plt.gca()
ax.invert_xaxis()

plt.savefig("temp_01.png")
# plt.show()


