word="ziyad"
reverse_word=" "
print(len(word))
for i in range(len(word)-1,-1,-1):
    reverse_word=reverse_word+word[i]+" "
print(reverse_word)