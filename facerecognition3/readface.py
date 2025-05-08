import pickle

# Specify the path to the binary file
file_path = 'face_recognition.db-x-users-1-face_encoding.bin'

# Open the file in binary read mode
with open(file_path, 'rb') as file:
    # Load the data using pickle
    face_encoding = pickle.load(file)

# Print or inspect the deserialized data
print(face_encoding)
