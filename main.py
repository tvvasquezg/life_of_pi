# -*- coding: utf-8 -*-
from manim import *
#from Escena_0 import Escena_0

class Escena_0(Scene):
    def construct(self):
        # Presentación
        title = MathTex("\\text{The Life of } \\pi \\text{ (2014)}").scale(1.2)
        pi_symbol1 = MathTex("\\pi").next_to(title, DOWN).scale(3)
        autors = Tex("Daniel Ricardo Rodriguez Olarte").scale(0.7).next_to(pi_symbol1, DOWN)
        autors1 = Tex("Tania Vanesa Vasquez Guevara").scale(0.7).next_to(autors, DOWN)

        self.play(Write(title), run_time=2)
        self.play(Write(pi_symbol1), run_time=2)
        self.play(Write(autors),Write(autors1), run_time=2)
        self.wait(1)
        self.play(FadeOut(title), FadeOut(pi_symbol1), FadeOut(autors),FadeOut(autors1))

        # Escena 0: Introducción
        text1 = Tex("Bienvenidos a un viaje a través de la historia y los misterios de uno de los números más fascinantes en matemáticas: $\\pi$").scale(0.9).to_edge(UP-(1))
        pi_symbol = MathTex(r"\pi").scale(4)
        self.play(Write(text1), run_time=2)
        self.play(pi_symbol.animate.scale(1.5).move_to(UP * 2), run_time=3)
        self.play(FadeOut(pi_symbol),FadeOut(text1), run_time=2)


class Escena_1(Scene):
    def construct(self):
        # Escena 1: Animación de un círculo
        text2 = Tex(r"\(\pi\) es conocido por todos como la relación entre la circunferencia de un círculo y su diámetro").scale(0.7).to_edge(UP*(0.5))

        circle = Circle(radius=2, color=BLUE)
        self.play(Create(circle), Write(text2))

        # Dibujar una línea que representa el diámetro
        diameter = Line(start=LEFT * 2, end=RIGHT * 2, color=GREEN)
        self.play(Create(diameter))

        # Crear un punto en el borde del círculo
        point_on_circle = Dot(point=circle.get_start())

        # Dibujar la circunferencia del círculo
        circumference = VGroup()
        for _ in range(36):  # Aproximadamente igual a 2*pi
            circumference.add(point_on_circle.copy())
            point_on_circle.rotate(PI / 18, about_point=ORIGIN)

        # Animar la circunferencia desplegándose en una línea
        self.play(Transform(circumference, Line(start=LEFT * 6, end=RIGHT * 6, color=RED)))

        # Mostrar la relación entre la circunferencia y el diámetro
        self.wait(1)
        self.play(Indicate(circumference), Indicate(diameter))
        self.play(FadeOut(circumference), FadeOut(diameter))

        formula = MathTex("\\pi = \\frac{C}{d}").next_to(circle, RIGHT, buff=2)

        # Desvanecer el círculo antes de mostrar la ecuación
        self.play(FadeOut(circle), Write(formula), run_time=2)
        

        pyramid = ImageMobject("C:\\Users\\yotai\\Documents\\Algebra\\life_of_pi\\media\\images\\manin\\keops.jpg").next_to(formula,LEFT*(7))
        #self.play(FadeIn(pyramid), run_time=2)

        # Escena 2: Breve mención de su uso
        text3 = Tex("Desde la construcción de las pirámides hasta los modernos cálculos de ingeniería y ciencia, $\\pi$ juega un papel crucial").scale(0.6).to_edge(DOWN*(2))
        self.play(Write(text3),FadeIn(pyramid), run_time=3)

        
        self.wait(2)

        # Transición a la siguiente escena
        self.play(FadeOut(formula), FadeOut(text3), FadeOut(pyramid))


