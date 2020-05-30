# Word counting function#
def word_counter(sentences):
    sentences.replace('\n', '')
    lowered_sentences = (sentences.lower()).split(' ')
    counts = {items: lowered_sentences.count(items) for items in set(lowered_sentences)}
    return counts


# Reading the count file and calling word counter#
with open('count.txt', 'r', encoding='UTF-8') as f:
    sentences = f.read()
    counted = word_counter(sentences)


# Writing the counted dictionary in a new file#
with open('count_frequency.txt', 'w', encoding='UTF-8') as f:
    for words, freq in counted.items():
        f.write(f'{words} = {freq}\n')
