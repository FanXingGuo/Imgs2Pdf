# Imgs2Pdf
批量图片黑白化，并合并成PDF
## 拍照的图片
 ![image](https://github.com/FanXingGuo/Imgs2Pdf/blob/master/1pp.png)
 ## 效果图
 ![image](https://github.com/FanXingGuo/Imgs2Pdf/blob/master/2pp.png)
 
 ## 使用方式
 需要依赖模块PIL：
 ```bash
 sudo easy_install PIL
 ```
 运行
 ```bash
 python imgs2pdf.py 140 高中数学公式.pdf
 ```
 其中 第一个参数140，是黑色占比，范围0-255，数值越大，黑色越多，经测试，推荐140
 第二个参数为 文件全
