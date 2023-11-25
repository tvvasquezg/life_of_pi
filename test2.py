from manim import *
import numpy as np

class VisualizePi(Scene):
    def construct(self):
        title2 = MathTex("\\text{Propiedades Matemáticas de } \\pi").to_edge(UP)
        properties_narration = MathTex("\\pi \\text{ es un número irracional y trascendental, no expresable como fracción exacta y no solución de ecuaciones algebraicas no triviales.}").scale(0.5).next_to(title2, DOWN)
        self.play(Write(title2))
        self.play(Write(properties_narration))
        self.wait(2)

         # Irracionalidad de Pi
        sub_title = MathTex("\\text{Irracionalidad de } \\pi").scale(0.7).next_to(properties_narration, DOWN)
        pi_decimals = DecimalNumber(
            3.14159,
            num_decimal_places=20,
            include_sign=False,
            font_size=36,
            group_with_commas=False
        ).next_to(sub_title, DOWN)
        self.play(Write(sub_title))
        self.play(Write(pi_decimals))


        # Configuraciones iniciales
        points_per_iteration = 6
        total_iterations = 4000  # Ajustar para una espiral más larga o más corta
        radius0 = 1
        radius1 = 1

        # Definir las funciones complejas
        z1 = lambda theta: radius0 * np.exp(1j * theta) + radius1 * np.exp(1j * np.pi * theta)

        # Lista para almacenar los puntos de la espiral
        spiral_points = []

        # Crear puntos iniciales para la espiral
        for iteration in range(0, points_per_iteration):
            theta = np.radians(iteration)
            new_point = z1(theta)
            spiral_points.append([new_point.real, new_point.imag, 0])

        # Inicializar la espiral con los puntos iniciales
        spiral = VMobject()
        spiral.set_points_as_corners(spiral_points)

        # Bucle de animación
        for iteration in range(points_per_iteration, total_iterations, points_per_iteration):
            theta = np.radians(iteration)
            new_point = z1(theta)
            spiral_points.append([new_point.real, new_point.imag, 0])

            # Actualizar la espiral con los nuevos puntos
            spiral.set_points_as_corners(spiral_points)

            # Animar la adición de un segmento a la espiral
            self.play(Create(Line(spiral_points[-2], spiral_points[-1])),run_time=0.001)

            # Título de la sección
            title = Text("π en la Era Digital", font_size=40)
            self.play(Write(title))
            self.wait(1)

     # Representación del cálculo moderno de π
        computer_icon = ImageMobject("computer_icon.png")
        pi_digits = DecimalNumber(3.14159, num_decimal_places=10)
        pi_stream = VGroup(computer_icon, pi_digits).arrange(DOWN)
            
        self.play(FadeIn(computer_icon))
        self.play(Transform(computer_icon, pi_digits))
        self.wait(2)
            # Animación de un contador de dígitos
        digit_counter = Integer(0).scale(2)
        self.play(ChangeDecimalToValue(digit_counter, 1000000), run_time=2)
        self.wait(1)

            # Transición al final
        self.play(FadeOut(title), FadeOut(pi_stream), FadeOut(digit_counter))

 