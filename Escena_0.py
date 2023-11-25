from manin import *

class Escena_0(Scene):
    def construct(self):
        # Presentación
        title = MathTex("\\text{The Life of } \\pi \\text{ (2014)}").scale(1.2)
        pi_symbol1 = MathTex("\\pi").next_to(title, DOWN).scale(3)
        autors = Tex("Daniel Rodriguez - Tania Vasquez").scale(0.7).next_to(pi_symbol1, DOWN)

        self.play(Write(title), run_time=2)
        self.play(Write(pi_symbol1), run_time=2)
        self.play(Write(autors), run_time=2)
        self.wait(1)
        self.play(FadeOut(title), FadeOut(pi_symbol1), FadeOut(autors))

        # Escena 0: Introducción
        text1 = Tex("Bienvenidos a un viaje a través de la historia y los misterios de uno de los números más fascinantes en matemáticas: $\\pi$").scale(0.7).to_edge(UP)
        pi_symbol = MathTex(r"\pi").scale(4)
        self.play(Write(text1), run_time=2)
        self.play(pi_symbol.animate.scale(1.5).move_to(UP * 2), run_time=3)
        self.play(FadeOut(pi_symbol), run_time=2)
