def filter_by_state(data_list, state='EXECUTED'):
    filtered_list = []

    for item in data_list:
        if item.get('state')==state:
            filtered_list.append(item)

    return filtered_list