# -*- coding: utf-8 -*-

from __future__ import print_function

from scipy.spatial import distance


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


def infer(query, samples=None):
  ''' infer a query, return it's result

    arguments
      query       : a dict with three keys, see the template
                    {
                      'img': <path_to_img>,
                      'cls': <img class>,
                      'hist' <img histogram>
                    }
      samples     : a list of {
                                'img': <path_to_img>,
                                'cls': <img class>,
                                'hist' <img histogram>
                              }
  '''

  q_img, q_cls, q_hist = query['img'], query['cls'], query['hist']
  results = []
  for idx, sample in enumerate(samples):
    s_img, s_cls, s_hist = sample['img'], sample['cls'], sample['hist']
    if q_img == s_img:
      continue
    results.append('hamming distance of '+ q_img + ' and ' + s_img + ' : ' + str(hamming_distance(q_hist, s_hist)))
  return results
