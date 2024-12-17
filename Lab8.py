import os
import tarfile

def create_tar_from_images(image_dir, tar_path):
    if not os.path.isdir(image_dir):
        raise FileNotFoundError(f"Директория {image_dir} не найдена.")

    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff')

    with tarfile.open(tar_path, 'w') as tar:
        for root, dirs, files in os.walk(image_dir):
            for file in files:
                if file.lower().endswith(image_extensions):
                    file_path = os.path.join(root, file)
                    tar.add(file_path, arcname=os.path.relpath(file_path, image_dir))
                    print(f"Добавлено в архив: {file_path}")


if __name__ == "__main__":
    images_directory = 'E:/lython/Thomas/Photos/'
    tar_file_path = 'E:/lython/Thomas/Archived/archive.tar'

    try:
        create_tar_from_images(images_directory, tar_file_path)
        print("Создание архива завершено.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
