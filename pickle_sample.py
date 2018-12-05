import pickle

a = [1, 2, 3, 4, 5]
fo = open("sample_pickle", 'wb')
pickle.dump(a, fo)
fo.close()
fo = open("sample_pickle", 'rb')
b = pickle.load(fo)
print(str(b))
print(b[2])