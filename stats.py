def number_of_words(text):
    num_words = 0
    text_split = text.split()
    num_words += len(text_split)
    return num_words

def count_of_characters(character):
    character_counter = {}
    lower_case = character.lower()

    for words in lower_case:
        for character in words:
            if character in character_counter:
                character_counter[character] += 1
            else:
                character_counter[character] = 1
    return character_counter

def sort(items):
    return items["num"]

def report(dictionary):
    s_list = []
    
    for k, v in dictionary.items():
        tmp_dict = {"char": k, "num": v}
        s_list.append(tmp_dict)
        
    s_list.sort(reverse=True, key=sort) 
    return s_list