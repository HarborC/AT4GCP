from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals

from GUI import Gui
from Database import Database
from mytk import tk
from pathlib import Path
from imageSugestion import get_all_images
import sys
import argparse
import pickle


def parse_args():
    parser = argparse.ArgumentParser(
        description=__doc__)
    parser.add_argument(
        'dataset',
        help='dataset',
    )
    parser.add_argument(
        '-n',
        '--no-preload',
        help='skip preloading',
        action='store_true'
    )
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    path = args.dataset
    seqs = get_all_images(path)
    database = Database(seqs, path, preload_images=not args.no_preload)
    root = tk.Tk()
    root.resizable(True, True)
    my_gui = Gui(root, database)
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)
    root.title("ANNOTATION GUI")
    root.mainloop()
