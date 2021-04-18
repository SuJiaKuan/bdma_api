def str2float(text):
    parsed = [t for t in text if t.isdigit() or t == "." or t == "-"]
    parsed = "".join(parsed)

    return float(parsed) if parsed else 0.0


def str2int(text):
    return int(str2float(text))
