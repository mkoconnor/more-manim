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

class TrigSpecifDeriv(Scene):
    def construct(self):
        text1 = TextMobject("Starting from the first property...").to_edge(TOP)
        orig = TexMobject(r"\sin^2(x)+\cos^2(x)","=","1")
        deriv=TexMobject("[",r"\sin^2(x)+\cos^2(x)","]'","=","1","{}'")
        self.play(Write(text1))
        self.play(Write(orig))
        self.wait()
        text2 = TextMobject("...differentiate both sides.").to_edge(TOP)
        self.play(Transform(text1,text2))
        self.wait()
        self.play(ReplacementTransform(orig[0],deriv[1]),ReplacementTransform(orig[2],deriv[4]))
        self.play(Write(deriv[0]),Write(deriv[2]),Write(deriv[3]),Write(deriv[5]))
        deriv_with_zero_expanded=TexMobject("[",r"\sin^2(x)+\cos^2(x)","]'","=","0")
        self.play(
            ReplacementTransform(VGroup(deriv[4], deriv[5]), deriv_with_zero_expanded[4]),
            *[ReplacementTransform(deriv[i],deriv_with_zero_expanded[i]) for i in range(4)])
        deriv_expanded=TexMobject(r"\sin(x)\sin'(x) + \cos(x)\cos'(x)", "=", "0")
        self.play(
            ReplacementTransform(
                VGroup(*[deriv_with_zero_expanded[i] for i in [0,1,2]]),
                deriv_expanded[0]),
            *[ReplacementTransform(
                deriv_with_zero_expanded[i + 2], deriv_expanded[i]) for i in [1, 2]])

class TrigSpecifPath(Scene):
    def construct(self):
        path_expr = TexMobject(r"t\longmapsto (",r"\cos", "(","t",")",",",r"\sin", "(","t",")",")")
        path_text = VGroup(TextMobject("The path"), path_expr, TextMobject("has unit speed"))
        path_text.arrange(DOWN)
        self.play(Write(path_text))
        self.wait()
        path_eq = TexMobject(r"\cos", r"{}'^2", "(", "t", ")", "+", r"\sin", r"{}'^2{}", "(", "t", ")", "=", "1", "{}^2")
        sqrt = TexMobject(r"\sqrt{\phantom{\cos'^2(t)+\sin'^2(t)")
        sqrt.move_to(path_eq,aligned_edge=LEFT)
        sqrt.shift(LEFT * 0.4)
        self.play(
            FadeOut(path_text[0]),
            FadeOut(path_text[2]),
            *[FadeOut(path_expr[i]) for i in [0,5,10]]
        )
        self.play(
            ReplacementTransform(
                path_expr[1], path_eq[0]
                ),
            ReplacementTransform(
                path_expr[2], path_eq[2]
                ),
            ReplacementTransform(
                path_expr[3], path_eq[3]
                ),
            ReplacementTransform(
                path_expr[4], path_eq[4]
                ),
            ReplacementTransform(
                path_expr[6], path_eq[6]
                ),
            ReplacementTransform(
                path_expr[7], path_eq[8]
                ),
            ReplacementTransform(
                path_expr[8], path_eq[9]
                ),
            ReplacementTransform(
                path_expr[9], path_eq[10]
                ),
            Write(sqrt),
            *[Write(path_eq[i]) for i in [1,5,7,11,12]])
        self.play(Uncreate(sqrt), Write(path_eq[13]))
        self.play(Uncreate(path_eq[13]))

class TrigSystem(Scene):
    def construct(self):
        line1 = TextMobject("So, we have a system of two equations")
        line2 = TextMobject(r"in the two unknowns ", r"$\sin'(x)$", " and ", r"$\cos'(x)$:")
        line2[1].set_color(YELLOW)
        line2[3].set_color(YELLOW)
        text = VGroup(line1, line2)
        text.arrange(DOWN)
        text.to_edge(TOP)
        self.play(Write(text))
        self.wait()
        first_eq = TexMobject(r"\sin(x)", r"\sin'(x)", "+", r"\cos(x)", r"\cos'(x)", "=0")
        first_eq[1].set_color(YELLOW)
        first_eq[4].set_color(YELLOW)
        second_eq = TexMobject(r"\sin'(x)","{}^2+", r"\cos'(x)", "{}^2=1")
        second_eq[0].set_color(YELLOW)
        second_eq[2].set_color(YELLOW)
        system=VGroup(first_eq,second_eq)
        system.arrange(DOWN)
        system.shift(BOTTOM / 4)
        self.play(Write(system))
        
class TrigSolution(Scene):
    def construct(self):
        text = TextMobject("Solving with the quadratic formula yields two solutions:")
        text.to_edge(TOP)
        sol1 = TexMobject(r"\sin'(x)=\cos(x)", r"\cos'(x)=-\sin(x)").arrange(DOWN).shift(DOWN/5)
        sol2 = TexMobject(r"\sin'(x)=-\cos(x)", r"\cos'(x)=\sin(x)").arrange(DOWN)
        sol2.next_to(sol1,DOWN, buff = 1)
        self.play(Write(text))
        rect1 = SurroundingRectangle(sol1)
        self.play(Write(sol1),ShowCreation(rect1))
        rect2 = SurroundingRectangle(sol2)
        self.play(Write(sol2),ShowCreation(rect2))
        self.wait()
        self.play(Uncreate(text),Uncreate(sol2),Uncreate(rect2))
        text2 = TextMobject(r"The initial conditions $\cos(0)=1$ and $\sin(0)>0$ leave", "just this one:").arrange(DOWN).to_edge(TOP)
        self.play(Write(text2))
        self.wait()
        qed = TextMobject("QED :)").next_to(rect1,BOTTOM)
        self.play(Write(qed))
    
                            
