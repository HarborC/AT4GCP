from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals

import os
import pickle

def get_all_images(path):
    IMG_EXENT = [".jpg", ".jpeg", ".png", ".tiff", ".tif", ".JPG", ".JPEG", ".PNG", ".TIFF", ".TIF"]

    seqs_sub = []
    images_path = os.path.join(path, "images")
    flist = os.listdir(images_path)
    def get_name(x):
        (filepath, tempfilename) = os.path.split(x)
        (filename, exent) = os.path.splitext(tempfilename)
        return float(filename)

    for skey in flist:
        if os.path.isdir(os.path.join(images_path, skey)):
            seq_img_path = os.path.join(images_path, skey)
            imagefiles = os.listdir(seq_img_path)
            for imagefile in imagefiles:
                if imagefile[0] == '.':
                    continue
                if os.path.isfile(os.path.join(seq_img_path, imagefile)) and os.path.splitext(imagefile)[-1] in IMG_EXENT:
                    seqs_sub.append(skey + "/" + imagefile)
                    print(skey + "/" + imagefile)

    seqs_sub = sorted(seqs_sub, key=lambda x:get_name(x))
    return [seqs_sub, seqs_sub]
