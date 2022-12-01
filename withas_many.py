with open('data') as fin, open('res', 'w') as fout:
    for line in fin:
        if 'some key' in line:
            fout.write(line)

with open('script1.py') as f1, open('script2.py') as f2:
    for pair in zip(f1, f2):
        print(pair)

