import bz2file as bz2
import pickle

def decompress_pickle(file):
    data = bz2.BZ2File(file, 'rb')
    data = pickle.load(data)
    return data

model = decompress_pickle('similarity.pbz2')