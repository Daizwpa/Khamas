from utils.image_core import imread, imresize, imrotate
from skimage import exposure


class PreProcess:

    def __init__(self, new_size_x, new_size_y, rotate) -> None:
        self.size_x = new_size_x
        self.size_y = new_size_y
        self.rotate = rotate

    def process(self, path):
        image = None
        try:
            image = imread(path=path)
            image = imresize(image=image, size_x=self.size_x,
                             size_y=self.size_y)
            image = imrotate(image=image, r=self.rotate)
            image = exposure.adjust_log(image=image)
        except:
            raise
        return image
