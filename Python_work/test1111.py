import locale
locale.setlocale(locale.LC_ALL, 'C')

import tesserocr

image = tesserocr.file_to_text('Jietu20190714-171332.jpg')
print(image)
