import os
import shutil
from sklearn.model_selection import train_test_split

# Paths
data_dir = r"C:\Users\LENOVO\Desktop\pro\img_khanom"
train_dir = r"C:\Users\LENOVO\Desktop\pro\img\train"
val_dir = r"C:\Users\LENOVO\Desktop\pro\img\val"

# Create train and val directories if they don't exist
os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)

# Get the list of classes
classes = [d for d in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, d))]

# Loop over each class
for class_name in classes:
    class_path = os.path.join(data_dir, class_name)
    images = [
        f for f in os.listdir(class_path) if os.path.isfile(os.path.join(class_path, f))
    ]

    # Split images into train and validation sets
    train_images, val_images = train_test_split(images, test_size=0.2, random_state=42)

    # Create class directories in train and val folders
    train_class_dir = os.path.join(train_dir, class_name)
    val_class_dir = os.path.join(val_dir, class_name)
    os.makedirs(train_class_dir, exist_ok=True)
    os.makedirs(val_class_dir, exist_ok=True)

    # Move images to respective directories
    for image in train_images:
        shutil.move(
            os.path.join(class_path, image), os.path.join(train_class_dir, image)
        )

    for image in val_images:
        shutil.move(os.path.join(class_path, image), os.path.join(val_class_dir, image))

print("Dataset split into train and val folders successfully.")
