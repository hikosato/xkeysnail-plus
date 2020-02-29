# xkeysnail-plus
[mooz/xkeysnail](https://github.com/mooz/xkeysnail) に、以下のキーを修飾キーとして利用できるようにしました。  

+ 変換キー
+ 無変換キー
+ カタカナ・ひらがなキー
+ メニューキー

## 動機
xkeysnailに限らず、AutoHotkeyなどのキーリマップツールで、  
例えば、```Ctrl+H```を```BackSpace```にキーバインドを変更すると、  
そのままではアプリ本来のキーバインド(Chromeだと履歴表示、VSCodeだと置換)が機能しなくなります。  
アプリ側でキーバインドを変更できるものは、アプリごとに他のキーバインドに変更すればいいのですが、  
面倒なので、無変換キーを修飾キー化して、  
```
・ Ctrl+H     --> BackSpace
・ Muhenkan+H --> Ctrl+H
```
のような設定ができれば、アプリ本来のキーバインド```Ctrl+H```を```無変換+H```に振り替えることで、  
アプリ本来のキーバインドを侵食することなくそのまま活用できます。  
AutoHotkeyのようにxkeysnailでもできればいいのにというのが動機です。  
というわけで、xkeysnailのコードに、ほんの少しだけ手を加えたものがこのxkeysnail-plusです。  
このREADME.mdでは、実践的な事柄についてのみ解説します。  
フォーク元のxkeysnailが内部で、どのようにして低レイヤーレベルでのキーリマップを実現しているかは、  
[https://github.com/mooz/xkeysnail](https://github.com/mooz/xkeysnail)を参照してください。  

## 検証した環境
+ Ubuntu 18.04 Desktop Remix 日本語  
+ Logicool ロジクール K275 ワイヤレスキーボード  
(日本語キーボード PC108、右Windowsキーなしタイプ)   

    
## インストール
pip3が必要です。  
```
$ sudo apt install python3-pip
```
```git clone```して出来たxkeysnail-plusディレクトリに入ってpip3でインストールします。
```
$ git clone https://github.com/hikosato/xkeysnail-plus.git
$ cd xkeysnail-plus/
$ sudo -H pip3 install --upgrade .
```
```/usr/local/bin/```にxkeysnail-plusコマンドが設置されます。  


## アンインストール
```
$ sudo -H pip3 uninstall xkeysnail-plus
```
で、すべてアンインストールされます。  

## テスト実行の手順
ログイン時に自動起動させる方法は後述していますが、  
ひとまず、ターミナル上でフォアグランド起動して、  
私が用意した、Mac風キーバインド設定であるconfig.pyがどのような設定なのか、  
それを起点にして自分好みにキー配列やキーバインドを追加・変更してみたり、  
キーバインドの動作確認など、このツールの一連の操作に慣れてから自動起動設定することをおすすめします。    
  
まずは、お使いのMozcのプロパティの現在のキー設定をバックアップしてください。  
「Mozc」-> 「ツール」->「プロパティ」->  
「キー設定の選択--編集」->「編集」->「エクスポート」  
で、ご自身の設定をファイルとして保存できます。   
エクスポートの上にインポートがあったかと思いますが、  
インポートを選択することで、このバックアップファイルをインポートして元に戻せます。  
   
その後、config.pyのキーバインドに合わせたMozcキー設定をあらかじめ、  
xkeysnail-plusの```etc/install_set/Mozc_xkey_keymap.txt```に準備してありますので、  
Mozcにインポートしてください。  
     
次に、```xhost```に一時的にrootを登録します。  
```
$ xhost +si:localuser:root
```
ログアウトするとこの設定は消えます。  
  
最後に、設定ファイルを引数で指定してxkeysnail-plusコマンドを実行します。  
カレントディレクトリが先程``` pip3 install ```した場所のままだとして  
```
$ sudo xkeysnail-plus config/config.py
```  
これで、キー配列とキーバインドがconfig.pyに書かれたものに変更されます。  
configフォルダにある```default_config.py```は、フォーク元のxkeysnailのサンプル設定ファイルです。  

config.pyのキー配列やキーバインドを自分好みに変更した後、  
先程xkeysnail-plusを起動したターミナルのコマンドライン上で、```Ctrl+C```で停止させ、再度  
```
$ sudo xkeysnail-plus config/config.py
```
を実行して、config.pyを再読込みすると変更が反映されます。  

## 設定
フォーク元の[How to prepare config.py](https://github.com/mooz/xkeysnail#how-to-prepare-configpy)に詳細が記載されています。  
設定は各関数の引数に書き込みます。  
  
キー配列に関する設定は、  
+ ```define_modmap(layout)```
+ ```define_conditional_modmap(condition, layout)```  
+ ```define_multipurpose_modmap(layout)```  
  
キーバインドの設定は、  
```define_keymap(condition, keybind, "name")```  
に記入します。  
  
### 引数について
  
引数layoutはキー・バリューのdict(辞書)です。  
key.pyのKeyクラスに登録されているキー名を使用します。  
```
# Capslockキーを左Controlキーに変更
    Key.CAPSLOCK: Key.LEFT_CTRL,
```
  
引数keybindもキー・バリューのdict(辞書)ですが、  
transform.pyのKクラスを使用します。  
```
# Ctrl+HをBackSpaceに振り替える
    K("C-h"): K("backspace"),
```
Cは修飾キーControlです。hはHキーです。修飾キーは大文字小文字を区別されますが、  
H, backspaceキーなどの修飾キー以外のキーは区別されません。
```
# 修飾キー以外は大文字小文字を区別しない
    K("C-H"): K("bAcKsPaCe"),
```

xkeysnail-plusでは、  
ウィンドウごとにキー配列・キーバインドを適用するために、ウィンドウのWM_CLASSを利用しています。   
WM_CLASSはxkeysnail-plusを起動したターミナルに、押したキーの登録キー名とともに、  
リアルタイムに表示されています。  
  
例えば、VSCodeでエンターキーを押した場合は、  
```
WM_CLASS 'Code' | active keymaps = [Global keybinding, mac-like keys]
ENTER
```
CodeがWM_CLASSで、ENTERがエンターキーの登録キー名です。   
  
   
引数condition(条件)は、 
```None```で、すべてのウィンドウに対して有効になり、   
```re.compile(r'Code|Google-chrome')```で、VSCodeかChromeの時のみkeybindが有効になり、  
```lambda wm_class: wm_class not in ("Gnome-terminal", "vlc")```で、  
Ubuntu標準ターミナルとvlc media player**以外**のウィンドウでkeybindが有効になります。  
キー配列、キーバインド、どちらの関数のconditionでも利用可能です。  
  
```
# ウィンドウのVM_CLASSを条件に、ウィンドウごとに「キー配列」を設定する
define_conditional_modmap(re.compile(r'Emacs'), {
    # Emacsの時だけ右CtrlにESCを割り当てる
    Key.RIGHT_CTRL: Key.ESC,
    # これにより、Emacsは上のdefine_modmap()から隔離されるので、
    # CapsLockキーはCapsLockのままになる。
    # Emacsで、Capslockキーも左Controlキーに変更したい場合はここで再設定する。
    # Key.CAPSLOCK: Key.LEFT_CTRL,
})
```
```
# 修飾キー以外のキーの振る舞いを、単独押し時と他のキーとの同時押し時で変化させる。
define_multipurpose_modmap(
    # Enter単独押しではEnter、
    # Enterを押しながら他のキー(Hキーとか)を押すと、Enter+Hが右Ctrl+Hになる。
    {Key.ENTER: [Key.ENTER, Key.RIGHT_CTRL]}
    # define_keymap()で、Ctrl+Hはbackspaceにキーバインドしてあるので、
    # 最終的にはbackspaceになる。

    # CapsLockキー単独押しではESC、他のキーと組み合わせると左Ctrlとして機能する。
    # {Key.CAPSLOCK: [Key.ESC, Key.LEFT_CTRL]}
    # define_modmap()との同一キーの重複設定はできない。
)
```

引数"name"は、```Global keybinding, mac-like keys```のように表示用として利用されます。  
ご自身でわかりやすい名前をつけてください。
  

修飾キーの一覧
|キー名|キーバインド設定時の記号|キー配列設定時の値|
|:---|:---|:---|
|Shift|Shift|無し(左右のどちらかを指定する)|
|左Shift|LShift|Key.LEFT_SHIFT|
|右Shift|RShift|Key.RIGHT_SHIFT|
|Control|C, Ctrl|無し(左右のどちらかを指定する)|
|左Control|LC, LCtrl|Key.LEFT_CTRL|
|右Control|RC, RCtrl|Key.RIGHT_CTRL|
|Alt|M, Alt|無し(左右のどちらかを指定する)|
|左Alt|LM, LAlt|Key.LEFT_ALT|
|右Alt|RM, RAlt|Key.RIGHT_ALT|
|Windows(Super)|Win, Super|無し(左右のどちらかを指定する)|
|左Windows(Super)|LWin, LSuper|Key.LEFT_META|
|右Windows(Super)|RWin, RSuper|Key.RIGHT_META|
|変換キー|Henkan|Key.HENKAN|
|無変換キー|Muhenkan|Key.MUHENKAN|
|カタカナ・ひらがなキー|Kata_Hira|Key.KATAKANAHIRAGANA|
|メニューキー|Menu|Key.COMPOSE|

## ログイン時にxkeysnail-plusを自動起動させる
参考サイト: [xkeysnailでキーリマップする-Qiita](https://qiita.com/miy4/items/dd0e2aec388138f803c5)  
  
xkeysnailはuinputという低レイヤーのAPIを利用しているので、  
sudo(管理者権限)での実行が必須です。  
上記テスト実行のようにrootユーザーを使うのは、個人利用でもセキュリティリスクが高いので  
ノーログインユーザーxkeysnailを新たに作成して起動用のユーザーとします。   
※ 以下で作成するファイルはxkeysnail-plus/etc/install_set/に同梱してあります。  
  
uinputというユーザーを作成
```
$ sudo groupadd uinput
```
xkeysnailユーザーを作成し、input,uinputグループにも所属させます。
```
$ sudo useradd -G input,uinput -s /sbin/nologin xkeysnail
```
```/etc/udev/rules.d/40-udev-xkeysnail.rules```ファイルを作成して以下を記入。
```
KERNEL=="uinput", GROUP="uinput"
```
```/etc/modules-load.d/uinput.conf```ファイルを作成して以下を記入。
```
uinput
```
```/etc/sudoers.d/10-sudo-xkeysnail```ファイルを作成して以下を記入。  
satohはご自分のログインユーザー名に変更してください。  
```
satoh ALL=(ALL) ALL, (xkeysnail) NOPASSWD: /usr/local/bin/xkeysnail-plus
```
```~/.xprofile```ファイルを作成して以下を記入。
```
if [ -x /usr/local/bin/xkeysnail-plus ]; then
	xhost +si:localuser:xkeysnail
	sudo -u xkeysnail DISPLAY=$DISPLAY /usr/local/bin/xkeysnail-plus $HOME/.xkeysnail/config.py &
fi
```
```~/.xkeysnail```ディレクトリを作成して、xkeysnail-plus/config/config.pyをコピー。  
  
OS再起動でキーバインド設定が反映されます。  
pip3でインストール完了後は、```git clone```でダウンロードしたxkeysnail-plusフォルダは無くても動作に影響しません。  
下記項目を設定しないのであれば削除しても構いません。  
  
## その他
### CapsLockキー単独押しで何も起きないようにする
UbuntuのCapslockキーの振る舞いはデフォルトでは  
+ 単独押しで英数トグル
+ Shift+CapslockでCapslock
  
が作動します。  
単独押しを無効にするには、xkbに元から備わっているオプション設定を利用します。  
```/etc/default/keyboard```ファイルのXKBOPTIONSをこのように設定します。  
```
XKBOPTIONS="shift:both_capslock"
```
OS再起動すると、  
+ 左(右)Shiftキー+Capslock
+ 左右のShiftキーを両方同時押し
  
でのみCapslockが有効になり、単独押しでは何も起きなくなります。

### Menuキーを修飾キーにする際のxkb設定
```xkeysnail-plus/etc/```にmysymbolファイルがあります。  
これを```/usr/share/X11/xkb/symbols/```にコピーします。  
次に、```/usr/share/X11/xkb/rules/evdev```を```sudo vi```で開いて、  
ファイルの末尾に以下を追記します。目立ちませんが、先頭の「!」も必須です。  
```
! option                 =   symbols
  mysymbol:no_menu       =   +mysymbol(no_menu)
```
※ この設定作業は慎重に行ってください。  
間違った設定をすると、OS自体は起動できても、デスクトップ環境にログインできなくなる可能性があります。  
間違った設定によってエラー停止しているだけの状態ですので、  
原因は変更したファイルだとわかっていますので、慌てずに、リカバリーモードで復旧してください。  
以下の手順になります。 

1. おそらく黒い画面のままで停止しているはずです。
2. 電源ボタン長押しで落とした後、再起動します。
3. grubメニューが表示されたら、Advanceed options for Ubuntuに入ります。  
   grubメニューが表示されない場合は起動時にShiftキーを連打すれば表示されます。
4. recovery modeに入ります。(複数あるときは上の方を選択)
5. 「root - Drop to root shell prompt」を選択してEnter。
6. 下に、「Press Enter for maintenance」が表示されたらEnter。
  
これで、プロンプトが表示されてコマンドが入力できる状態になりますので、  
原因は変更したファイルですので、設定を元に戻してexitで抜けます。  
一つ前の画面に戻りますので、「resume Resume normal boot」を選択してEnter。  
「You are now going to exit the recovery mode and ... 」となるのでOK(Enter)。  
これで復旧できると思います。  
  
復旧直後から、「システムプログラムの問題が見つかりました」というダイアログが、  
ログインするたびに表示されるようになると思います。  
今回は、原因ははっきりしていますので「キャンセル」で閉じて、  
```
$ sudo rm /var/crash/*
```
を実行してダンプファイルをすべて削除してください。  


### 左Windowsキー+Aで「すべてを選択(Ctrl+A)」
config.pyで、  
すでに「無変換+A」で「すべてを選択」ができるようになっていますが、  
応用のために、あえて他の方法も残しておきます。  
  
xkeysnailでキーバインドを変更しても、元々の機能が透過してしまうので、  
define_keymap()内で```K("LSuper-a"): (K("C-a"))```としても  
左Windowsキー単独押しで、「アクティビティ」画面へ切り替わるだけで、  
「すべてを選択」にはなりません。    
  
以下のコマンドをターミナルで実行して、  
アクティビティへのシステムキーバインドを、左Windowsキーから右Windowsキーに変更することで対応します。  
```$ gsettings set org.gnome.mutter overlay-key "Super_R"```   
元に戻すときは以下を実行してリセットします。  
```$ gsettings reset org.gnome.mutter overlay-key```  
  
元からキーボードに右Windowsキーがない場合は、  
カタカナ・ひらがなキーなどを右Windowsキーに変更してください。  
例えば、define_modmap()に以下を追記します。  
```
Key.KATAKANAHIRAGANA: Key.RIGHT_META,
```

### 既知の問題
新しく追加した  

+ 変換キー
+ 無変換キー
+ カタカナ・ひらがなキー
+ メニューキー
  
は、元々修飾キーではないので、VSCodeやIntellij系でキーバインドを変更するときのスキャン時に、   
例えば、xkeysnail-plus側の設定で  
```
K("Muhenkan-h"): K("C-h"),
```
として、```Ctrl+H``` を送信しているつもりでも、  
VSCodeでは```ctrl + h + unknown```として認識され、  
Intellij系では```無変換```として認識され、  
そのままではIDEツールのキーバインドができない場合があります。  
  
このような場合には、  
一度、xkeysnail-plusを停止して正規のCtrlキーに戻してからIDEツールのキーバインド設定をすると、  
うまく登録できるようです。    
