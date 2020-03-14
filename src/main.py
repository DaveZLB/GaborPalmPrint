# -*- coding: utf-8 -*-

from __future__ import print_function

from evaluate import infer
from db import Database
from gabor import Gabor
result_file_name = 'result.txt'


def write_result(result):
  with open(result_file_name, 'a+') as f:
    for r in result:
      f.write(r + '\n')


if __name__ == '__main__':
  db = Database()
  # retrieve by gabor
  method = Gabor()
  samples = method.make_samples(db)
  for query_idx in range(len(samples)):
    query = samples[query_idx]
    result = infer(query, samples=samples)
    write_result(result)
    print(result)