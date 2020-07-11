import tensorflow as tf
from PIL import Image, ImageFilter
from tensorflow.keras.models import load_model
import copy
import os
import numpy as np
WIDTH = 448  # 640
HEIGHT = 640  # 1152


class Colorizer:

    def __init__(self, generator: str, upscaler: str):
        self.generator = load_model(generator)
        self.upscale = load_model(upscaler)

    def load_img(self, url):
        img = Image.open(url)
        img = np.asarray(img, dtype=np.uint8)
        return img

    def eval(self, filename: str, title: str):

        def quantize(d):
            _ = np.asarray(d, dtype=np.int32)
            _ = np.asarray(_, dtype=np.float32)
            _ /= 127.5
            _ -= 1.0
            return _

        def resize(i):
            i = i.resize((WIDTH, HEIGHT))
            return np.asarray(i)

        comic = Image.open(filename).convert('L')
        original = copy.deepcopy(comic)
        original = original.resize((WIDTH * 2, HEIGHT * 2))
        original = np.expand_dims(original, axis=-1)
        original = np.asarray([original], dtype=np.float32)
        original /= 127.5
        original -= 1.
        comic = comic.filter(ImageFilter.GaussianBlur(2))
        title = Image.open(title)
        title = np.asarray(title)
        title = title[:, :, [2, 1, 0]]
        title = Image.fromarray(title)
        title = resize(title)
        comic = resize(comic)
        comic = np.asarray([comic], dtype=np.uint8)
        comic = np.expand_dims(comic, -1)
        comic = tf.image.adjust_gamma(comic, 1.15, 1.15)
        comic = tf.image.adjust_contrast(comic, 1.2)
        title = np.asarray([title], dtype=np.float32)
        title = tf.image.adjust_saturation(title, 1.2)
        comic = quantize(comic)
        title = quantize(title)
        output, _ = self.generator([comic, title], training=False)
        output = tf.image.adjust_saturation(output, 1.4)
        output = tf.image.adjust_contrast(output, 1.2)
        output = self.upscale([original, output], training=False)
        output = np.asarray(output, dtype=np.float32)
        output = np.where(output > 1, np.ones_like(output), output)
        output = np.where(output < 0, np.zeros_like(output), output)
        output = (output * 0.5) + 0.5
        output *= 255
        output = np.asarray(output[0], dtype=np.uint8)
        return output

    def colorize(self, title_image: str, images: [str]):
        path = os.path.split(title_image)[0]
        save_path = f"{path}/colorized"
        images.remove(title_image)
        img_total = []
        img_total.append(self.load_img(title_image))
        if not os.path.exists(save_path):
            os.mkdir(save_path)
        for i, img in enumerate(images):
            print(f"COLORIZING {img}")
            temp = self.eval(img, title_image)
            img = Image.fromarray(temp[:, :, ::-1])
            img.save(f"{save_path}/{i:06d}.jpg")
