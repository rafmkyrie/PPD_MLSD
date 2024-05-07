import pickle
import json



# Open the pickle file for reading in binary mode
with open('data/Olympic/raw.pickle', 'rb') as file:
    # Load the data from the pickle file
    data = pickle.load(file)


#print(data)


#0/0
# Now you can work with the data as needed
print("len test_ind:", len(data['test_ind']))
print("len val_ind:", len(data['val_ind']))
print("len texts:", len(data['texts']))
print("len train_ind:", len(data['train_ind']))
print("len info:", len(data['info']))
print(data.keys())

#print(data)


print(data['info'])
