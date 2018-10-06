操作系统,Win10 64
Python版本 anaconda python 2
本项目使用了一下库
numpy
matplotlib
seaborn
IPython.display
xgboost
time
datetime
安装xgboost如下:

先从github上获取xgboost
git clone --recursive https://github.com/dmlc/xgboost
在git shell下输入命令行
git submodule init
git submodule update
安装MinGW
地址 https://sourceforge.net/projects/mingw-w64/
安装过程中
version 7.2.0
Architecture X86_64
Threads posix
Exception seh
build revision 1
将下列地址添加到环境
C:\Program Files\mingw-w64\x86_64-7.2.0-posix-seh-rt_v5-rev1\mingw64\bin
在终端里输入
alias make='mingw32-make'

cp make/mingw64.mk config.mk; make -j4
最后在xgboost的文件夹里打开终端输入
mkdir build
cd build
cmake .. -G"Visual Studio 12 2013 Win64"
最后将python-package\xgboost里的xgboost.dll复制到python下的xgboost文件夹里
由于是c编译出来的dll网上也有下载,所以之后用上Gpu运算的时候我直接从网上下载了xgboost.dll
网页地址
http://ssl.picnet.com.au/xgboost/
