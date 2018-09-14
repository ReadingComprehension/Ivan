# coding:utf-8

import sys
import pynlpir
import  torch
import jieba
'''
with open('data/embedding/sgns.baidubaike.bigram-char', 'r',encoding= 'utf-8') as f:
    line_count = 0
    for line in f:
        if line_count != 0:
            print(line)
            vals = line.rstrip().split(' ')
            print(vals)

        line_count += 1
'''


word2idx = torch.load('C:/Users/chendiao/Desktop/AIChallenge/comatch-jieba/data/RC/idx2word.pt')
f1 = open('Dictionary','w',encoding='utf-8')
for word in word2idx:
    f1.write(str(word)+'\t')
    #f1.write(str(word2idx[word]))
    f1.write('\n')

'''
pynlpir.open()
s = "飞机在起飞和降落时是最危险的。飞中远距离的飞机所携带的燃油比较多，如果不放掉大部分燃油，着陆时对起落架等部位的冲击力太大，容易发生意外，同时燃油较少，发生事故时，火灾也不会太严。"
segments = pynlpir.segment(s)
seg = [b[0] for b in segments]

print(seg)
pynlpir.close()

segments = jieba.lcut(s,HMM=True,cut_all=False)


print(segments)
'''