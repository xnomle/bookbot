
def count_word(text):
    return len(text.split())

def each_char(book):
    lower = book.lower()
    d = {}
    for char in lower:
            d[char] = d.get(char,0) + 1          
    return d 

def sort_on(items):
    return items["num"]

def sorted_dict(d):
     result_list = []    
     for character, count in d.items():
          if character.isalpha():
               result_list.append({"char":character, "num": count})     
     result_list.sort(reverse=True, key=sort_on)
     return result_list         
