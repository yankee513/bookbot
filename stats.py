
def count_words(txt):
    return len(txt.split())


def count_letters(txt):
    txt = txt.lower()
    chars = set(txt)
    d = {c : txt.count(c) for c in chars}
    return d

def sort_dict(d):
    "Returns an array of dictionaries based on their item counts..."
    char_index = [{"char" : c, "num" : n} for c,n in d.items() if c.isalpha()] # Easy...
    sf = lambda x : x["num"]
    char_index.sort(key=sf,reverse=True)
    return char_index
