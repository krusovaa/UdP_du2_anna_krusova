# Dělení adresních bodů

Tento program dělí metodou quadtree data (body) do skupin tak, aby žádná skupina něměla více než 50 jednotek (bodů). Načte vstupní data, rozdělí je, ke každé jednotce přidá informaci, do které skupiny patří a jednotky zapíše do výstupního souboru.

## Vstup a výstup

Vstupem je soubor s názvem `input.geojson`, který je uložen ve formátu GeoJSON jako FeatureCollection bodů. V tom samém formátu je zapisován výstup s názvem `output.geojson` a přidaným atributem `cluster_id`, jež určuje náležitost k danému kvadrantu.

## Funkce

* **add_cluster_id(feature, cluster_id)**

Každému bodu z vstupních dat `feature` přidá atribut `cluster_id`.

* **get_breakpoints(features)**

Z vstupních dat vytvoří dva seznamy souřadnic (x a y) a z každého vybere minimální a maximální hodnotu, spočítá pro oba střední hodnotu a tyto hodnoty vrátí.

* **split_features(features, x_mid, y_mid)**

Rozdělí jednotlivé prvky vstupních dat do 4 seznamů (kvadranty) podle jejich vztahu ke středu osy x a y `x_mid`, `y_mid` a přidá jim atribut `cluster_id` dle příslušného kvadrantu. Vrací seznamy prvků v jednotlivých kvadrantech.

* **quad_tree(features, output_list, x_mid, y_mid, x_qlen, y_qlen, quad)**

Pokud je v jednom kvadrantu více než 50 prvků, dělí dále tento kvadrant na čtvrtiny pomocí změny hodnoty geometrického středu. Ten je tvořen přičítáním resp. odčítáním poloviny délky předchozího kvadrantu. Je zavolána funkce `split_features` a následně rekurzivně funkce `quad_tree`. Pokud je v kvadrantu není více než 50 prvků, jsou data zapsána do seznamu `output_list`.
