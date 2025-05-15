# path = ["moves", 1, "power"]
def queryJson(data, path):
    for key in path:
        data = data[key]
    return data