# -*- coding: utf-8 -*-

import re
from xkeysnail_plus.transform import *


# 「キー配列」の全体設定
define_modmap({
    # Capslockキーを左Controlキーに変更
    Key.CAPSLOCK: Key.LEFT_CTRL,
    # 半角全角キー(GRAVEで登録されている)をCapslockキーに変更
    Key.GRAVE: Key.CAPSLOCK,
})

# ウィンドウのVM_CLASSを条件に、ウィンドウごとに「キー配列」を設定する
define_conditional_modmap(re.compile(r'Emacs'), {
    # Emacsの時だけ右CtrlにESCを割り当てる
    Key.RIGHT_CTRL: Key.ESC,
    # これにより、Emacsは上のdefine_modmap()から隔離されるので、
    # CapsLockキーはCapsLockのままになる。
    # Emacsで、Capslockキーも左Controlキーに変更したい場合はここで再設定する。
    # Key.CAPSLOCK: Key.LEFT_CTRL,
})

# 修飾キー以外のキーの振る舞いを、単独押し時と他のキーとの同時押し時で変化させる。
define_multipurpose_modmap(
    # Enter単独押しではEnter、
    # Enterを押しながら他のキー(Hキーとか)を押すと、Enter+Hが右Ctrl+Hになる。
    {Key.ENTER: [Key.ENTER, Key.RIGHT_CTRL]}
    # 下で、Ctrl+Hはbackspaceにしてあるので、最終的にはbackspaceになる。

    # CapsLockキー単独押しではESC、他のキーと組み合わせると左Ctrlとして機能する。
    # {Key.CAPSLOCK: [Key.ESC, Key.LEFT_CTRL]}
    # define_modmap()との同一キーの重複設定はできない。
)

define_keymap(None, {

    # Ubuntuのアクティブウィンドウ切り替えは、
    # アプリ切り替え(Alt+Tab) -> ウィンドウ選択(Alt+半角全角キー)　の2段階操作になっている。
    # 上の設定で半角全角キーにはCapsLockを割り当てているのでその代替処置。
    K("M-capslock"): K("M-grave"),

}, "Global keybinding")


# Gnomeターミナル、vlc Player以外で有効になるキーバインド
# wm_classを調べるには、$ xprop WM_CLASS を実行してウィンドウをクリック。
define_keymap(lambda wm_class: wm_class not in ("Gnome-terminal", "vlc"), {
    # カーソル移動 (Shiftで選択しながら移動)
    K("C-b"): K("left"),
    K("C-Shift-b"): K("Shift-left"),
    K("C-f"): K("right"),
    K("C-Shift-f"): K("Shift-right"),
    K("C-p"): K("up"),
    K("C-Shift-p"): K("Shift-up"),
    K("C-n"): K("down"),
    K("C-Shift-n"): K("Shift-down"),
    K("C-a"): K("home"),
    K("C-Shift-a"): K("Shift-home"),
    K("C-e"): K("end"),
    K("C-Shift-e"): K("Shift-end"),
    # 単語間移動 (自分用。Mac本来のキーバインドは、Option+ Left or Right)
    K("C-u"): K("C-Left"),
    K("C-i"): K("C-Right"),

    # Delete, Backspace
    K("C-d"): K("delete"),
    K("C-k"): [K("Shift-end"), K("delete")],
    K("C-h"): K("backspace"),

    # 修飾キー以外は大文字小文字を区別しない
    # K("C-H"): (K("bAcKsPaCe")),

    # 上記でつぶしたControlキーとの本来のキーバインドを、無変換キーとの組み合わせで補完する
    K("Muhenkan-b"): K("C-b"),
    K("Muhenkan-f"): K("C-f"),
    K("Muhenkan-p"): K("C-p"),
    K("Muhenkan-n"): K("C-n"),
    K("Muhenkan-a"): K("C-a"),
    K("Muhenkan-e"): K("C-e"),
    K("Muhenkan-u"): K("C-u"),
    K("Muhenkan-i"): K("C-i"),
    K("Muhenkan-d"): K("C-d"),
    K("Muhenkan-k"): K("C-k"),
    K("Muhenkan-h"): K("C-h"),

}, "mac-like keys")
