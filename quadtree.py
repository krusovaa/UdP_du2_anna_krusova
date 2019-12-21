def add_cluster_id(feature, cluster_id):
    if 'cluster_id' not in feature['properties']:
        feature['properties']['cluster_id'] = ''
    feature['properties']['cluster_id'] += cluster_id


def get_breakpoints(features):
    x_coordinates = []
    y_coordinates = []
    for coordinate in features:
        x_axis = coordinate['geometry']['coordinates'][0]
        y_axis = coordinate['geometry']['coordinates'][1]
        x_coordinates.append(x_axis)
        y_coordinates.append(y_axis)
    x_min = min(x_coordinates)
    x_max = max(x_coordinates)
    y_min = min(y_coordinates)
    y_max = max(y_coordinates)
    x_mid = (x_min + x_max) / 2
    y_mid = (y_min + y_max) / 2
    return x_min, x_max, y_min, y_max, x_mid, y_mid


def split_features(features, x_mid, y_mid):
    features1 = []
    features2 = []
    features3 = []
    features4 = []
    for point in features:
        coordinates = point['geometry']['coordinates']
        x = coordinates[0]
        y = coordinates[1]
        if x <= x_mid and y > y_mid:
            add_cluster_id(point, '1')
            features1.append(point)
        elif x > x_mid and y > y_mid:
            add_cluster_id(point, '2')
            features2.append(point)
        elif x <= x_mid and y <= y_mid:
            add_cluster_id(point, '3')
            features3.append(point)
        elif x > x_mid and y <= y_mid:
            add_cluster_id(point, '4')
            features4.append(point)
        # body ležící na osách jsou přidány buď do 1. nebo 4. kvadrantu
        elif x == x_mid and y > y_mid or x < x_mid and y == y_mid or x == x_mid and y == y_mid:
            add_cluster_id(point, 1)
            features1.append(point)
        elif x == x_mid and y < y_mid or x > x_mid and y == y_mid:
            add_cluster_id(point, 4)
            features4.append(point)
    return features1, features2, features3, features4


def quad_tree(features, output_list, x_mid, y_mid, x_qlen, y_qlen, quad=0):

    #  input: listy features 1-4
    if len(features) < 50:
        for point in features:
            output_list.append(point)
        return output_list

    if quad == 1:
        x_mid = x_mid - x_qlen
        y_mid = y_mid + y_qlen
    if quad == 2:
        x_mid = x_mid + x_qlen
        y_mid = y_mid + y_qlen
    if quad == 3:
        x_mid = x_mid - x_qlen
        y_mid = y_mid - y_qlen
    if quad == 4:
        x_mid = x_mid + x_qlen
        y_mid = y_mid - y_qlen

    features1, features2, features3, features4 = split_features(features, x_mid, y_mid)

    quad_tree(features1, output_list, x_mid, y_mid, x_qlen/2, y_qlen/2, quad=1)
    quad_tree(features2, output_list, x_mid, y_mid, x_qlen/2, y_qlen/2, quad=2)
    quad_tree(features3, output_list, x_mid, y_mid, x_qlen/2, y_qlen/2, quad=3)
    quad_tree(features4, output_list, x_mid, y_mid, x_qlen/2, y_qlen/2, quad=4)
