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
folder_path = r"\\192.168.0.31\e\2021_AI_hub_project_data\★AI_hub_Project\Dataset\데이터셋 parsing본(yolov4)\★2022.1.11_Final_dataset\img"
names_file = "D:/docker-darknet-yolov3-yolov4-training-test/construction_final/valid_txt.txt"
output_folder =r"\\192.168.0.31\e\2021_AI_hub_project_data\★AI_hub_Project\Dataset\데이터셋 parsing본(yolov4)\★2022.1.11_Final_dataset\tts_out"

extract_files(folder_path, names_file, output_folder)

