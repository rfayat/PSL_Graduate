"Useful helper functions"
from pathlib import Path


def convert_first_arg_to_path(f):
    "Convert the first argument of a function to a pathlib Path"

    def g(p, *args, **kwargs):
        if not isinstance(p, Path):
            p = Path(p)
        return f(p, *args, **kwargs)

    return g
