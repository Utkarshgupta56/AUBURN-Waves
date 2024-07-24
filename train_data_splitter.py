import os
import shutil
import pandas as pd

# Paths
csv_file_path = 'train.csv'
images_folder_path = 'train_dataset/train_dataset'
output_folder_path = 'train_dataset'

# Create output directory if it doesn't exist
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# Read the CSV file
df = pd.read_csv(csv_file_path)

# Iterate over each row in the CSV
for index, row in df.iterrows():
    file_name = row['File Name']
    class_name = row['Class']
    
    # Create class directory if it doesn't exist
    class_folder_path = os.path.join(output_folder_path, class_name)
    if not os.path.exists(class_folder_path):
        os.makedirs(class_folder_path)
    
    # Source file path
    src_file_path = os.path.join(images_folder_path, file_name)
    
    # Destination file path
    dest_file_path = os.path.join(class_folder_path, file_name)
    
    # Copy file
    shutil.copy(src_file_path, dest_file_path)

print('Images have been separated into individual class folders.')
