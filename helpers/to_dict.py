def to_dict(content):
    list_of_dicts = []
    for item in content:
        if not item:
            continue
        d = {
            'question': item[0],
            'answers': [i for i in item[1:]]
        }
        list_of_dicts.append(d)

    return list_of_dicts
