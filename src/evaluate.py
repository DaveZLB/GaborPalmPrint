# -*- coding: utf-8 -*-

from __future__ import print_function

from scipy.spatial import distance
import numpy as np;

result_file_name = 'result.txt'

def hamming_distance(v1, v2):
  assert v1.shape == v2.shape, "shape of two vectors need to be same!"
  v_sharp = v1.shape
  gabor_filter_number = v_sharp[0]
  filters_total_hamming_distance = 0
  for i in range(gabor_filter_number):
      v1_real_mat = v1[i][0]
      v1_imag_mat = v1[i][1]
      v2_real_mat = v2[i][0]
      v2_imag_mat = v2[i][1]
      real_hamming_distance = distance.hamming(v1_real_mat.flatten(),v2_real_mat.flatten())
      imag_hamming_distance = distance.hamming(v1_imag_mat.flatten(), v2_imag_mat.flatten())
      filters_total_hamming_distance += (real_hamming_distance + imag_hamming_distance) / 2
  return filters_total_hamming_distance / gabor_filter_number


def infer(samples=None):
    cls_map = {}
    for query in samples:
        q_img, q_cls, q_hist = query['img'], query['cls'], query['hist']
        print(q_img)
        results = []
        for idx, sample in enumerate(samples):
            s_img, s_cls, s_hist = sample['img'], sample['cls'], sample['hist']
            if q_img == s_img:
                continue
            results.append((s_img,s_cls,hamming_distance(q_hist, s_hist)))
        dt = np.dtype([('name', 'S10'), ('cls', 'S10'), ('dis', float)])
        np_arr = np.array(results,dt)
        ss = np.sort(np_arr,order='dis')[:5]['cls'].astype(dtype=np.int)
        predict_cls = np.argmax(np.bincount(ss))
        if q_cls in cls_map:
            if q_cls == predict_cls:
                cls_map[q_cls] = cls_map[q_cls] + 1
        else:
            cls_map[q_cls] = 0
    total_acc = 0
    for k,v in cls_map.items():
        cls_map[k] = v / 5
        total_acc += cls_map[k]
    cls_map['mAP'] = total_acc/len(cls_map.keys())
    write_result(cls_map)

def write_result(result):
  with open(result_file_name, 'a+') as f:
    for k,v in result.items():
        f.write("\n{} , {}".format(k, v))

