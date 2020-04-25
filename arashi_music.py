# -*- coding: utf-8 -*-
import pyxel

WINDOW_H = 100
WINDOW_W = 140

class App:
    def __init__(self):
        self.IMG_ID0 = 0 #クレーン
        self.music_flug = False
        #windowの設定(幅、高さ、名前)
        pyxel.init(WINDOW_W, WINDOW_H, caption="Musicplayer", fps=10)
        #pyxeleditorのRetroRPGgame.pyxresを挿入
        #pyxeleditorで作った画像はimage(0)になる
        pyxel.load("arashi.pyxres")
        #Falseにするとマウス非表示
        pyxel.mouse(False)
        #BGM music1


        pyxel.run(self.update, self.draw)


    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btnp(pyxel.KEY_1):
            pyxel.playm(0, loop=False)
        if pyxel.btnp(pyxel.KEY_2):
            pyxel.playm(1, loop=False)
        if pyxel.btnp(pyxel.KEY_3):
            pyxel.playm(2, loop=False)
        if pyxel.btnp(pyxel.KEY_4):
            pyxel.playm(3, loop=False)
        if pyxel.btnp(pyxel.KEY_5):
            pyxel.playm(4, loop=False)
        #if pyxel.btnp(pyxel.KEY_5):
        #    pyxel.playm(5, loop=False)

    def draw(self):
        pyxel.cls(6)

        #0-0:close #32-0:open
        pyxel.blt(0, 0, 0, 32, 16, 32, 32, 0) #太陽

        pyxel.blt(pyxel.frame_count % pyxel.width, 0, 0, 0, 0, 32, 16, 0) #雲
        pyxel.blt(-140 + pyxel.frame_count % pyxel.width, 0, 0, 0, 0, 32, 16, 0) #雲

        pyxel.blt(30 + pyxel.frame_count % pyxel.width, 15, 0, 32, 0, 32, 16, 0) #雲
        pyxel.blt(-110 + pyxel.frame_count % pyxel.width, 15, 0, 32, 0, 32, 16, 0) #雲

        pyxel.blt(80 + pyxel.frame_count % pyxel.width, 65, 0, 0, 16, 32, 16, 0) #雲
        pyxel.blt(-60 + pyxel.frame_count % pyxel.width, 65, 0, 0, 16, 32, 16, 0) #雲

        #pyxel.blt(120, pyxel.frame_count % pyxel.height, 0, 0, 32, 16, 40, 0) #風船

        pyxel.blt(30, 84, 1, 16*(pyxel.frame_count % 4), 0, 16, 16, 0) #大野智
        pyxel.blt(45, 84, 1, 16*(pyxel.frame_count % 4), 16, 16, 16, 0) #櫻井翔
        pyxel.blt(60, 84, 1, 16*(pyxel.frame_count % 4), 32, 16, 16, 0) #相葉雅紀
        pyxel.blt(75, 84, 1, 16*(pyxel.frame_count % 4), 48, 16, 16, 0) #二宮和也
        pyxel.blt(90, 84, 1, 16*(pyxel.frame_count % 4), 64, 16, 16, 0) #松本潤

        pyxel.text(40, 35, "WELCOME TO Pyxel!", 7)

        pyxel.text(10, 43, "THIS IS MUSIC PLAYER OF ARASHI", 7)
        pyxel.text(10, 51, "PUSH 1-5 kEY TO START MUSIC!", pyxel.frame_count % 16)

        pyxel.text(18, 62, "1. A RA SHI", 10)
        pyxel.text(18, 70, "2. Happiness", 5)
        pyxel.text(18, 78, "3. Love so sweet", 8)

        pyxel.text(73, 62, "4. Monster", 3)
        pyxel.text(73, 70, "5. sakura sake", 2)
        #pyxel.text(73, 78, "5. ", 8)

App()
