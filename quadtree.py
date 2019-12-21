def add_cluster_id(feature, cluster_id):
    if 'cluster_id' not in feature['properties']:
        feature['properties']['cluster_id'] = ''
    feature['properties']['cluster_id'] += cluster_id

def get_breakpoints(input):
    coordinates = []
    for coordinate in input['features']:
        xy = coordinate['geometry']['coordinates']
        coordinates.append(xy)
    coordinates.sort(key=lambda p: p[0])
    x_min = coordinates[0][0]
    x_max = coordinates[-1][0]
    coordinates.sort(key=lambda p: p[1])
    y_min = coordinates[0][1]
    y_max = coordinates[-1][1]
    return x_min, x_max, y_min, y_max




