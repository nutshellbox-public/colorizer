import tensorflow as tf
from PyQt5 import QtGui
from tensorflow.keras.models import load_model
import copy
import os
import cv2
import numpy as np
import sys
WIDTH = 448  # 640
HEIGHT = 640  # 1152


class Colorizer:

    def __init__(self, generator: str, upscaler: str, refiner: str):
        self.generator = load_model(generator)
        self.upscale = load_model(upscaler)
        self.refiner = load_model(refiner)

    def eval(self, filename: str, title: str):

        def quantize(d):
            _ = np.asarray(d, dtype=np.int32)
            _ = np.asarray(_, dtype=np.float32)
            _ /= 127.5
            _ -= 1.0
            return np.clip(_, -1, 1)

        def read_color_image(file: str):
            img = cv2.imread(file, cv2.IMREAD_COLOR)
            img = cv2.resize(img, (WIDTH, HEIGHT), interpolation=cv2.INTER_AREA)
            return img

        def read_bw_image(file: str):
            img = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, (WIDTH, HEIGHT), interpolation=cv2.INTER_AREA)
            return np.expand_dims(np.asarray(img), axis=-1)

        comic = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
        original = copy.deepcopy(comic)
        original = cv2.resize(original, (WIDTH * 2, HEIGHT * 2), interpolation=cv2.INTER_AREA)
        original = np.expand_dims(original, axis=-1)
        original = np.asarray([original], dtype=np.float32)
        original /= 127.5
        original -= 1.
        comic = cv2.GaussianBlur(comic, (3, 3), 3)
        title = cv2.imread(title, cv2.IMREAD_COLOR)
        title = cv2.resize(title, (WIDTH, HEIGHT), interpolation=cv2.INTER_AREA)
        comic = cv2.resize(comic, (WIDTH, HEIGHT), interpolation=cv2.INTER_AREA)
        comic = cv2.fastNlMeansDenoising(comic, None, 3, 3, 5)
        comic = np.asarray([comic], dtype=np.uint8)
        title = np.asarray([title], dtype=np.float32)
        comic = np.expand_dims(comic, -1)
        comic = tf.image.adjust_contrast(comic, 1.2)
        title = tf.image.adjust_saturation(title, 1.5)
        comic = quantize(comic)
        title = quantize(title)
        output, _ = self.generator([comic, title], training=False)
        output, _ = self.refiner([output, title], training=False)
        output = self.upscale([output, original], training=False)
        output = np.asarray(output, dtype=np.float32)
        output = np.clip(output, -1, 1)
        output = (output * 0.5) + 0.5
        output *= 255
        output = np.asarray(output[0], dtype=np.uint8)
        return output

    def colorize(self, title_image: str, images: [str], qt_window):
        path = os.path.split(title_image)[0]
        save_path = f"{path}/colorized"
        images.remove(title_image)
        img_total = []
        img_total.append(cv2.imread(title_image, cv2.IMREAD_COLOR))
        if not os.path.exists(save_path):
            os.mkdir(save_path)
        cv2.imwrite(f"{save_path}/{0:06d}.png", cv2.imread(title_image, cv2.IMREAD_COLOR))
        for i, img in enumerate(images):
            print(f"COLORIZING {img}")
            qt_window.on_colorizing = True
            qt_window.set_progress(f"COLORIZING {img}")
            temp = self.eval(img, title_image)
            cv2.imwrite(f"{save_path}/{i + 1:06d}.png", temp)
            qt_window.processed.setPixmap(QtGui.QPixmap(f"{save_path}/{i + 1:06d}.png"))
        qt_window.set_progress(f"Done.")
        qt_window.on_colorizing = False
        if sys.platform in ('darwin', 'linux'):
            os.system(f"open {save_path}")
        else:
            os.system(f"explorer {save_path}")
