# import os

# def check_file_in_folder(folder_path, target_file):
#     # Get the list of files in the folder
#     files_in_folder = os.listdir(folder_path)

#     # Check if the target file exists in the folder
#     if target_file in files_in_folder:
#         print(f"The file '{target_file}' exists in the folder.")
#     else:
#         print("List of files in the folder:")
#         for file in files_in_folder:
#             print(file)

# # Example usage
# folder_path ="D:/docker-darknet-yolov3-yolov4-training-test/construction_final/out_folder"
# target_file = "D:/docker-darknet-yolov3-yolov4-training-test/construction_final/valid.txt"

# check_file_in_folder(folder_path, target_file)




import os
import shutil

def save_file_if_not_exist(folder_path, target_file):
    # Get the list of files in the folder
    files_in_folder = os.listdir(folder_path)

    # Check if the target file exists in the folder
    if target_file in files_in_folder:
        print(f"The file '{target_file}' exists in the folder.")
    else:
        print(f"The file '{target_file}' does not exist in the folder.")
        print("Saving content to a new file with the target name.")

        # Get the content of the target file
        with open(target_file, 'r') as source_file:
            content = source_file.read()

        # Save the content to a new file in the specified folder
        new_file_path = os.path.join(folder_path, os.path.basename(target_file))
        with open(new_file_path, 'w') as new_file:
            new_file.write(content)

        print(f"Content saved to '{new_file_path}'.")

# Example usage
folder_path = "D:/docker-darknet-yolov3-yolov4-training-test/construction_final/out_folder"
target_file = "D:/docker-darknet-yolov3-yolov4-training-test/construction_final/valid.txt"

save_file_if_not_exist(folder_path, target_file)

