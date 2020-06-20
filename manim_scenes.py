from manimlib.imports import *
from math import cos, sin, pi

class Temperature(Scene):
    def construct(self):
        title = VGroup(*[TextMobject(s) for s in ["Mnemonics", "for", "Common", "Temperatures"]])
        title.arrange(RIGHT)
        title.set_color_by_gradient(PINK,BLUE,YELLOW)
        title.to_edge(UP)
        ul = Line()
        ul.scale(title.get_width() / ul.get_width())
        ul.move_to(title,BOTTOM)
        bottom = Text("Wait, this is just text?")
        bottom.to_edge(BOTTOM)
        arrow = Arrow()
        self.play(Write(title), ShowCreation(ul), Write(bottom), Write(arrow), Write(NumberPlane()))
        self.wait(2)
        self.play(title.scale,3)
        self.play(arrow.rotate, pi)
        self.play(title.move_to,bottom,{"aligned_edge":LEFT})
        title.set_color(RED)
        self.play(FadeOut(title))
        self.wait(2)

        
class ToEdgeTest(Scene):
    def construct(self):
        self.to_edge_test()
        self.to_edge_test(buff=0.5)

    def to_edge_test(self, buff=0):
        text = Text("Hello", font='Arial', stroke_width=1, size = 0.4)
        rect = Rectangle(width=0.3, height=text.get_height(), stroke_color=RED)

        group = VGroup(rect,text).arrange(RIGHT)
        group.save_state()
        self.add(group)

        for d in [LEFT,RIGHT,UP,DOWN]:
            self.play(group.to_edge, d, {"buff":buff})
            self.wait()
            group.restore()
        self.remove(group)
