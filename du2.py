# Napište neinteraktivní program, který bude metodou quadtree dělit data do skupin tak, aby žádná skupina neměla více než 50 jednotek.
# Program načte vstupní data ze souboru input.geojson, jednotky ze vstupního souboru rozdělí do skupin pomocí algoritmu quadtree,
# ke každé jednotce přidá informaci, do které skupiny patří a jednotky s informacemi o skupinách vypíše do výstupního souboru output.geojson.
# Při programování počítejte s tím, že vstupních bodů můžou být desetitisíce.
#
# Budeme uvažovat následující variantu quadtree.
# Výchozí obdélník je bounding box množiny vstupních bodů. Pokud nějaká oblast obsahuje více než 50 bodů, rozdělí se geometricky na čtvrtiny a opět je testována na toto kritérium.
# Pokud oblast obsahuje méně než 50 bodů, dále se nedělí.