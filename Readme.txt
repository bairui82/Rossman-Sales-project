����ϵͳ,Win10 64
Python�汾 anaconda python 2
����Ŀʹ����һ�¿�
numpy
matplotlib
seaborn
IPython.display
xgboost
time
datetime
��װxgboost����:

�ȴ�github�ϻ�ȡxgboost
git clone --recursive https://github.com/dmlc/xgboost
��git shell������������
git submodule init
git submodule update
��װMinGW
��ַ https://sourceforge.net/projects/mingw-w64/
��װ������
version 7.2.0
Architecture X86_64
Threads posix
Exception seh
build revision 1
�����е�ַ��ӵ�����
C:\Program Files\mingw-w64\x86_64-7.2.0-posix-seh-rt_v5-rev1\mingw64\bin
���ն�������
alias make='mingw32-make'

cp make/mingw64.mk config.mk; make -j4
�����xgboost���ļ�������ն�����
mkdir build
cd build
cmake .. -G"Visual Studio 12 2013 Win64"
���python-package\xgboost���xgboost.dll���Ƶ�python�µ�xgboost�ļ�����
������c���������dll����Ҳ������,����֮������Gpu�����ʱ����ֱ�Ӵ�����������xgboost.dll
��ҳ��ַ
http://ssl.picnet.com.au/xgboost/
