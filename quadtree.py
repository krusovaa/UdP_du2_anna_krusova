def add_cluster_id(feature, cluster_id):
    if 'cluster_id' not in feature['properties']:
        feature['properties']['cluster_id'] = ''
    feature['properties']['cluster_id'] += cluster_id


def get_breakpoints(features):
    coordinates = []
    for coordinate in features['features']:
        xy = coordinate['geometry']['coordinates']
        coordinates.append(xy)
    coordinates.sort(key=lambda p: p[0])
    x_min = coordinates[0][0]
    x_max = coordinates[-1][0]
    coordinates.sort(key=lambda p: p[1])
    y_min = coordinates[0][1]
    y_max = coordinates[-1][1]
    return x_min, x_max, y_min, y_max


def split_features(features, x_mid, y_mid):
    features1 = []
    features2 = []
    features3 = []
    features4 = []
    for point in features['features']:
        coordinates = point['geometry']['coordinates']
        x = coordinates[0]
        y = coordinates[1]
        if x <= x_mid and y > y_mid:
            add_cluster_id(point, 1)
            features1.append(point)
        elif x > x_mid and y > y_mid:
            add_cluster_id(point, 2)
            features2.append(point)
        elif x <= x_mid and y <= y_mid:
            add_cluster_id(point, 3)
            features3.append(point)
        elif x > x_mid and y <= y_mid:
            add_cluster_id(point, 4)
            features4.append(point)
        # body ležící na osách jsou přidány buď do 1. nebo 4. kvadrantu
        elif x == x_mid and y > y_mid or x < x_mid and y == y_mid or x == x_mid and y == y_mid:
            add_cluster_id(point, 1)
            features1.append(point)
        elif x == x_mid and y < y_mid or x > x_mid and y == y_mid:
            add_cluster_id(point, 4)
            features4.append(point)
    return features1, features2, features3, features4


def quad_tree(features, output_list, x_mid, y_mid, x_qlen, y_qlen, q=0):

    #  input: listy features 1-4
    if len(features) < 50:
        for point in features:
            output_list.append(point)
        return output_list

    if q == 1:
        x_mid = x_mid - x_qlen
        y_mid = y_mid + y_qlen
    if q == 2:
        x_mid = x_mid + x_qlen
        y_mid = y_mid + y_qlen
    if q == 3:
        x_mid = x_mid - x_qlen
        y_mid = y_mid - y_qlen
    if q == 4:
        x_mid = x_mid + x_qlen
        y_mid = y_mid - y_qlen

    features1, features2, features3, features4 = split_features(features, x_mid, y_mid)

    quad_tree(features1, output_list, x_mid, y_mid, x_qlen/2, y_qlen/2, q=1)
    quad_tree(features2, output_list, x_mid, y_mid, x_qlen/2, y_qlen/2, q=2)
    quad_tree(features3, output_list, x_mid, y_mid, x_qlen/2, y_qlen/2, q=3)
    quad_tree(features4, output_list, x_mid, y_mid, x_qlen/2, y_qlen/2, q=4)