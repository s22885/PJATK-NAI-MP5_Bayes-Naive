import io
import os.path


def data_load(data: str):
    if os.path.isfile(data):
        return [True, open(data, encoding="utf-8").read()]
    return [False]

