# -*- coding: utf-8 -*-

from __future__ import print_function
from skimage.filters import gabor_kernel
from skimage import color
from scipy import ndimage as ndi
import multiprocessing
from six.moves import cPickle
import numpy as np
import scipy.misc
import os



gabor_kernel_params = [
  {
    'theta': 0 / 4 * np.pi,
    'sigma': 1.4045,
    'frequency': 0.3666,
    'kernel_size': 9
  },
  {
    'theta': 1 / 4 * np.pi,
    'sigma': 1.4045,
    'frequency': 0.3666,
    'kernel_size': 9
  },
  {
    'theta': 2 / 4 * np.pi,
    'sigma': 1.4045,
    'frequency': 0.3666,
    'kernel_size': 9
  },
  {
    'theta': 3 / 4 * np.pi,
    'sigma': 1.4045,
    'frequency': 0.3666,
    'kernel_size': 9
  },
  {
    'theta': 0 / 4 * np.pi,
    'sigma': 2.8090,
    'frequency': 0.1833,
    'kernel_size': 17
  },
  {
    'theta': 1 / 4 * np.pi,
    'sigma': 2.8090,
    'frequency': 0.1833,
    'kernel_size': 17
  },
  {
    'theta': 2 / 4 * np.pi,
    'sigma': 2.8090,
    'frequency': 0.1833,
    'kernel_size': 17
  },
  {
    'theta': 3 / 4 * np.pi,
    'sigma': 2.8090,
    'frequency': 0.1833,
    'kernel_size': 17
  },
  {
    'theta': 0 / 4 * np.pi,
    'sigma': 5.6179,
    'frequency': 0.0916,
    'kernel_size': 35
  },
  {
    'theta': 1 / 4 * np.pi,
    'sigma': 5.6179,
    'frequency': 0.0916,
    'kernel_size': 35
  },
  {
    'theta': 2 / 4 * np.pi,
    'sigma': 5.6179,
    'frequency': 0.0916,
    'kernel_size': 35
  },
  {
    'theta': 3 / 4 * np.pi,
    'sigma': 5.6179,
    'frequency': 0.0916,
    'kernel_size': 35
  },
]

def make_gabor_kernel(gabor_kernel_params):
    kernels = []
    for p in gabor_kernel_params:
      kernels.append(gabor_kernel(p['frequency'], theta=p['theta'], sigma_x=p['sigma'], sigma_y=p['sigma'],n_stds=p['kernel_size']))
    return kernels

gabor_kernels = make_gabor_kernel(gabor_kernel_params)

# cache dir
cache_dir = 'cache'
if not os.path.exists(cache_dir):
  os.makedirs(cache_dir)


class Gabor(object):

  def gabor_histogram(self, input):

    if isinstance(input, np.ndarray):  # examinate input type
      img = input.copy()
    else:
      img = scipy.misc.imread(input, mode='RGB')
    return self._gabor(img, kernels=gabor_kernels)

  def _power(self, image, kernel):

    image = (image - image.mean()) / image.std()  # Normalize images for better comparison.
    real = ndi.convolve(image, np.real(kernel), mode='wrap')
    real[real >= 0] = 1
    real[real < 0] = 0
    real = real.astype(np.int)
    imag = ndi.convolve(image, np.imag(kernel), mode='wrap')
    imag[imag >= 0] = 1
    imag[imag < 0] = 0
    imag = imag.astype(np.int)
    return np.array([real,imag])

  def _gabor(self, image, kernels=make_gabor_kernel(gabor_kernel_params), normalize=True):
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())

    img = color.rgb2gray(image)

    results = []
    feat_fn = self._power
    print("kernels number = " + str(len(kernels)))
    for kernel in kernels:
      results.append(pool.apply_async(self._worker, (img, kernel, feat_fn)))
    pool.close()
    pool.join()
    gabor_feat = np.array([np.array([res.get()[0],res.get()[1]]) for res in results])
    return gabor_feat
  
  
  def _worker(self, img, kernel, feat_fn):
    try:
      ret = feat_fn(img, kernel)
    except:
      print("return zero")
      ret = np.zeros(2)
    return ret
  
  
  def make_samples(self, db, verbose=True):
    sample_cache = "gabor-params-cache"
    try:
      samples = cPickle.load(open(os.path.join(cache_dir, sample_cache), "rb", True))
      if verbose:
        print("Using cache..., config=%s" % (sample_cache))
    except:
      if verbose:
        print("Counting histogram..., config=%s" % (sample_cache))
  
      samples = []
      data = db.get_data()
      for d in data.itertuples():
        d_img, d_cls = getattr(d, "img"), getattr(d, "cls")
        d_hist = self.gabor_histogram(d_img)
        d_img_name = d_img[d_img.rindex('/') + 1:]
        samples.append({
                        'img':  d_img_name,
                        'cls':  d_cls, 
                        'hist': d_hist
                      })
      cPickle.dump(samples, open(os.path.join(cache_dir, sample_cache), "wb", True))
  
    return samples

