import subprocess

def convert_to_bw(input_image_path, output_image_path):
    cmd = f'ffmpeg -i {input_image_path} -vf hue=s=0 {output_image_path}'
    subprocess.run(cmd, shell=True)


# Example usage:
input_image_path = "photo_alexia_compressed_ex4.jpeg"
output_image_path = "photo_alexia_bw.png"
convert_to_bw(input_image_path, output_image_path)
