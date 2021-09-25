# 嘉然曲线（Diana Curve）

![image](https://github.com/yuchenxi2000/diana-curve/blob/main/diana.jpg)

![image](https://github.com/yuchenxi2000/diana-curve/blob/main/diana_origin.jpg)

## 使用

把matlab文件夹下三个文件导入Matlab，然后运行plot_diana.m。或者在generator目录下运行visualize.py

generator文件夹下是生成公式的Python脚本

## 灵感来源

Einstein curve https://www.wolframalpha.com/input/?i=Einstein+curve

一个参数方程，画出来是爱因斯坦的人像，于是想整个活

## 实现方法

1. 用Adobe Illustrator描点。参数方程采用分段曲线是因为图像本身不连续。曲线不是闭合的但描点时把首尾相连是因为傅立叶级数在跳跃间断点处有Gibbs现象（剧烈震荡）

2. 对每段曲线做FFT，做适当的截断，转成方程

> 最耗时的工作不是写脚本而是描点。。

## TODO

其他软件的公式生成，如Mathematica（目前只能生成Matlab）

