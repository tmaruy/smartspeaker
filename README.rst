=======================
smartspeaker作成
=======================

Create smartspeaker with Raspberry Pi

-------------------------------------
Materials
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
* `赤外線リモコンを使う <http://make.bcde.jp/raspberry-pi/%E8%B5%A4%E5%A4%96%E7%B7%9A%E3%83%AA%E3%83%A2%E3%82%B3%E3%83%B3%E3%82%92%E4%BD%BF%E3%81%86/#LIRCLinux_Infrared_Remote_Control>`
* `Raspberry pi 3をつかってLINEから赤外線リモコンを操作 <https://qiita.com/na59ri/items/aea452f2487a393537dd>`

Methods
-----------------
1. | LIRCのインストール
   | Raspberry Piで赤外線受信を行うためにLIRC (Linux infrared remote control)をインストールします。
    
   sudo apt-get install lirc

2. | GPIOの設定
   | 赤外線受信モジュールと送信モジュールのピンを設定
   | ファイル`/boot/config.txt`に以下の内容を追加して再起動
   | gpio_in_pinが受信、gpio_out_pinが送信用のピンとして設定される
      
   #RemoteController
   dtoverlay=lirc-rpi
   dtparam=gpio_in_pin=22
   dtparam=gpio_out_pin=21
   
3. | 赤外線受信用モジュールをつなぐ
   | モジュールは2.のgpio_in_pinで設定したピンに繋げる

4. | リモコンの発信パターンを学習
   | 
   
   