class Escena_2(Scene):
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
         # Historia
        text5 = Tex("Acompáñanos para descubrir cómo $\\pi$ ha sido calculado, estudiado y celebrado a lo largo de los siglos").scale(0.5).move_to(ORIGIN)
        self.play(Write(text5))
        self.wait(2)
        self.play(FadeOut(text5))

        # Crear la línea de tiempo
        tex_li = Tex("Linea del tiempo de $\\pi$.")
        self.play(Write(tex_li))
        timeline = NumberLine(
            x_range=[-3500, 2014, 1000],  # Ajustar según el número de eventos
            length=11,
            color=BLUE,
            include_numbers=True,
            label_direction=DOWN,
            font_size=20
        ).to_edge(DOWN+(1))
        self.play(Create(timeline),FadeOut(timeline))
        self.wait(1)

        events = [
    {"year": -3000, "text": "Babilonios y Egipcios", "value": "2"},
    {"year": -150, "text": "Ptolemy", "value": "3"},
    {"year": -250, "text": "Arquímedes", "value": "3"},
    {"year": -263, "text": "Liu Hui", "value": "5"},
    {"year": 480, "text": "Tsu Ch’ung Chi", "value": "4"},
    {"year": 1429, "text": "Al-Kashi", "value": "14"},
    {"year": 1699, "text": "Sharp (and Halley)", "value": "71"},
    {"year": 1706, "text": "Machin", "value": "100"},
    {"year": 1853, "text": "Rutherford", "value": "440"},
    {"year": 1947, "text": "Ferguson (Calculator)", "value": "808"},
    {"year": 1949, "text": "Reitwiesner et al. (ENIAC)", "value": "2037"},
    {"year": 1958, "text": "Genyus", "value": "10000"},
    {"year": 1981, "text": "Miyoshi and Kanada", "value": "2000036"},
    {"year": 1987, "text": "Kanada et. al Jan.", "value": "134217700"},
    {"year": 1989, "text": "Kanada and Tamura Nov.", "value": "1073741799"},    
    {"year": 1994, "text": "Chudnovskys May", "value": "4044000000"},
    {"year": 1999, "text": "Kanada and Takahashi Sep.", "value": "206158430000"},
    {"year": 2002, "text": "Kanada-Ushiro-Kuroda Dec.", "value": "1241100000000"},
    {"year": 2009, "text": "Bellard Dec.", "value": "2699999990000"}
]


        for i, event in enumerate(events):
            dot = Dot(color=RED).move_to(timeline.n2p(event["year"]))
            text = Text(event["text"], font_size=15).next_to(dot, UP*(i+1))
            value = Text(event["value"], font_size=11).next_to(dot, DOWN*(i+(0.8)))
            self.play(FadeIn(dot), Write(text), Write(value), run_time=1)
            self.play(FadeOut(dot),FadeOut(text),run_time=0.25)
            self.wait(0.5)

            # Ajustes para las imágenes de cada evento
            if i == 0:
                babi = ImageMobject("C:\\Users\\yotai\\Documents\\Algebra\\life_of_pi\\media\\images\\pi\\babilonios.jpeg").move_to(DOWN-(1))
                self.play(FadeIn(babi), run_time=2)
                text1 = Tex(r"Históricamente, las aproximaciones de $\pi$ han variado, con los babilonios utilizando 3.125 y los egipcios $\frac{256}{81}$ que es igual a 3.1604").scale(0.7).to_edge(UP)
                text2 = Tex(r"También se ha propuesto que los hebreos usaron $\pi$ igual a 3 basándose en un verso bíblico I de Reyes 7:23 que dice:").scale(0.5).next_to(text1, DOWN)
                text3 = Tex(r"Luego hizo el mar de fundición, que tenía diez codos de borde a borde; era completamente redondo, su altura era de cinco codos y una línea de treinta codos lo rodeaba.Acá se deduce que se tomaba $\pi$ como $\frac{30}{10}$ ").scale(0.5).to_edge(UP)

                # Transiciones
                self.play(Write(text1), run_time=6)
                self.wait(3)
                self.play(FadeOut(text1), Write(text2), run_time=6)
                self.wait(3)
                self.play(FadeOut(text2), Write(text3), run_time=6)
                self.wait(3)
                self.play(FadeOut(text3))
                self.wait(1)
            elif i == 1:
                circle = Circle(radius=2, color=WHITE).move_to(ORIGIN)
                self.play(FadeOut(babi), Create(circle), run_time=2)

                # Polígonos para Arquímedes
                num_iterations = 6
                for sides in range(4, num_iterations + 4):
                    inscribed_polygon, inscribed_label = self.get_polygon_inscribed_in_circle(circle, sides)
                    circumscribed_polygon, circumscribed_label = self.get_polygon_circumscribed_about_circle(circle, sides)
                    self.play(Create(inscribed_polygon), Write(inscribed_label), run_time=0.7)
                    self.play(FadeOut(inscribed_polygon), FadeOut(inscribed_label), run_time=0.7)
                    self.play(Create(circumscribed_polygon), Write(circumscribed_label), run_time=0.7)
                    self.play(FadeOut(circumscribed_polygon), FadeOut(circumscribed_label), run_time=0.7)

                self.wait(3)
            elif i == 2:
                chino = ImageMobject("C:\\Users\\yotai\\Documents\\Algebra\\life_of_pi\\media\\images\\pi\\china.jpg").move_to(DOWN-(1))
                tsu = ImageMobject("C:\\Users\\yotai\\Documents\\Algebra\\life_of_pi\\media\\images\\pi\\tsu.jpg").next_to(chino, RIGHT)
                self.play(FadeOut(circumscribed_polygon), FadeOut(circle), FadeIn(chino), FadeIn(tsu), run_time=2)
            elif i == 3:
                alga = ImageMobject("C:\\Users\\yotai\\Documents\\Algebra\\life_of_pi\\media\\images\\pi\\alga.jpeg").move_to(DOWN-(1))
                self.play(FadeOut(tsu), FadeIn(alga), run_time=2)
                self.play(FadeOut(alga),FadeOut(chino))
            elif i == 15:
                pip = ImageMobject("C:\\Users\\yotai\\Documents\\Algebra\\life_of_pi\\media\\images\\pi\\pi.png").scale(0.3).move_to(DOWN-(1))
                self.play(FadeOut(alga), FadeIn(pip), run_time=2)
                txtpi = Tex(r"La significativa mejora en la aproximación de $\pi$ a lo largo de los siglos destaca la evolución del conocimiento matemático y las técnicas computacionales,").scale(0.7).to_edge(UP)
                textpi1 = Tex(r"culminando en valores de $\pi$ cada vez más precisos en la era moderna, como los logrados por Bellard en 2009.").scale(0.7).move_to(txtpi)
                self.play(Write(txtpi),run_time=(10))
                self.play(FadeOut(txtpi))
                self.play(Write(textpi1),FadeOut(pip),run_time=5)

                self.wait(2)
        self.play(FadeOut(timeline), *[FadeOut(mob) for mob in self.mobjects],FadeOut(tex_li))
        self.wait(1)

