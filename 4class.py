import os

label_path = '/Users/techfever/Downloads/rt/labels/train2017' 

target_classes = {0, 1, 2, 3}  # Update these to your actual class indices

for label_file in os.listdir(label_path):
    if label_file.endswith('.txt'):
        file_path = os.path.join(label_path, label_file)
        new_lines = []

        with open(file_path, 'r') as f:
            for line in f:
                parts = line.strip().split()
                class_index = int(parts[0])  # Get the class index
                
                if class_index in target_classes:
                    new_lines.append(line)  # Keep the line if it's a target class

        with open(file_path, 'w') as f:
            f.writelines(new_lines)
