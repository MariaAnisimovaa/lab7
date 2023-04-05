def z1():
    from PIL import Image
    n = "sobaken.jpg"
    with Image.open(n) as img:
        img.load()
    img.show()
    width, height = img.size
    format = img.format
    mode = img.mode
    print("Ширина: ", width)
    print("Высота: ", height)
    print("Формат: ", format)
    print("Цветовая модель: ", mode)

def z2():
    from PIL import Image
    n = "sobaken.jpg"
    with Image.open(n) as img:
        img.load()
    n_img = img.resize((img.width // 3, img.height // 3))
    n_img.save("1_sobaken.jpg")

    nn_img = img.transpose(Image.FLIP_TOP_BOTTOM)
    nn_img.save("top_sobaken.jpg")
    nn_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    nn_img.save("left_sobaken.jpg")

def z3():
    from PIL import Image, ImageFilter
    n = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]
    for file in n:
        with Image.open(file) as img:
            img.load()
            n_img = img.filter(ImageFilter.CONTOUR)
            n_img.show()
            n_img.save("new_" + file)

def z4():
    from PIL import Image
    w = "watermark.png"
    with Image.open(w) as img_w:
        img_w.load()
    img_w = Image.open(w)
    img_w = img_w.resize((img_w.width // 2, img_w.height // 2))

    n = "sobaken.jpg"
    with Image.open(n) as img:
        img.load()

    img.paste(img_w, (300,200), img_w)
    img.save("watermark_sob.jpg")
