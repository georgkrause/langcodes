from importlib.resources import files


DATA_ROOT = files('langcodes').joinpath('data')


def data_filename(filename: str) -> str:
    return str(DATA_ROOT / filename)
