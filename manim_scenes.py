from manimlib.imports import *
from math import cos, sin, pi

class Temperature(Scene):
    def construct(self):
        title = TextMobject("Mnemonics for Common Temperature Conversions")
        self.play(FadeIn(title))
        self.wait(0)
        self.play(title.to_edge,TOP)
        self.wait(0)
        header = VGroup(TextMobject(r"$${}^\circ \mathrm{C}$$"), TextMobject(r"$${}^\circ \mathrm{F}$$"))
        header.arrange(RIGHT,buff=1)
        header.move_to(LEFT)
        celsius = VGroup(*[Integer(i) for i in [0,10,20,30]])
        celsius.arrange(DOWN)
        celsius.set_color_by_gradient(BLUE,RED)
        buff = 0.1
        celsius.next_to(header[0],BOTTOM,buff=buff)
        fahrenheit_for_color=VGroup(*[Integer(i) for i in [32, 50, 68, 86]])
        fahrenheit_for_color.set_color_by_gradient(BLUE,RED)
        fahrenheit = VGroup(fahrenheit_for_color[0], fahrenheit_for_color[1], VGroup(fahrenheit_for_color[2], fahrenheit_for_color[3]))
        fahrenheit[2].arrange(DOWN)
        fahrenheit.arrange(DOWN)
        fahrenheit.next_to(header[1],BOTTOM,buff=buff)
        self.play(Write(header))
        self.play(Write(celsius))
        def make_explainer(text,i):
            explainer = VGroup(Arrow(start=RIGHT/5,end=LEFT/5), TextMobject(text))
            explainer.arrange(RIGHT)
            explainer.next_to(fahrenheit[i],RIGHT)
            return explainer
        explainer = make_explainer("Freezing temp of water", 0)
        self.play(Write(fahrenheit[0]))
        self.play(ShowCreation(explainer))
        self.play(Write(fahrenheit[1]))
        explainer2 = make_explainer("Round number", 1)
        self.play(TransformFromCopy(explainer,explainer2))
        self.play(Write(fahrenheit[2]))
        final_explainer=VGroup(Brace(fahrenheit[2], RIGHT), TextMobject("Digits are reversed"))
        final_explainer.arrange(RIGHT)
        final_explainer.next_to(fahrenheit[2])
        self.play(TransformFromCopy(explainer2,final_explainer))
        self.wait(2)

class Temperature_try1(Scene):
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

class TrigDeriv(Scene):
    def construct(self):
        title = TextMobject("Why is $\sin'(x)=\cos(x)$?")
        title.to_edge(UP)
        self.play(Write(title))
        text = VGroup(TextMobject(r"Most proofs go through a lemma stating $$\lim_{x\to 0}\frac{\sin(x)}{x} = 0$$"), TextMobject("But this lemma actually isn't necessary"))
        text.arrange(DOWN, buff=1)
        text.next_to(title,DOWN, buff = 1)
        self.play(Write(text[0]))
        self.play(Write(text[1]))
        self.wait()
        self.play(Uncreate(text[0]), Uncreate(text[1]))
        text2 = TextMobject("All we need are the following two facts:")
        nums = VGroup(TextMobject("1."), TextMobject("2."))
        nums.arrange(DOWN)
        fact1 = TexMobject(r"\sin^2(x)"," + ", r"\cos^2(x)"," = 1")
        path = TexMobject(r"t\to(",r"\cos(t)",",",r"\sin(t)",")")
        fact2 = VGroup(TextMobject("The path"),path,TextMobject("has unit velocity"))
        fact2.arrange(DOWN)
        facts = VGroup(fact1, fact2)
        facts.arrange(DOWN)
#        num1 = TextMobject("1.")
#        num2 = TextMobject("2.")
#        num1.next_to(fact1,LEFT)
#        num1.to_edge(facts,LEFT)
#        num2.next_to(fact2,LEFT)
#        num2.to_edge(facts,LEFT)
        self.play(ShowCreation(fact1),ShowCreation(fact2))
        self.wait()
        self.play(
            Transform(fact1[0],TexMobject("f(x)^2").move_to(fact1[0])),
            Transform(fact1[2],TexMobject("g(x)^2").move_to(fact1[2])),
            Transform(path[1],TexMobject("f(t)").move_to(path[1])),
            Transform(path[3],TexMobject("g(t)").move_to(path[3])))
                            
