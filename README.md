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
[[無変換キーなどを修飾キー化] Ubuntuのキー配列・キーバインドをやりたい放題自分好みに変更する。](https://60can.hatenablog.jp/entry/%25e7%2584%25a1%25e5%25a4%2589%25e6%258f%259b%25e3%2582%25ad%25e3%2583%25bc%25e3%2581%25aa%25e3%2581%25a9%25e3%2582%2592%25e4%25bf%25ae%25e9%25a3%25be%25e3%2582%25ad%25e3%2583%25bc%25e5%258c%2596-ubuntu%25e3%2581%25)
