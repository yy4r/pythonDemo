import csv
import itertools

def read_simi_words(simi_words_path):
    original_word_simi_words={}
    with open(simi_words_path) as f:
        csv_reader= csv.reader(f)
        for row in csv_reader:
            original_word=row[0]
            simi_words= row[1].split(',')
            original_word_simi_words[original_word]=set(simi_words)
    return original_word_simi_words

def read_expand_words(need_expand_words_file_path):
    need_expand_words=set()
    with open(need_expand_words_file_path) as f :
        csv_reader = csv.reader(f)
        for row in csv_reader:
            need_expand_words.add(row[0])
    return need_expand_words

def expand_words(word, simi_words: dict):
    expands_words = set()
    for cnt, char in enumerate(word):
        new_round_words = set()
        char_simi_words = simi_words.get(char, set())
        if cnt == 0:
            new_round_words.update(char_simi_words)
        else:
            for w, c in itertools.product(expands_words, char_simi_words):
                new_round_words.add(w + c)
        expands_words = new_round_words
    return expands_words










if __name__=='__main__':
    simi_words_path=r'simi_words.csv'
    expands_words_path=r'expand_words.csv'
    output_path=r'expand_result.csv'
    csv_writer = csv.writer(open(output_path,'w'),lineterminator='\n')
    simi_words_dict = read_simi_words(simi_words_path)
    expand_words_set = read_expand_words(expands_words_path)
    for word in expand_words_set :
        expands_result=expand_words(word,simi_words_dict)
        for w in expands_result:
            csv_writer.writerow([word,w])