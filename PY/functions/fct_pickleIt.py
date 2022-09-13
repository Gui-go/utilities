import pickle

def save_obj(obj_to_save, file_path):
    with open(file_path, 'wb') as file: # Opens an object and configures it to write bytes
        pickle.dump(obj_to_save, file) # Pickles (saves) the object
    
def load_obj(file_path):
    with open(file_path, 'rb') as file:
        return pickle.load(file)

if __name__ == '__main__':
    test_obj = {1: 'a', 2: 'b', 3: 'c'}
    save_obj(test_obj, 'test_obj.pickle')
    recovered = load_obj('test_obj.pickle')
    print(recovered)
    print("----------------------")
    test_obj2 = [1, "2", "três", "LET'S GO!"]
    save_obj(test_obj2, 'test_obj2.pickle')
    recovered = load_obj('test_obj2.pickle')
    print(recovered)



# test_obj = {1: 'a', 2: 'b', 3: 'c'}
# save_obj(test_obj, 'test_obj.pickle')
# recovered = load_obj('test_obj.pickle')
# print(recovered)