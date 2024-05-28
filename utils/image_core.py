
import skimage as ski
import cv2 as cv
import os
from skimage.transform import resize, rotate
from skimage import img_as_ubyte


def imread(path):
    """read image

    Args:
        path (str): path of image in hard disk

    Raises:
        Exception: Exception if the image does not exist
    """
    image = None
    if os.path.exists(path=path):
        image = ski.io.imread(fname=path)
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
    except:
        raise
    return image


def imrotate(image, r):
    """rotate image

    Args:
        image (ndarray): image
        r (int): angler

    Returns:
        ndarray: image
    """
    try:
        image = rotate(image=image, angle=r)
    except:
        raise
    return image


def imshow(image):
    try:
        ski.io.imshow(image)
    except:
        raise


def imSave(image, path):
    """save image

    Args:
        image (ndarray): image
        path (str): path to save
    """
    try:
        image = img_as_ubyte(image)
        ski.io.imsave(fname=path, arr=image)
    except:
        raise
