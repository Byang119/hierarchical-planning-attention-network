from nltk.corpus import wordnet as wn

def order_label(path):
    sw = [',', '.', ';', '\\', '/', '&', '-lrb-', '-rrb-', '-rsb-', '-lsb-', '--', '-', '_', 'in', 'of', 'on', '\"',
          '``', '!', ':', '?', '+', '=', 'be']
    with open(path + ".infobox", 'r', encoding='utf-8') as f1, open(path + ".row.label", 'r', encoding='utf-8') as f2, \
            open(path + +".summary", 'r', encoding='utf-8') as f3:
        ww = []
        labels = []
        for l1, l2, l3 in zip(f1, f2, f3):
            lab, pos, wo = l1.strip().split('<\sp>')
            label = ' '.join(lab.split('|&|')).split()
            word = ' '.join(wo.split('|&|')).split()
            word_ = [wn.morphy(w) for w in word]
            keys = l2.strip().split()
            w_list = []
            for w in l3.strip().split():
                w_ = wn.morphy(w)
                if w_ not in sw and w not in sw:
                    if w in word:
                        a = label[word.index(w)]
                    elif w_ and w_ in word_:
                        a = label[word_.index(w_)]
                    try:
                        if a not in w_list and a in keys:
                            w_list.append(a)
                    except:
                        continue

            for w in keys:
                if w not in w_list:
                    w_list.append(w)

            ww.append(' '.join(w_list))

    with open('ordered/' + path + ".o_label", 'w', encoding='utf-8') as o:
        o.write('\n'.join(ww))


def order_data(path):
    infobox = []
    with open(path + ".infobox", 'r', encoding='utf-8') as f1, open(path + ".row.label", 'r', encoding='utf-8') as f2, \
            open(path + ".summary", 'r', encoding='utf-8') as f3, open("ordered/" + path + ".o_label", 'r',
                                                                       encoding='utf-8') as f4:

        labels = []
        positions = []
        words = []
        ww = []
        for l1, l2, l3, l4 in zip(f1, f2, f3, f4):
            label1 = []
            position1 = []
            word1 = []
            lab, pos, wo = l1.strip().split('<\sp>')
            label = lab.split('|&|')
            position = pos.split('|&|')
            word = wo.split('|&|')

            olabel = l2.strip().split()
            rlabel = l4.strip().split()

            for item in rlabel:
                index = olabel.index(item)
                label1.append(label[index])
                position1.append(position[index])
                word1.append(word[index])
            infobox.append('|&|'.join(label1) + "<\sp>" + '|&|'.join(position1) + "<\sp>" +
                           '|&|'.join(word1))

    with open("prepro/ordered/" + path + ".infobox", 'w', encoding='utf-8') as o:
        o.write('\n'.join(infobox))

