from manim import *
class PiEvolution(Scene):
    def get_polygon_inscribed_in_circle(self, circle, num_sides):
        radius = circle.radius - 0.1
        polygon = RegularPolygon(n=num_sides, radius=radius, color=BLUE)
        polygon.move_to(circle.get_center())
        angle = 360 / num_sides
        label = MathTex(f"{angle}^\\circ").next_to(circle.get_center(), UP).scale(0.5)
        return polygon, label

    def get_polygon_circumscribed_about_circle(self, circle, num_sides):
        radius = circle.radius + 0.1
        polygon = RegularPolygon(n=num_sides, radius=radius, color=RED)
        polygon.move_to(circle.get_center())
        angle = 360 / num_sides
        label = MathTex(f"{angle}^\\circ").next_to(circle.get_center(), UP).scale(0.5)
        return polygon, label

    def construct(self):
        # Presentación centrada
        title = MathTex("\\text{The Life of } \\pi \\text{ (2014)}").scale(1.5).to_edge(UP)
        pi_symbol1 = MathTex("\\pi").scale(3).next_to(title, DOWN)
        authors = Tex("Daniel Rodriguez - Tania Vasquez").scale(0.9).next_to(pi_symbol1, DOWN)
        self.play(Write(title), run_time=2)
        self.play(Write(pi_symbol1), run_time=2)
        self.play(Write(authors), run_time=2)
        self.wait(1)
        self.play(FadeOut(title), FadeOut(pi_symbol1), FadeOut(authors))

        # Escena 0: Introducción
        text1 = Tex("Bienvenidos a un viaje a través de la historia y los misterios de uno de los números más fascinantes en matemáticas: $\\pi$").scale(0.7).to_edge(UP)
        pi_symbol = MathTex(r"\pi").scale(4).move_to(ORIGIN)
        self.play(Write(text1), run_time=2)
        self.play(pi_symbol.animate.scale(1.5).move_to(UP * 2), run_time=3)
        self.play(FadeOut(pi_symbol), run_time=2)

        # Escena 1: Animación de un círculo
        circle = Circle(radius=2, color=BLUE).shift(LEFT * 3)
        text2 = Tex(r"\(\pi\) es conocido por todos como la relación entre la circunferencia de un círculo y su diámetro").scale(0.5).next_to(circle, DOWN, buff=1)
        diameter = Line(start=circle.get_left(), end=circle.get_right(), color=RED)
        formula = MathTex("\\pi = \\frac{C}{d}").next_to(circle, RIGHT, buff=2)

        self.play(Create(circle), Write(text2), run_time=3)
        self.play(Create(diameter), Write(formula), run_time=3)
        self.wait(1)

        # Escena 2: Breve mención de su uso
        text3 = Tex("Desde la construcción de las pirámides hasta los modernos cálculos de ingeniería y ciencia, $\\pi$ juega un papel crucial").scale(0.6).to_edge(DOWN)
        pyramid = ImageMobject("C:\\Users\\yotai\\Documents\\Algebra\\life_of_pi\\media\\images\\manin\\keops.jpg").next_to(circle, RIGHT, buff=2)
        
        self.play(Write(text3), FadeOut(text2),FadeOut(text1), run_time=2)
        self.play(FadeIn(pyramid), run_time=2)
        self.wait(1)

        # Transición a la siguiente escena
        self.play(FadeOut(circle), FadeOut(diameter), FadeOut(formula), FadeOut(text3), FadeOut(pyramid))

        # Historia
        text5 = Tex("Acompáñanos para descubrir cómo $\\pi$ ha sido calculado, estudiado y celebrado a lo largo de los siglos").scale(0.5).move_to(ORIGIN)
        self.play(Write(text5))
        self.wait(2)
        self.play(FadeOut(text5))

        # Crear la línea de tiempo
        tex_li = Tex("Liniea del tiempo de $\\pi$.")
        timeline = NumberLine(
            x_range=[-3500, 2014, 500],  # Ajustar según el número de eventos
            length=10,
            color=BLUE,
            include_numbers=True,
            label_direction=DOWN,
            font_size=20
        ).to_edge(DOWN)
        self.play(Create(timeline))
        self.wait(1)

        events = [
            {"year": -3000, "text": "Babilonios y Egipcios", "value": "3.125 - 3.1604"},
            {"year": -250, "text": "Arquímedes", "value": "3.14"},
            {"year": 500, "text": "Tsu Chung-Chih", "value": "3.141592"},
            {"year": 1400, "text": "Al-Kāshī", "value": "3.1415926535"},
            {"year": 2000, "text": "Era Digital", "value": "Billones de dígitos"},
        ]

        for i, event in enumerate(events):
            dot = Dot(color=RED).move_to(timeline.n2p(event["year"]))
            text = Text(event["text"], font_size=15).next_to(dot, UP*(i+2))
            value = Text(event["value"], font_size=15).next_to(dot, DOWN*(i+1))
            self.play(FadeIn(dot), Write(text), Write(value), run_time=1)
            self.wait(1)

            # Ajustes para las imágenes de cada evento
            if i == 0:
                babi = ImageMobject("C:\\Users\\yotai\\Documents\\Algebra\\life_of_pi\\media\\images\\pi\\babilonios.jpeg").move_to(ORIGIN)
                self.play(FadeIn(babi), run_time=2)
            elif i == 1:
                circle = Circle(radius=2, color=WHITE).move_to(ORIGIN)
                self.play(FadeOut(babi), Create(circle), run_time=2)

                # Polígonos para Arquímedes
                num_iterations = 6
                for sides in range(4, num_iterations + 4):
                    inscribed_polygon, inscribed_label = self.get_polygon_inscribed_in_circle(circle, sides)
                    circumscribed_polygon, circumscribed_label = self.get_polygon_circumscribed_about_circle(circle, sides)
                    self.play(Create(inscribed_polygon), Write(inscribed_label), run_time=0.5)
                    self.play(FadeOut(inscribed_polygon), FadeOut(inscribed_label), run_time=0.5)
                    self.play(Create(circumscribed_polygon), Write(circumscribed_label), run_time=0.5)
                    self.play(FadeOut(circumscribed_polygon), FadeOut(circumscribed_label), run_time=0.5)

                self.wait(1)
            elif i == 2:
                chino = ImageMobject("C:\\Users\\yotai\\Documents\\Algebra\\life_of_pi\\media\\images\\pi\\china.jpg").move_to(LEFT)
                tsu = ImageMobject("C:\\Users\\yotai\\Documents\\Algebra\\life_of_pi\\media\\images\\pi\\tsu.jpg").next_to(chino, RIGHT)
                self.play(FadeOut(circumscribed_polygon), FadeOut(circle), FadeIn(chino), FadeIn(tsu), run_time=2)
            elif i == 3:
                alga = ImageMobject("C:\\Users\\yotai\\Documents\\Algebra\\life_of_pi\\media\\images\\pi\\alga.jpeg").move_to(ORIGIN)
                self.play(FadeOut(tsu), FadeIn(alga), run_time=2)
            elif i == 4:
                pip = ImageMobject("C:\\Users\\yotai\\Documents\\Algebra\\life_of_pi\\media\\images\\pi\\pi.png").scale(0.5).move_to(ORIGIN)
                self.play(FadeOut(alga), FadeIn(pip), run_time=2)

        self.play(FadeOut(timeline), *[FadeOut(mob) for mob in self.mobjects],FadeOut(tex_li))
        self.wait(1)

        # Sección de Cultura Popular
        title1 = MathTex("\\pi \\text{ en la Cultura Popular}").to_edge(UP)
        intro_narrationCP = MathTex(" \\pi \\text{ ha capturado la imaginación en la cultura popular, apareciendo en películas, literatura y arte.}").scale(0.5).next_to(title1, DOWN)
        self.play(Write(title1))
        self.play(Write(intro_narrationCP))

        # Imágenes representativas de la cultura popular
        book = ImageMobject("C:\\Users\\yotai\\Documents\\Algebra\\life_of_pi\\media\\images\\pi\\book.png").next_to(intro_narrationCP, DOWN)
        culture = ImageMobject("C:\\Users\\yotai\\Documents\\Algebra\\life_of_pi\\media\\images\\pi\\2.png").next_to(book, RIGHT)
        self.play(FadeIn(book), FadeIn(culture), run_time=3)
        self.play(FadeOut(title1), FadeOut(intro_narrationCP))
        self.wait(2)

        # Propiedades Matemáticas de Pi
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
            self.play(Create(Line(spiral_points[-2], spiral_points[-1])),run_time=0.0000001)

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






















        self.wait(1)

        # Cambio gradual de los decimales de Pi
        for _ in range(5):
            new_decimal = DecimalNumber(
                3.14159,
                num_decimal_places=20,
                include_sign=False,
                font_size=36,
                group_with_commas=False
            ).next_to(sub_title, DOWN)
            self.play(Transform(pi_decimals, new_decimal), run_time=2)
            self.wait(1)

        # Transición a la siguiente sección
        self.play(FadeOut(title2), FadeOut(properties_narration), FadeOut(sub_title), FadeOut(pi_decimals))
        self.wait(1)