class Escena_3(Scene):
    def construct(self):
        # Sección de Cultura Popular
        title1 = MathTex("\\pi \\text{ en la Cultura Popular}").to_edge(UP)
        intro_narrationCP = MathTex(" \\pi \\text{ ha capturado la imaginación en la cultura popular, apareciendo en películas, literatura y arte.}").scale(0.5).next_to(title1, DOWN)
        self.play(Write(title1))
        self.play(Write(intro_narrationCP))

        # Imágenes representativas de la cultura popular
        book = ImageMobject("C:\\Users\\yotai\\Documents\\Algebra\\life_of_pi\\media\\images\\pi\\book.png").next_to(intro_narrationCP, DOWN)
        book1 = ImageMobject("C:\\Users\\yotai\\Documents\\Algebra\\life_of_pi\\media\\images\\pi\\Libros.png").next_to(intro_narrationCP, DOWN)
        book2 = ImageMobject("C:\\Users\\yotai\\Documents\\Algebra\\life_of_pi\\media\\images\\main\\joyofpi_.jpg").next_to(intro_narrationCP, DOWN)        
        culture = ImageMobject("C:\\Users\\yotai\\Documents\\Algebra\\life_of_pi\\media\\images\\pi\\2.png").next_to(intro_narrationCP, DOWN)
        culture1 = ImageMobject("C:\\Users\\yotai\\Documents\\Algebra\\life_of_pi\\media\\images\\pi\\Cultura.jpeg").next_to(intro_narrationCP, DOWN)                            
        piday = ImageMobject("C:\\Users\\yotai\\Documents\\Algebra\\life_of_pi\\media\\images\\pi\\pi2.png").next_to(intro_narrationCP, DOWN)        
        piday1 = ImageMobject("C:\\Users\\yotai\\Documents\\Algebra\\life_of_pi\\media\\images\\pi\\Pida.png").next_to(intro_narrationCP, DOWN)        
        self.play(FadeIn(culture), run_time=3)
        self.play(FadeOut(culture))
        self.play(FadeIn(culture1),run_time =2)
        self.play(FadeOut(culture1))
        self.play(FadeIn(book), run_time=2)
        self.play(FadeOut(book))
        self.play(FadeIn(book2),run_time =2)
        self.play(FadeOut(book2))
        self.play(FadeIn(book1),run_time =2)
        self.play(FadeOut(book1))
        self.play(FadeIn(piday),run_time =2)
        self.play(FadeOut(piday))
        self.play(FadeIn(piday1),run_time =2)
        self.play(FadeOut(piday1))
        self.wait(2)

