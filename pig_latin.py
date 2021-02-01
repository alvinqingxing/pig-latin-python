def pig_latin(sentence):
	pig_latin_text = []
	word_list = sentence.split()
	for word in word_list:
		pig_latin_text.append(word[1:] + word[0] + "ay")
	return " ".join(pig_latin_text)