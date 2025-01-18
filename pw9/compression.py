import pickle
import gzip
import os

def save_data_pickle(file_name, data):
    with gzip.open(file_name, 'wb') as f:
        pickle.dump(data, f)

def load_data_pickle(file_name):
    with gzip.open(file_name, 'rb') as f:
        return pickle.load(f)

def check_and_load_data(file_name):
    if os.path.exists(file_name):
        return load_data_pickle(file_name)
    return None

