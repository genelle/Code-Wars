#Stop gninnipS My sdroW!
#http://www.codewars.com/kata/stop-gninnips-my-sdrow/

def spin_words(sentence):
    words = sentence.split()
    for index in range(len(words)):
        if len(words[index]) < 5:
            continue
        else:
            words[index] = words[index][::-1]
            
    return " ".join(words)