def get_vecs(data: str, separator: str = ";"):
    lines = data.splitlines(keepends=False)
    res = []
    for i in lines:
        tmp = i.split(sep=separator)
        res.append(tmp)
    return res
