import re
import collections
import os
from nltk.corpus import wordnet as wn


def unfilt(x):
    if 'image' in x or 'caption' in x or 'website' in x:
        return True
    return False

vocab = []
pvocab=[]
lvocab=[]

for name in ["train", "valid", "test"]:
    box_label, box_pos, box_word = [], [], []
    boxg,boxs,rows=[],[],[]
    boxg_word,boxg_label,boxg_pos,boxs_word,boxs_label,boxs_pos,summary=[],[],[],[],[],[],[]
    nums = [0] * 1000
    maxlen1 = 0
    with open("original_data/" + name + ".summary", 'r', encoding='utf-8') as f1, \
            open("original_data/" + name + ".box",'r', encoding='utf-8') as f2:
        num=0
        for text, box in zip(f1, f2):
            num+=1
            #print(num)
            # text=' '.join([w.strip() for w in re.findall(pat,text.strip().lower())])
            #word=['name','birthdate','birthname','birthplace','deathdate','deathplace','']
            text =' '.join(text.strip().lower().split())
            item = box.strip().lower().replace('|name','name').replace('|birth_date','birth_date').split('\t')
            box_single_word, box_single_label, box_single_pos = [], [], []
            box_s_l,box_s_p,box_s_w=[],[],[]
            row_label=[]
            row_slabel=[]
            boxg_single_word,boxg_single_label,boxg_single_pos,boxs_single_word,boxs_single_label,boxs_single_pos,summary_s=[],[],[],[],[],[],[]
            for it in item:
                if len(it.split(':')) > 2:
                    continue
                # print it
                prefix, word = it.split(':')
                if '<none>' in word or word.strip()=='' or prefix.strip()=='':
                    continue
                new_label = re.sub("_[1-9]\d*$", "", prefix)
                new_label=new_label.replace('_','')
                if '|' in new_label:
                    new_label = new_label.split('|')[-1]
                if new_label.strip() == "":
                    continue
                if unfilt(new_label.strip()):
                    continue
                sin_pos=1
                if re.search("_[1-9]\d*$", prefix):
                    field_id = int(prefix.split('_')[-1])
                    sin_pos = field_id if field_id <= 30 else 30
                    #box_single_pos.append(field_id if field_id <= 30 else 30)
                else:
                    #box_single_pos.append(1)
                    sin_pos = 1
                if new_label.strip() not in row_slabel:
                    row_slabel.append(new_label.strip())
                box_single_word.append(word.strip().split()[0])
                box_single_label.append(new_label.strip())
                box_single_pos.append(sin_pos)

            if not len(box_single_label)==len(box_single_pos)==len(box_single_word):
                print(len(box_single_label),len(box_single_pos),len(box_single_word),
                      '\n\t',box_single_label,'\n\t',box_single_pos,'\n\t',box_single_word)

            #print(all_types)
            for type in row_slabel:
                if not type in box_single_label:
                    continue
                else:
                    i=0
                    rpw=[]
                    lp,ll=[],[]
                    while i<len(box_single_label):
                        if box_single_label[i]==type and "<none>" not in box_single_word[i]:
                            ll.append(box_single_label[i])
                            lp.append(str(box_single_pos[i]))
                            #rpw.append(box_single_word[i])
                            rpw.append(box_single_word[i])
                        i += 1
                    vocab.extend(rpw)
                    lvocab.extend(ll)
                    pvocab.extend(lp)
                    if len(rpw)>maxlen1:
                        maxlen1=len(rpw)
                    if len(rpw)>130: print(num,len(rpw),type)
                    nums[len(rpw)]+=1
                    row_label.append(type)
                    boxg_single_label.append(' '.join(ll))
                    boxg_single_pos.append(' '.join(lp))
                    boxg_single_word.append(' '.join(rpw))
            lvocab.extend(row_label)
            boxg.append('|&|'.join(boxg_single_label)+"<\sp>"+'|&|'.join(boxg_single_pos)+"<\sp>"+
                        '|&|'.join(boxg_single_word))
            #row_label.append('supplement')
            rows.append(' '.join(row_label))
            summary.append(text)
            vocab.extend(text.split())
    print(maxlen1, nums)
    with open("prepro3/"+name+".infobox",'w',encoding='utf-8') as w:
        w.write('\n'.join(boxg))
    del boxg
    with open("prepro3/" + name + ".row.label", 'w', encoding='utf-8') as w:
        w.write('\n'.join(rows))
    with open("prepro3/" + name + ".summary", 'w', encoding='utf-8') as w:
        w.write('\n'.join(summary))

b = collections.Counter(vocab)
vocab = b.most_common(30000)
#print(len(vocab), vocab[19900:])
with open("prepro3/vocab", 'w', encoding='utf-8') as out:
    out.write('<pad>' + ' ' + '0\n')
    out.write('<unk>' + ' ' + '0\n')
    out.write('<s>' + ' ' + '0\n')
    out.write('</s>' + ' ' + '0\n')
    i = 0
    for word, id in vocab:
        i += 1
        out.write(word + ' ' + str(id) + '\n')
    print(i)

b = collections.Counter(lvocab)
vocab = b.most_common(len(b))
#print(len(vocab), vocab[19900:])
with open("prepro3/label.vocab", 'w', encoding='utf-8') as out:
    out.write('<pad>' + ' ' + '0\n')
    out.write('<unk>' + ' ' + '0\n')
    i = 0
    for word, id in vocab:
        i += 1
        out.write(word + ' ' + str(id) + '\n')
    print(i)

b = collections.Counter(pvocab)
vocab = b.most_common(len(b))
#print(len(vocab), vocab[19900:])
with open("prepro3/pos.vocab", 'w', encoding='utf-8') as out:
    out.write('<pad>' + ' ' + '0\n')
    out.write('<unk>' + ' ' + '0\n')
    i = 0
    for word, id in vocab:
        i += 1
        out.write(word + ' ' + str(id) + '\n')
    print(i)


