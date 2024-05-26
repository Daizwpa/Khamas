
import skimage as ski
import CV2 as cv
import os
from skimage.transform import resize


def imread(path):
    """read image

    Args:
        path (str): path of image in hard disk

    Raises:
        Exception: Exception if the image does not exist
    """
    image = None
    if os.path.exists(path=path):
        image = cv.imread(path)
    else:
        raise Exception("There is no image in this path " + path)

    return image


def imresize(image, size_x, size_y):
    """resize image 

    Args:
        image (ndarry): 2D image
        size_x (int): x dimension 
        size_y (int): y dimension

    Returns:
        ndarray: image with new size (size_x, size_y)
    """
    try:
        image = resize(image=image, output_shape=(size_x, size_y), )
        pass
    except:
        pass
    pass
    return image
