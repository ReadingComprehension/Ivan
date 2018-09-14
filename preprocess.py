import glob
import os
import json
import pynlpir
from nltk.tokenize import sent_tokenize, word_tokenize
import warnings

warnings.filterwarnings('ignore')
def sent_word_tokenize(text):
    sents = sent_tokenize(text)
    words = [word_tokenize(s) for s in sents]
    return words

def wd_tokenize(text):
    pynlpir.open(encoding_errors='ignore')
    segments = pynlpir.segment(text)
    segs = [b[0] for b in segments]
    pynlpir.close()
    return segs

def answer_index(answer,options):
    if answer == options[0]:
        return 0
    elif answer == options[1]:
        return 1
    else:
        return 2

'''
将原始json中的数据分词分句,并且将答案映射成index形式,生成新.json文件存储在data/RC/sequence中
'''

def preprocess(task):
    print('Preprocessing the dataset ' + task + '...')
    data_names = ['test']
    for data_name in data_names:
        data_all = []
        path = os.path.join('data', task, data_name)
        with open(path + '.json', 'r', encoding='utf-8') as fpr:
            for line in fpr.readlines():
                data_raw = json.loads(line)
                instance = {}
                instance['q_id'] = data_raw['query_id']
                instance['article'] = [wd_tokenize(s.strip()) for s in sent_tokenize(data_raw['passage'])]
                instance['question'] = wd_tokenize(data_raw['query'])
                instance['options'] = [wd_tokenize(option) for option in data_raw['alternatives'].split('|')]
                if data_name != 'test':
                    instance['ground_truth'] = answer_index(data_raw['answer'],data_raw['alternatives'].split('|'))
                data_all.append(instance)
                if len(data_all) % 1000 == 0:
                    print(len(data_all))
        with open(os.path.join('data', task, 'sequence', data_name)+'.json', 'w', encoding='utf-8') as fpw:
            json.dump(data_all, fpw,ensure_ascii=False)

if __name__ == '__main__':
    preprocess('RC')
