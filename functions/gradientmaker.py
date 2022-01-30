import re
from PIL import Image, ImageDraw
from functions.generate_random_string import generate_random_string

letter_colors = {
    'а': [249, 11, 16],
    'б': [124, 86, 81],
    'в': [135, 61, 36],
    'г': [124, 139, 134],
    'д': [70, 44, 50],
    'е': [2, 87, 229],
    'ё': [3, 154, 189],
    'ж': [234, 177, 5],
    'з': [81, 208, 44],
    'и': [4, 121, 175],
    'й': [7, 99, 147],
    'к': [123, 39, 26],
    'л': [221, 226, 115],
    'м': [248, 89, 4],
    'н': [7, 151, 61],
    'о': [239, 238, 231],
    'п': [194, 193, 182],
    'р': [57, 42, 50],
    'с': [184, 223, 128],
    'т': [81, 84, 93],
    'у': [228, 218, 0],
    'ф': [53, 33, 140],
    'х': [204, 197, 156],
    'ц': [180, 204, 100],
    'ч': [207, 132, 62],
    'ш': [175, 158, 129],
    'щ': [167, 130, 106],
    'ъ': [68, 63, 71],
    'ы': [64, 45, 40],
    'ь': [215, 214, 203],
    'э': [120, 79, 248],
    'ю': [240, 152, 7],
    'я': [238, 1, 76]
}


def text_to_gradient(text, amount):
    symbols = ''.join(re.findall(r'[а-яА-Я]', text)).lower()
    letters = set(symbols)
    occurrence = {}
    for letter in letters:
        occurrence[letter] = symbols.count(letter)
    sorted_occurence = {}
    sorted_keys = sorted(occurrence, key=occurrence.get)

    for w in sorted_keys:
        sorted_occurence[w] = occurrence[w]
    colors = [tuple(letter_colors[i]) for i in list(sorted_occurence.keys())][-amount:]

    image_height, image_width = 1080, 1920
    image = Image.new('RGB', (image_width, image_height), 'white')
    draw = ImageDraw.Draw(image)

    one_gradient_width = int(image_width / (amount - 1))
    for i in range(amount):
        if i < amount - 1:
            current_color, desired_color = colors[i], colors[i + 1]
            r_diff, g_diff, b_diff = desired_color[0] - current_color[0], \
                                     desired_color[1] - current_color[1], \
                                     desired_color[2] - current_color[2]
            r_step, g_step, b_step = r_diff / one_gradient_width, \
                                     g_diff / one_gradient_width, \
                                     b_diff / one_gradient_width
            c_r, c_g, c_b = current_color
            for j in range(one_gradient_width):
                draw.line((i * one_gradient_width + j, 0, i * one_gradient_width + j, image_height),
                          (int(c_r), int(c_g), int(c_b)))
                c_r += r_step
                c_g += g_step
                c_b += b_step

    path = generate_random_string(9)
    image.save(f'static/pictures/{path}.png')

    return path
