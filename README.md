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

    
## 使い方
[[無変換キーなどを修飾キー化] Ubuntuのキー配列・キーバインドをやりたい放題自分好みに変更する。](https://yukue.biz/%e7%84%a1%e5%a4%89%e6%8f%9b%e3%82%ad%e3%83%bc%e3%81%aa%e3%81%a9%e3%82%92%e4%bf%ae%e9%a3%be%e3%82%ad%e3%83%bc%e5%8c%96-ubuntu%e3%81%ae%e3%82%ad%e3%83%bc%e9%85%8d%e5%88%97%e3%83%bb%e3%82%ad%e3%83%bc)
