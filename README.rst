=======================
smartspeaker
=======================

Create smartspeaker with Raspberry Pi

-------------------------------------
目的
-------------------------------------
* | 家の外からエアコンを動かしたい
* | 家の中にあるリモコンをまとめたい
  | スマホに置き換える
  | 音声で動かす

-------------------------------------
材料
-------------------------------------
* | Raspberry pi 2
* | USBマイク
* | USB Wifiアダプタ
* | 赤外線受信モジュール
* | 赤外線USB

-------------------------------------
赤外線による操作
-------------------------------------

Reference
-----------------
* `赤外線リモコンを使う <http://make.bcde.jp/raspberry-pi/%E8%B5%A4%E5%A4%96%E7%B7%9A%E3%83%AA%E3%83%A2%E3%82%B3%E3%83%B3%E3%82%92%E4%BD%BF%E3%81%86/#LIRCLinux_Infrared_Remote_Control>`__
* `Raspberry pi 3をつかってLINEから赤外線リモコンを操作 <https://qiita.com/na59ri/items/aea452f2487a393537dd>`__

Methods
-----------------
1. | LIRCのインストール
   | Raspberry Piで赤外線受信を行うためにLIRC (Linux infrared remote control)をインストールします。
    
.. code-block:: 

   sudo apt-get install lirc

2. | GPIOの設定
   | 赤外線受信モジュールと送信モジュールのピンを設定
   | ファイル`/boot/config.txt`に以下の内容を追加して再起動
   | gpio_in_pinが受信、gpio_out_pinが送信用のピンとして設定される
  
.. code-block:: 

   #RemoteController
   dtoverlay=lirc-rpi
   dtparam=gpio_in_pin=22
   dtparam=gpio_out_pin=21
   
3. | 赤外線受信用モジュールをつなぐ
   | モジュールは2.のgpio_in_pinで設定したピンに繋げる

4. | リモコンの発信パターンを学習
   | 以下のコマンドを入力したのちに赤外線を照射。すると以下のように受信した信号が出力される

.. code-block::
   
   sudo /etc/init.d/lirc stop
   mode2 -d /dev/lirc0
   # ここで照射

.. figure:: https://user-images.githubusercontent.com/53417955/62022857-1481a000-b209-11e9-8e3c-265de945eac4.png



