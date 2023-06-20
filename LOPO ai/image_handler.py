from PIL import Image, ImageDraw


class imageHandler():
    def read_image(self, image):
        # open a image, read it and put the pixels (rgb) in a list. [<- y[<- x [^r^,^g^,^b^]]]
        im = Image.open(image)
        pix = im.load()
        image = []
        for y in range(im.size[1]):
            image.append([])
            for x in range(im.size[0]):

                image[y].append(list(pix[x, y]))
        return [im.size, image]

    def image_to_one_zero(self, image):
        for y in range(len(image)):
            for x in range(len(image[y])):
                # make every pixel one value & make every pixel a value between 0 and 1
                image[y][x] = image[y][x] / 255
        return image

    def one_zero_to_image(self, image):
        for y in range(len(image)):
            for x in range(len(image[y])):
                c = round(image[y][x] * 255)
                image[y][x] = [c, c, c]
        return image

    def write_image(self, loc, image, s, rotate, flip):
        img = Image.new(mode="RGBA", size=(s[0], s[0]), color='black')
        img_draw = ImageDraw.Draw(img)
        for y in range(len(image)):
            for x in range(len(image[y])):
                c = image[y][x]
                img_draw.point((x+1, y+1), fill=(c, c, c))
        img = img.rotate(rotate)
        if flip:
            img = img.transpose(Image.FLIP_LEFT_RIGHT)
        # img.show()
        img.save(loc)

    def make_image_full_list(self, image):
        newlist = []
        for y in range(len(image)):
            for x in range(len(image[y])):
                newlist.append(image[y][x])
        return newlist
