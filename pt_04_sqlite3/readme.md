
## Pin Tools : Sqlite3

Import achived pins into sqlite3 and run a simple query.

First step is to transform the archive in json format to a TSV file using pandas :

```py
path_json = "../pt_02_split_json/"
name_json = "nviii-pinboard_export.2024.12.07_01.04_b.json"

df = pd.read_json(path_json + name_json)

print(df)

name_tsv = name_json[:-4] + "tsv"
df.to_csv(name_tsv, sep='\t', index=False)
```

And then this can be imported (and queried) using this file ```from_tsv.sql``` :

```sql
.mode tabs
.import nviii-pinboard_export.2024.12.07_01.04_b.tsv pins
PRAGMA table_info(pins);
SELECT description FROM pins WHERE description LIKE '%3d%';
.save pins_nviii.db
```

Which can be run from the command line as : ```sqlite3 < from_tsv.sql```.

The result of the query for descriptions that are like '3d' is :

```
3D SPACE CAN BE TILED WITH CORNER-FREE SHAPES
"Over the last decade, more than $10 Billion of outside capital was injected into 3D printing companies."
Open CASCADE Technology (OCCT) is the only open-source full-scale 3D geometry library
graphics.social : a gathering place for the computer graphics community to discuss 3D and 2D graphics, computer science, and any related topics.
RIP 3D Printing: The Cart Before the Horse
The openNURBS Toolkit consists of C++ source code for a library that will read and write openNURBS 3D model files (.3dm)
CLO : 3D Virtual Preview Garments . . . Significantly shorten your time-to-market with virtual sampling and remote collaboration.
Grasshopper: Visual Scripting for Rhinoceros 3D by David Bachman (2017)
Breaking News: Apple Explores 3D Printing for Next-Gen Watch Casings - [2309]
Stunning 3D Printed Hat from the Late Zaha Hadid
Wilson's 3D-Printed Basketball of the Future Is Full of Holes But Never Goes Flat
. . . <snip> . . . 
Shapeways 3D Printing - Make Your Ideas Real with the Shapeways 3D Printing Marketplace & Community.
Shapeways 3D printing service reaches one million objects sold
CGS to debut 3D packaging software in Hall 8b
3D Software for Lenticular Printing and 3D Photography from HumanEyes
X3D for Web Authors, Chapter 06 - Geometry Points Lines Polygons: Color Per Vertex Examples
Nokia Maps 3D WebGL (beta)
x3dom --- Instant 3D the HTML way!
Web3D Consortium | Open Standards for Real-Time 3D Communication
Mantis Vision's F5 Handheld 3D Scanner for the Field - Core77
```

