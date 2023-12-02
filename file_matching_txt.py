import os
import shutil

def extract_files(folder_path, names_file, output_folder):
    # Read the names from the file
    with open(names_file, 'r') as file:
        names_to_extract = [line.strip() for line in file]

    # Get the list of files in the folder
    files_in_folder = os.listdir(folder_path)

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Extract matched files
    for filename in files_in_folder:
        for extracted_file_name in names_to_extract:
            if filename in extracted_file_name:
                source_path = os.path.join(folder_path, filename)
                destination_path = os.path.join(output_folder, filename)
                shutil.copyfile(source_path, destination_path)
                print(f"File '{filename}' copied to '{output_folder}'.")

# Example usage
folder_path = "D:/docker-darknet-yolov3-yolov4-training-test/construction_final/img"
names_file = "D:/docker-darknet-yolov3-yolov4-training-test/construction_final/valid_text_split.txt"
output_folder ="D:/docker-darknet-yolov3-yolov4-training-test/construction_final/out"

extract_files(folder_path, names_file, output_folder)
