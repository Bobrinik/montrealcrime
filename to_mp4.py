import os
import imageio
from datetime import datetime

def to_date(date_msg):
    return datetime.strptime(date_msg, '%Y-%m-%d')

png_dir = 'data_viz/.'
images = [(to_date(file_name.split(".")[0]), file_name) for file_name in os.listdir(png_dir) if file_name.endswith(".png")]
sorted_images = sorted(images, key=lambda x: x[0])

images_to_save = []
writer = imageio.get_writer('movie.mp4', fps=3)


for date_of_file, file_name in sorted_images:
    print(f"{date_of_file}-{file_name}")
    if file_name.endswith('.png'):
        file_path = os.path.join(png_dir, file_name)
        writer.append_data(imageio.imread(file_path))

writer.close()
