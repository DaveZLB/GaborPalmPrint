# -*- coding: utf-8 -*-

from __future__ import print_function

import pandas as pd
import os

DB_dir = '../database'
DB_csv = 'data.csv'


class Database(object):

  def __init__(self):
    self._gen_csv()
    self.data = pd.read_csv(DB_csv)

  def _gen_csv(self):
    if os.path.exists(DB_csv):
      return
    with open(DB_csv, 'w', encoding='UTF-8') as f:
      f.write("img,cls,name")
      for root, _, files in os.walk(DB_dir, topdown=False):
        cls = root.split('/')[-1]
        for name in files:
          if not name.endswith('.bmp'):
            continue
          img = os.path.join(root, name)
          cls = name.split("_")[0]
          f.write("\n{},{},{}".format(img, cls,name))

  def __len__(self):
    return len(self.data)

  def get_data(self):
    return self.data


if __name__ == "__main__":
  db = Database()
  data = db.get_data()

  print("DB length:", len(db))
