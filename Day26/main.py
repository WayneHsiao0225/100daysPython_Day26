import pandas as pd
data=pd.read_csv("nato_phonetic_alphabet.csv")  # type dataframe
data_dict={value.letter:value.code for (key,value) in data.iterrows()}
word_input=input("Enter a word: ").upper()
#print(type(word_input))
ans=[data_dict[i] for i in word_input]
print(ans)
