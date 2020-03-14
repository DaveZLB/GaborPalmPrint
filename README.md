# 使用 Gabor filter 和 Hamming distance

- Gabor filter 参数设置

No | Sizes | theta | frequence | sigma |
---|--- | --- | --- | --- |
1 | 9 by 9  | 0 | 0.3666 | 1.4045 |
2 | 9 by 9  | 45 | 0.3666 | 1.4045 |
3 | 9 by 9  | 90 | 0.3666 | 1.4045 |
4 | 9 by 9  | 135 | 0.3666 | 1.4045 |
5 | 17 by 17  | 0 | 0.1833 | 2.8090 |
6 | 17 by 17  | 45 | 0.1833 | 2.8090 |
7 | 17 by 17  | 90 | 0.1833 | 2.8090 |
8 | 17 by 17  | 135 | 0.1833 | 2.8090 |
9 | 35 by 35  | 0 | 0.0916 | 5.6179 |
10 | 35 by 35  | 45 | 0.0916 | 5.6179 |
11 | 35 by 35  | 90 | 0.0916 | 5.6179 |
12 | 35 by 35  | 135 | 0.0916 | 5.6179 |

- 实验结果

选取了BMP600里面的几张图片做了比较

BMP600/050_1.bmp,BMP600
BMP600/001_2.bmp,BMP600
BMP600/001_1.bmp,BMP600
BMP600/060_1.bmp,BMP600
BMP600/002_1.bmp,BMP600
BMP600/004_1.bmp,BMP600

结果如下：
```cmd
hamming distance of 050_1.bmp and 001_2.bmp : 0.49606068929036456
hamming distance of 050_1.bmp and 001_1.bmp : 0.49991607666015625
hamming distance of 050_1.bmp and 060_1.bmp : 0.46475474039713544
hamming distance of 050_1.bmp and 002_1.bmp : 0.48000335693359375
hamming distance of 050_1.bmp and 004_1.bmp : 0.48215484619140625
hamming distance of 001_2.bmp and 050_1.bmp : 0.49606068929036456
hamming distance of 001_2.bmp and 001_1.bmp : 0.3457743326822917
hamming distance of 001_2.bmp and 060_1.bmp : 0.5032094319661459
hamming distance of 001_2.bmp and 002_1.bmp : 0.4950205485026042
hamming distance of 001_2.bmp and 004_1.bmp : 0.4903055826822917
hamming distance of 001_1.bmp and 050_1.bmp : 0.49991607666015625
hamming distance of 001_1.bmp and 001_2.bmp : 0.3457743326822917
hamming distance of 001_1.bmp and 060_1.bmp : 0.5109405517578125
hamming distance of 001_1.bmp and 002_1.bmp : 0.5073801676432291
hamming distance of 001_1.bmp and 004_1.bmp : 0.5021820068359375
hamming distance of 060_1.bmp and 050_1.bmp : 0.46475474039713544
hamming distance of 060_1.bmp and 001_2.bmp : 0.5032094319661459
hamming distance of 060_1.bmp and 001_1.bmp : 0.5109405517578125
hamming distance of 060_1.bmp and 002_1.bmp : 0.4887034098307292
hamming distance of 060_1.bmp and 004_1.bmp : 0.4919840494791667
hamming distance of 002_1.bmp and 050_1.bmp : 0.48000335693359375
hamming distance of 002_1.bmp and 001_2.bmp : 0.4950205485026042
hamming distance of 002_1.bmp and 001_1.bmp : 0.5073801676432291
hamming distance of 002_1.bmp and 060_1.bmp : 0.4887034098307292
hamming distance of 002_1.bmp and 004_1.bmp : 0.4824473063151042
hamming distance of 004_1.bmp and 050_1.bmp : 0.48215484619140625
hamming distance of 004_1.bmp and 001_2.bmp : 0.4903055826822917
hamming distance of 004_1.bmp and 001_1.bmp : 0.5021820068359375
hamming distance of 004_1.bmp and 060_1.bmp : 0.4919840494791667
hamming distance of 004_1.bmp and 002_1.bmp : 0.4824473063151042

```

# 参考资料

- https://www.youtube.com/watch?v=QEz4bG9P3Qs

- https://www.ntu.edu.sg/home/AdamsKong/publication/PR_Gabor.pdf

- https://github.com/pochih/CBIR


