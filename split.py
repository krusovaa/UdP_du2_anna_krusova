# import funkcí
import json
import quadtree as q

# načtení vstupních dat a uložení do proměnné
with open("input.geojson", "r", encoding="utf-8") as f:
    data = json.load(f)
features = data["features"]

x_min, x_max, y_min, y_max, x_mid, y_mid = q.get_breakpoints(features)
x_qlen = abs(x_min + x_max) / 2
y_qlen = abs(y_min + y_max) / 2

quad = 0

# seznam pro výsledné body
output_list = []

output_list = q.quad_tree(features, output_list, x_qlen, y_qlen, x_mid, y_mid, quad)

# zápis do souboru
gj_structure = {'type': 'FeatureCollection', 'features': output_list}
with open("output.geojson", "w", encoding="utf-8") as f:
    json.dump(gj_structure, f, indent=2, ensure_ascii=False)
