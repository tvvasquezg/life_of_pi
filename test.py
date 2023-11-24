from manim import *

class PiAnimation(Scene):
    def construct(self):
        # Crear un círculo
        circle = Circle(radius=2, color=BLUE)
        self.play(Create(circle))

        # Dibujar una línea que representa el diámetro
        diameter = Line(start=LEFT*2, end=RIGHT*2, color=GREEN)
        self.play(Create(diameter))

        # Crear un punto en el borde del círculo
        point_on_circle = Dot(point=circle.get_start())

        # Dibujar la circunferencia del círculo
        circumference = VGroup()
        for _ in range(36): # Aproximadamente igual a 2*pi
            circumference.add(point_on_circle.copy())
            point_on_circle.rotate(PI/18, about_point=ORIGIN)

        # Animar la circunferencia desplegándose en una línea
        self.play(Transform(circumference, Line(start=LEFT*6, end=RIGHT*6, color=RED)))

        # Mostrar la relación entre la circunferencia y el diámetro
        self.wait(1)
        self.play(Indicate(circumference), Indicate(diameter))
        self.wait(1)

        # Conclusión sobre el valor de pi
        pi_value = MathTex(r"\pi \approx \frac{Circumference}{Diameter}")
        self.play(Write(pi_value))
        self.wait(2)
