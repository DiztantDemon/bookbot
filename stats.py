def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    characters = {}
    for char in text.lower():
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

def sort_on(items):
    return items["num"]

def sorted_list(items):
    dict =  {}
    for key, value in items.items():
        dict[key] = {"char": key, "num": value}
    sorted_items = sorted(dict.values(), key=sort_on, reverse=True)
    return [(item["char"], item["num"]) for item in sorted_items]