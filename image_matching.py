import os

def compare_image_and_text_filenames(folder_path):
    image_filenames = []
    text_filenames = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") :
            image_filenames.append(filename)
        elif filename.endswith(".txt"):
            text_filenames.append(filename)

    matching_filenames = []
    for image_filename in image_filenames:
        image_basename, _ = os.path.splitext(image_filename)

        for text_filename in text_filenames:
            text_basename, _ = os.path.splitext(text_filename)

            if image_basename == text_basename:
                matching_filenames.append((image_filename, text_filename))

    return matching_filenames

if __name__ == "__main__":
    folder_path = r"D:\docker-darknet-yolov3-yolov4-training-test\construction_final\img"
    matching_filenames = compare_image_and_text_filenames(folder_path)
    print(matching_filenames)
