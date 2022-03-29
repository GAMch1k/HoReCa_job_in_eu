def data_beautify_bd(data):
    if isinstance(data, str):
        return f'"{data}"'
    return f'{data}'