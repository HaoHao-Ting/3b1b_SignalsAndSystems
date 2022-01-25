from manim import *

class Lec1(Scene):
    def construct(self):
        text1 = Text('中国Hello')
        self.play(Write(text1))
        circle = Circle()
        square = Square()
        self.play(FadeIn(circle))



