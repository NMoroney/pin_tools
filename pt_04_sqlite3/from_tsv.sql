.mode tabs
.import nviii-pinboard_export.2024.12.07_01.04_b.tsv pins
PRAGMA table_info(pins);
SELECT description FROM pins WHERE description LIKE '%3d%';
.save pins_nviii.db