class Escena_4(Scene):
    def construct(self):
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


class GregoryAnomaly(Scene):
    def construct(self):
        # Título
        title = Text("Una Anomalía Curiosa en la Serie de Gregory", font_size=24)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # Serie de Gregory para π
        gregory_series = MathTex(
            r"\pi = 4 \sum_{k=1}^{\infty} \frac{(-1)^{k+1}}{2k - 1} = 4 \left( 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \frac{1}{9} - \frac{1}{11} + \cdots \right)"
        )
        self.play(Write(gregory_series))
        self.wait(1)
        self.play(FadeOut(gregory_series))

        # Valor aproximado de π - Parte 1 (en blanco)
        approx_pi_part1 = MathTex(
            r"3.14159245358979323846264338327950278419716939938730582097494182230781640\ldots"
        ).scale(0.5)
        # Valor aproximado de π - Parte 2 (con números específicos en rojo)
        # Separando cada dígito/elemento en su propio MathTex
        digits = [
            "3.141592",
            "6",  # Rojo
            "53589793238462643383279502", 
            "8",  # Rojo
            "841971693993", 
            "7",  # Rojo
            "5",  # Rojo
            "1",  # Rojo
            "0582097494", 
            "459",  # Rojo
            "230781640\ldots"
        ]
        approx_pi_part2 = VGroup(*[MathTex(digit, color=RED if digit in ["6", "8", "7", "5", "1", "459"] else WHITE) for digit in digits])
        approx_pi_part2.arrange(RIGHT, buff=0.1).scale(0.5).next_to(approx_pi_part1, DOWN, aligned_edge=LEFT)

        # Animar la escritura del valor aproximado de π
        self.play(Write(approx_pi_part1))
        self.play(Write(approx_pi_part2))
        self.wait(1)

        # Resaltar los números en rojo
        for digit in approx_pi_part2:
            if digit.get_color() == RED:
                self.play(Indicate(digit, scale_factor=1.2))
        self.wait(1)

class Escena_5(Scene):
    def construct(self):
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


