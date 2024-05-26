import sys
import json
import requests
import numpy as np
from PIL import Image

def resize(img, new_size):
    img = Image.fromarray(img)
    img = img.resize(new_size)
    return np.array(img)