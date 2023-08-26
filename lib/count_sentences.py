#!/usr/bin/env python3

class MyString:
    def __init__(self, value):
        if not isinstance(value, str):
            raise TypeError("The value must be a string.")
        self.value = value

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):
        sentences = re.split(r'[.!?]', self.value)
        sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
        return len(sentences)
