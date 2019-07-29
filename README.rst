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
* | `赤外線LED <https://www.amazon.co.jp/gp/product/B016DE22KW>`__

-------------------------------------
赤外線による操作
-------------------------------------

参考
===================
* `赤外線リモコンを使う <http://make.bcde.jp/raspberry-pi/%E8%B5%A4%E5%A4%96%E7%B7%9A%E3%83%AA%E3%83%A2%E3%82%B3%E3%83%B3%E3%82%92%E4%BD%BF%E3%81%86/#LIRCLinux_Infrared_Remote_Control>`__
* `Raspberry pi 3をつかってLINEから赤外線リモコンを操作 <https://qiita.com/na59ri/items/aea452f2487a393537dd>`__

メモ
===================

1. LIRCのインストール
-----------------------------
* | Raspberry Piで赤外線受信を行うためにLIRC (Linux infrared remote control)をインストールします。
    
.. code-block:: 

   sudo apt-get install lirc

2. GPIOの設定
-----------------------------
* | 赤外線受信モジュールと送信モジュールのピンを設定
  | ファイル`/boot/config.txt`に以下の内容を追加して再起動
  | gpio_in_pinが受信、gpio_out_pinが送信用のピンとして設定される
  
.. code-block:: 

   #RemoteController
   dtoverlay=lirc-rpi
   dtparam=gpio_in_pin=22
   dtparam=gpio_out_pin=21
   
3. 赤外線受信用モジュールをつなぐ
-----------------------------------
* | モジュールは2.のgpio_in_pinで設定したピンに繋げる [1]_

.. image:: https://user-images.githubusercontent.com/53417955/62034599-44d93680-b229-11e9-9679-284efd349880.png

4. リモコンの赤外線発信パターンを調べる
---------------------------------------
* | 以下のコマンドを入力したのちに赤外線を照射。すると以下のように受信した信号が出力される

.. code-block::
   
   sudo /etc/init.d/lirc stop
   mode2 -d /dev/lirc0 | tee signals/aircon/on  # signals/aircon/onにシグナルが出力される
   # ここで照射

.. figure:: https://user-images.githubusercontent.com/53417955/62022857-1481a000-b209-11e9-8e3c-265de945eac4.png

5. 受信した信号を登録する
---------------------------------------
* | mode2で出力したシグナルを./lirc/reformat_lirc_signals.pyで処理
  | 出力ファイル lircd.confを/etc/lirc/に移動
   
6. 登録したシグナルを確認
---------------------------------------
* | lircd.confに登録されたシグナルの情報を確認する
 
.. code-block::
   
   sudo /etc/init.d/lircd start
   irsend LIST "" ""
   irsend LIST aircon ""
 
.. image:: https://user-images.githubusercontent.com/53417955/62032417-8fa47f80-b224-11e9-9df7-72f71798b13d.png

7. シグナルを出力
---------------------------------------
* | 以下のコマンドで登録したシグナルを出力することができる
  | 赤外線LEDを2.のgpio_out_pinで設定したピンに繋げる
   
.. code-block::
    
   irsend SEND_ONCE aircon on
 
課題
===================
* | 赤外線LEDのシグナルが弱い
  | LEDの問題？
  | LEDキャップ？
  | 電流が弱い？トランジスタ？


-------------------------------------
携帯からの遠隔操作
-------------------------------------

参考
===================
* | `Blynk <https://blynk.io/en/getting-started>`__
* | http://blog.livedoor.jp/victory7com/archives/48432885.html

メモ
===================

1. Blynkを携帯にインストール
-----------------------------
* | App storeでインストール

2. プロジェクトを作る
-----------------------------
* | 

.. image:: https://user-images.githubusercontent.com/53417955/62045011-38f86f00-b23f-11e9-9888-11229af4dab8.png
.. image:: https://user-images.githubusercontent.com/53417955/62045039-50375c80-b23f-11e9-9e32-86e5b5973e83.png


3. Raspberry Pi側でBlynkをダウンロード
--------------------------------------

.. code-block::
   
   git clone https://github.com/blynkkk/blynk-library.git


4. ./blynk-library/linux/main.cppをいじる
------------------------------------------
* | main.cppの関数BLYNK_WRITEを

.. code-block:: c
   
   BLYNK_WRITE(V1){
    char command[256] = "";
    if(param[0] == 1){
      printf("Aircon ON\n");
      strcat(command, "irsend SEND_ONCE aircon on");
    }else{
      printf("Aircon OFF\n");
      strcat(command, "irsend SEND_ONCE aircon off");
    }
    system(command);
    }




.. [1] 図は `Fritzing <http://fritzing.org/download/>`__ で作成