class PiHistory(Scene):
    def construct(self):
        # Escena 1: Era digital de Pi
        text = Tex(r"Era Digital de $\pi$").to_edge(UP)
        text1 = Text("La era digital de Pi comenzó con la Transformada\n"
                     "Rápida de Fourier en 1965, que aceleró enormemente\n"
                     "los cálculos matemáticos.",
                     font_size=24,
                     color=WHITE)
        self.play(Write(text),Write(text1), run_time=7)
        self.wait(2)
        self.play(FadeOut(text1))

        # Escena 2: ENIAC y serie de Ballantine
        text2 = Text("La ENIAC, una de las primeras computadoras,\nrealizó el primer cálculo computarizado de Pi,\nseguido por la obtención de un millón de dígitos\nen 1973 usando la serie de Ballantine.",
                     font_size=24,
                     color=WHITE).shift(UP*2)
        #self.play(Write(text2), run_time=4)
        

        # Espacio para imagen
        # Aquí puedes insertar tu código para la imagen
        enic  = ImageMobject("C:\\Users\\yotai\\Documents\\Algebra\\life_of_pi\\media\\images\\main\\Eniac.jpg").next_to(text2,DOWN)
        self.play(Write(text2),run_time =5)
        self.play(FadeIn(enic),run_time =5)
        self.wait(2)
        self.play(FadeOut(text2),FadeOut(enic))

        # Escena 3: Algoritmo Cuadrático de Salamin-Brent
        text3 = Text("El Algoritmo Cuadrático de Salamin-Brent,\ndesarrollado en 1976, mejoró la eficiencia del\ncálculo de Pi mediante la iteración de la\nmedia aritmético-geométrica (AGM).",
                     font_size=24,
                     color=WHITE).shift(UP*1.5)
        formula_sb = MathTex(
            r"a_0 = 1, \quad b_0 = \frac{1}{\sqrt{2}}, \quad s_0 = \frac{1}{2}, \\"
            r"a_k = \frac{a_{k-1} + b_{k-1}}{2} \quad (\text{Aritmética}), \\"
            r"b_k = \sqrt{a_{k-1} b_{k-1}} \quad (\text{Geométrica}), \\"
            r"c_k = a_k^2 - b_k^2, \quad s_k = s_{k-1} - 2^k c_k, \\"
            r"p_k = \frac{2 a_k^2}{s_k}",
            font_size=24
        ).next_to(text3, DOWN, buff=0.5)

        formula_sb1 = MathTex("p_k \\text{ converge cuadráticamente a } \\pi",
            arg_separator="\n",
            font_size=24
        ).next_to(formula_sb, DOWN, buff=0.5) 

        self.play(Write(text3), run_time=6)
        self.play( Write(formula_sb),Write(formula_sb1), run_time=2)
        self.wait(2)
        self.play(FadeOut(text3), FadeOut(formula_sb),FadeOut(formula_sb1))

        # Escena 4: Bellard y BBP
        text4 = Text("Se desarrollaron métodos para calcular dígitos\nespecíficos de Pi, como el Algoritmo de Bellard en 1997\ny las contribuciones de Colin Percival entre 1998 y 2000,\nutilizando la Fórmula BBP (Bailey–Borwein–Plouffe).",
                     font_size=24,
                     color=WHITE).shift(UP*1.5)
        formula_bellard = MathTex(
            "\\pi = \\frac{1}{2^6} \\sum_{n=0}^{\\infty} \\frac{(-1)^n}{2^{10n}} \\left( \\frac{2^5}{4n+1} - \\frac{1}{4n+3} + \\frac{2^8}{10n+1} - \\frac{2^6}{10n+3} - \\frac{2^2}{10n+5} - \\frac{2^2}{10n+7} + \\frac{1}{10n+9} \\right)",
            font_size=24
        ).next_to(text4, DOWN, buff=0.5)

        self.play(Write(text4), Write(formula_bellard), run_time=13)
        self.wait(2)
        self.play(FadeOut(text4), FadeOut(formula_bellard))

        # Escena 5: Avances en el tercer milenio
        text5 = Text("En el tercer milenio, se lograron avances adicionales,\ncomo las identidades tipo Ramanujan para Pi por\nJesús Guillera y las fórmulas BBP para Pi cuadrado \nde David Broadhurst.",
                     font_size=24,
                     color=WHITE).shift(UP*1.5)
        formula_millennium = MathTex(
            r"\frac{4}{\pi^2} &= \sum_{n=0}^{\infty} (-1)^n r(n) \frac{5(13 + 180n + 820n^2)}{32 \cdot 2^{n+1}} \\",
            r"\frac{2}{\pi^2} &= \sum_{n=0}^{\infty} (-1)^n r(n) \frac{5(1 + 8n + 20n^2)}{2 \cdot 2^{n+1}}",
            arg_separator="\n",
            font_size=24
        ).next_to(text5, DOWN, buff=0.5)
        formula_millennium2 = MathTex("\\text{Donde }r(n) \\text{ se define como:}",
            "r(n) := \\frac{\\displaystyle\\prod_{i=1}^{n} \\left(\\frac{2i-1}{2i}\\right)}{n!}",
            arg_separator="\n",
            font_size=24
        ).next_to(formula_millennium, DOWN, buff=0.5)

        self.play(Write(text5), Write(formula_millennium),Write(formula_millennium2), run_time=10)
        self.wait(2)
        self.play(FadeOut(text5), FadeOut(formula_millennium),FadeOut(formula_millennium2))

        # Escena 6: Computadoras modernas
        text6 = Text("Hoy en día, las computadoras modernas han llevado\nel cálculo de Pi a niveles de precisión y velocidad\nantes inimaginables, reflejando el continuo progreso\nde la informática y su impacto en las matemáticas.",
                     font_size=24,
                     color=WHITE).shift(UP*2)
        
        server = ImageMobject("C:\\Users\\yotai\\Documents\\Algebra\\life_of_pi\\media\\images\\main\\server.jpg").scale(0.5).next_to(text6,DOWN)
        
        self.play(Write(text6),FadeIn(server), run_time=10)
        self.wait(2)