
def reverse(sentence, reverse_word):
    if type(reverse_word) != str:
        return "invalid input"
    if reverse_word in sentence:
        listSentence = sentence.split()
        indexWord = listSentence.index(reverse_word)
        newWord = []
        number = len(reverse_word)-1
        number2 = 0
        listSentence[indexWord] = reverse_word[::-1]
        finalSentence=""
        for word in listSentence:
            finalSentence = finalSentence + word + " "
        return(finalSentence)
    else:
        return "The word was not found"


