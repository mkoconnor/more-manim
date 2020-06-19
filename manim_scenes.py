from manimlib.imports import *
from math import cos, sin, pi

class Temperature(Scene):
    def construct(self):
        title = TextMobject("Mnemonics for Common Temperatures")
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))
        self.wait(1)
