def rev_sentence(sentence):
    
    words = sentence.split(' ')
    
    reverse_sentence = ' '.join(reversed(words))
    
    return reverse_sentence
if __name__ == "__main__":
    input = 'geeksforgeeks is the only website developed for computer science and engineering student'
    print (rev_sentence(input))
    