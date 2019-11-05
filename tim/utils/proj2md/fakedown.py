def level(n: int, text: str) -> str:
    return '#' * n + ' ' + text


def code(prefix: str, code: str) -> str:
    rv = f"```{prefix}\n" \
         f"{code}\n" \
         f"```" \
         "\n"
    return rv


def text(t: str) -> str:
    return t


def dump_file(prefix: str, filename: str) -> str:
    try:
        with open(filename, 'rt') as ifp:
            text = ''.join(n for n in ifp.readlines())
            return code(prefix, text)
    except Exception as e:
        return ""
