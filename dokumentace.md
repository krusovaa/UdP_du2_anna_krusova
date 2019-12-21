# Dělení adresních bodů

Tento program dělí metodou quadtree data (body) do skupin tak, aby žádná skupina něměla více než 50 jednotek (bodů). Vstupní data načte ze souboru `input.geojson`, rozdělí je, ke každé jednotce přidá informaci (cluster_id), do které skupiny patří a jednotky zapíše do výstupního souboru `output.geojson`.
