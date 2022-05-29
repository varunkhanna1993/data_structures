sentence = 'Hello my name is coolio, but I am not that cool - Aryan Dhingra.'
import re
def word_extraction(sentences ):
    words = re.sub('[^\w]', " ", sentence).split()
    ignore_words = ["a", "an", "the", "and","to","am" , "I", "but", "is"]
    cleaned_text = [w.lower() for w in words if w not in ignore_words]
    return cleaned_text

def tokenize(sentences):    
    words = []    
    for sentence in sentences:        
        w = word_extraction(sentences = sentence )        
        words.extend(w)            
    words = sorted(list(set(words)))    
    return words

print(tokenize(sentences=sentence ))