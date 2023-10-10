# openCVとは

## 1 OpenCV v4.6.0をインストールするまでの流れ

### 1-1
```
sudo apt install -y libatlas-base-dev
```

管理者権限でlibatlas-base-devパッケージをインストールし、行列やベクトルの計算を高速にするOpenCVを使用する際に必要となる

### 1-2 numpyをアップグレードしてインストール

```
pip install numpy --upgrade
```

### 1-3  wheelファイルを取得
```
wget https://www.piwheels.org/simple/opencv-python/opencv_python-4.6.0.66-cp37-cp37m-linux_armv7l.whl#sha256=70e5f777be8b2027e6667f840e64db82255461085eb7b81b5052416925ed3038
```

### 1-3 wheelファイルをインストール

```
pip install opencv_python-4.6.0.66-cp37-cp37m-linux_armv7l.whl
 ```

### 1-4 OpenCVインストール確認

1. 対話モードに以降
1. import cv2
1. cv2.__version__ 

## 2 openCVを使ったコードの解説

### 2-1 画像を表示
```
import cv2

image_file = 'cat.png'
img = cv2.imread(image_file)　//imgはnumpy配列型

cv2.imshow('image', img) //ウィンドウに名前を付け、第二引数に指定した画像を表示

cv2.waitKey(0) //キーが押されるまで処理を待つ
cv2.destroyAllWindows() //全てのウィンドウを閉じる
```


### 2-2 画像サイズ変更
```
img = cv2.resize(img, (400, 300))
```


### 2-3 エッジ検出

```
edges = cv2.Canny(gray_img, 50, 100)
```

#### cv2.Canny
- 第1引数: 画像データ
- 第2引数: この閾値より小さい勾配は、ノイズとして気にされます。
- 第3引数: この閾値より大きい勾配は、エッジとして検出されます。


## 各種エラー

### cv2.imshow('image', img)cv2.error: OpenCV(4.6.0) /tmp/pip-wheel-8c7uejek/opencv-python_88dbbad412c5416b992ae69de26299d6/opencv/modules/highgui/src/window_gtk.cpp:635: error: (-2:Unspecified error) Can't initialize GTK backend in function 'cvInitSystem'

GUIを使える環境で実行することで解決  
    vscodeではなくラズパイのデスクトップターミナルから実行することでエラーが解消される


## 参考サイト

[【09.基礎４】OpenCVを学ぶ](https://jellyware.jp/kurage/movidius/c09_opencv.html)
