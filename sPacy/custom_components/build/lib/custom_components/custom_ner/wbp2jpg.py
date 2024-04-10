#!/usr/bin/env python3

from PIL import Image

# Open webp image with alpha
im = Image.open('0_gf31eNP4WQHowZP9.webp')

# Make same size white background to paste it onto
bg = Image.new('RGB', im.size, 'white')

# Paste the webp with alpha onto the white background
bg.paste(im, im)
bg.save('result.jpg')
