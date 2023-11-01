#ex3

def serpentine(image_path):
    with open(image_path, "rb") as file:
        image_data = file.read()
    width, height = 0, 0

    for i in range(len(image_data) - 1):
        if image_data[i] == 0xFF and image_data[i + 1] == 0xC0:
            height, width = image_data[i + 5] * 256 + image_data[i + 6], image_data[i + 7] * 256 + image_data[i + 8]
            break

    if width == 0 or height == 0:
        raise ValueError("Not founded dimension.")

    serpentine_data = bytearray(len(image_data))

    row_length = width * 3  #

    for row in range(height):
        if row % 2 == 0:
            serpentine_data[row * row_length:(row + 1) * row_length] = image_data[row * row_length:(row + 1) * row_length]
        else:
            serpentine_data[row * row_length:(row + 1) * row_length] = image_data[(row + 1) * row_length - row_length:row * row_length - row_length:-1]

    return bytes(serpentine_data)

# Example
image_path = "photo_alexia.jpeg"
serpentine_data = serpentine(image_path)
