import string
import re
import csv
def remove_punct(text):
    table = str.maketrans("", "", string.punctuation)
    return text.translate(table)


all_data = []
with open('./datasets/law/test.csv', 'r', encoding="utf8") as csvfile:
     aspectreader = csv.reader(csvfile, delimiter=',')
     j = 0
     count = 0

     for row in aspectreader:
        if j == 0:
            j = 1
        else:
            sent = row[0].lower()
            # print(sent)

            sent = remove_punct(sent)
            sent.replace('\d+', '')
            # sent.replace(r'\b\w\b', '').replace(r'\s+', ' ')
                    # sent.replace('\s+', ' ', regex=True)
                    # sent=re.sub(r"^\s+|\s+$", "", sent), sep='')
            sent = re.sub(r"^\s+|\s+$", "", sent)
                    # nb_aspects = int(row[1])
            aspect = row[1].lower()
            start = int(row[3])
            end = int(row[4])
            sent_new = sent[0:start] + '$T$' + sent[end:]
            polarity = row[2]
            # print(sent)
            all_data.append(sent_new)
            all_data.append(aspect)
            all_data.append(polarity)
with open('your_file.txt', 'w') as f:
    for item in all_data:
        print("sdfghj")
        f.write("%s\n" % item)
