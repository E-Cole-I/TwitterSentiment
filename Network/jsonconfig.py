
# Database Information pulled from external file
def json_config(file_path):
    import json
    with open(file_path) as json_data_file:
        data = json.load(json_data_file)
    return data

