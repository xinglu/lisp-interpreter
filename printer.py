from mal_types import MalType, MalSymbol, MalNumber, MalList


def pr_str(obj):

    if isinstance(obj, MalSymbol):
        return str(obj.value)
    elif isinstance(obj, MalNumber):
        return str(obj.value)
    elif isinstance(obj, MalList):
        return obj.p_type[0] + " ".join([pr_str(i) for i in obj]) + obj.p_type[1]
    else:
         return str(obj)