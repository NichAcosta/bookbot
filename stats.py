def count_words (file):
    temp = file.split()
    count = 0
    for i in temp:
        count += 1
    return count

def character_count(file):
    counts = {}
    for ch in file:
        ch = ch.lower()
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1
                
    return counts
        
def get_num(diction):
    return diction["num"]
    
def sort_list(characters_dict):
    num = []
    for elements in characters_dict:
        num.append({"char": elements, "num": characters_dict[elements]})
    
    num.sort(reverse = True, key = get_num)
    for item in num:
        ch = item["char"]
        count = item["num"]
        if ch.isalpha() == True:
            print (f"{ch}: {count}")
            
