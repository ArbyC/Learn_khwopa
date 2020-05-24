class Reverser(str):
    def __init__(self, sentence):
        self.sentence = sentence

    def reverser(self):
        return ' '.join(self.sentence.split(' ')[::-1])
