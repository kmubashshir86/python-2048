import pickle

with open("money.bin",'wb') as f:
    pickle.dump(0,f)

with open("score.txt",'w') as f:
    str='0'
    f.write(str)