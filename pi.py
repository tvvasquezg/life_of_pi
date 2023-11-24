from manim import *


class PiTimeline(Scene):
    def construct(self):
        # Crear la línea de tiempo
        timeline = NumberLine(
            x_range=[-3500, 2014, 500],  # Ajustar según el número de eventos
            length=10,
            color=BLUE,
            include_numbers=True,
            label_direction=UP,
            font_size=20
        )
        self.play(Create(timeline))
        self.wait(1)

        # Eventos en la línea de tiempo
        events = [
            {"year": -3000, "text": "Babilonios y Egipcios", "value": "3.125 - 3.1604"},
            {"year": -250, "text": "Arquímedes", "value": "3.14"},
            {"year": 500, "text": "Tsu Chung-Chih", "value": "3.141592"},
            {"year": 1400, "text": "Al-Kāshī", "value": "3.1415926535"},
            {"year": 2000, "text": "Era Digital", "value": "Billones de dígitos"},
        ]

        # Crear y animar cada evento
        for i,event in enumerate(events):
            dot = Dot(color=RED).move_to(timeline.n2p(event["year"]))
            text = Text(event["text"], font_size=15).next_to(dot, UP*(i+2))
            value = Text(event["value"], font_size=15).next_to(dot, DOWN*(i+2))
            self.play(FadeIn(dot), Write(text), Write(value))
            self.wait(1)

        self.play(FadeOut(timeline), *[FadeOut(mob) for mob in self.mobjects])

class PiConOjos(VGroup):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        # Crear el símbolo de Pi
        pi_symbol = MathTex("\\pi").set_color("#66ccff").scale(6.5)

               # Crear los ojos
        # Esclerótica (parte blanca)
        esclerotica_izquierda = Circle(radius=0.17, color=WHITE, fill_opacity=1).move_to(pi_symbol.get_center() + UP*0.9 + LEFT*0.3)
        esclerotica_derecha = Circle(radius=0.17, color=WHITE, fill_opacity=1).move_to(pi_symbol.get_center() + UP*0.9 + RIGHT*0.3)

        # Pupilas (parte negra)
        pupila_izquierda = Dot(color=GREEN).scale(1).move_to(esclerotica_izquierda.get_center()+UP*0.09+RIGHT*0.08)
        pupila_derecha = Dot(color=BLACK).scale(1).move_to(esclerotica_derecha.get_center()+UP*0.09+RIGHT*0.08)

        # Crear cejas
        ceja_izquierda = Arc(start_angle=4*PI/4, angle=-PI/2, radius=0.2).next_to(esclerotica_izquierda, UP, buff=0.1)
        ceja_derecha = Arc(start_angle=-3*PI/4, angle=PI/2, radius=0.2).next_to(esclerotica_derecha, UP, buff=0.1)

        boca = Arc(start_angle=PI, angle=PI, radius=0.03).move_to(pi_symbol.get_center() + UP*0.5)

        # Agrupar todo
        #pi_con_ojos = VGroup(pi_symbol, esclerotica_izquierda, esclerotica_derecha, pupila_izquierda, pupila_derecha, ceja_izquierda, ceja_derecha, boca)
        self.add(pi_symbol, esclerotica_izquierda, esclerotica_derecha, pupila_izquierda, pupila_derecha, ceja_izquierda, ceja_derecha, boca)

from manim import *

class PiEvolution(Scene):
    def get_polygon_inscribed_in_circle(self, circle, num_sides):
            radius = circle.radius - 0.1  # Ajusta el radio según sea necesario

            polygon = RegularPolygon(n=num_sides, radius=radius, color=BLUE)
            polygon.move_to(circle.get_center())

            angle = 360 / num_sides
            label = MathTex(f"{angle}^\\circ").next_to(circle.get_center(), UP).scale(0.5)

            return polygon, label

    def get_polygon_circumscribed_about_circle(self, circle, num_sides):
        radius = circle.radius + 0.1  # Ajusta el radio según sea necesario

        polygon = RegularPolygon(n=num_sides, radius=radius, color=RED)
        polygon.move_to(circle.get_center())

        angle = 360 / num_sides
        label = MathTex(f"{angle}^\\circ").next_to(circle.get_center(), UP).scale(0.5)

        return polygon, label
    
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

        # Escena 1: Animación de un círculo
        circle = Circle(radius=2, color=BLUE).shift(LEFT * 3)
        text2 = Tex(r"\(\pi\) es conocido por todos como la relación entre la circunferencia de un círculo y su diámetro").scale(0.4).next_to(circle, DOWN, buff=0.5)
        diameter = Line(start=circle.get_left(), end=circle.get_right(), color=RED)
        formula = MathTex("\\pi = \\frac{C}{d}").next_to(circle, RIGHT, buff=2)

        self.play(Create(circle), Write(text2), run_time=3)
        self.play(Create(diameter), Write(formula), run_time=3)
        self.wait(1)

        # Escena 2: Breve mención de su uso
        text3 = Tex("Desde la construcción de las pirámides hasta los modernos cálculos de ingeniería y ciencia, $\\pi$ juega un papel crucial").scale(0.6).to_edge(DOWN)
        pyramid = ImageMobject("C:\\Users\\yotai\\Documents\\Algebra\\life_of_pi\\media\\images\\manin\\keops.jpg").next_to(circle, RIGHT, buff=2)
        
        self.play(Write(text3), FadeOut(text2),run_time=2)
        self.play(FadeIn(pyramid), run_time=2)
        self.wait(1)

        # Transición a la siguiente escena
        self.play(FadeOut(circle), FadeOut(diameter), FadeOut(formula), FadeOut(text3), FadeOut(pyramid))

        # Aquí puedes continuar con las siguientes escenas

        #historia
        text5 = Tex("Acompananos para descubrir cómo $\\pi$ ha sido calculado, estudiado y celebrado a lo largo de los siglos")

        intro_text = Text("Historia de $\\pi$", font_size=36)
        self.play(Write(text5))
        self.wait(2)
        self.play(FadeOut(text5))

        # Crear la línea de tiempo
        timeline = NumberLine(
            x_range=[-3500, 2014, 500],  # Ajustar según el número de eventos
            length=10,
            color=BLUE,
            include_numbers=True,
            label_direction=UP,
            font_size=20
        )
        self.play(Create(timeline))
        self.wait(1)

        # Eventos en la línea de tiempo
        events = [
            {"year": -3000, "text": "Babilonios y Egipcios", "value": "3.125 - 3.1604"},
            {"year": -250, "text": "Arquímedes", "value": "3.14"},
            {"year": 500, "text": "Tsu Chung-Chih", "value": "3.141592"},
            {"year": 1400, "text": "Al-Kāshī", "value": "3.1415926535"},
            {"year": 2000, "text": "Era Digital", "value": "Billones de dígitos"},
        ]

        # Crear y animar cada evento

        circle = Circle(radius=2, color=WHITE)
        self.play(Create(circle))

        num_iterations = 6

        for sides in range(4, num_iterations + 4):
            inscribed_polygon, inscribed_label = self.get_polygon_inscribed_in_circle(circle, sides)
            circumscribed_polygon, circumscribed_label = self.get_polygon_circumscribed_about_circle(circle, sides)

            self.play(Create(inscribed_polygon), Write(inscribed_label))
            self.wait(0.5)
            self.play(FadeOut(inscribed_polygon), FadeOut(inscribed_label))
            self.play(Create(circumscribed_polygon), Write(circumscribed_label))
            self.wait(0.5)
            self.play(FadeOut(circumscribed_polygon), FadeOut(circumscribed_label))

        self.wait(1)

        for i,event in enumerate(events):
                dot = Dot(color=RED).move_to(timeline.n2p(event["year"]))
                text = Text(event["text"], font_size=15).next_to(dot, UP*(i+2))
                value = Text(event["value"], font_size=15).next_to(dot, DOWN*(i+2))
                self.play(FadeIn(dot), Write(text), Write(value),)
                self.wait(1)

        self.play(FadeOut(timeline), *[FadeOut(mob) for mob in self.mobjects])





        # Añadir a la escena
       # self.add(personaje_pi)



       




        
       
        
       

class IntroPi(Scene):
    def construct(self):
        # Escena 1: Animación de un círculo
        circle = Circle(radius=2, color=BLUE)  # Crear un círculo azul
        self.play(Create(circle))  # Animación para dibujar el círculo
        self.wait(1)

        # Escena 2: Muestra un círculo y su diámetro
        diameter = Line(start=circle.get_left(), end=circle.get_right(), color=RED)  # Crear línea del diámetro
        self.play(Create(diameter))  # Animación para dibujar el diámetro
        self.wait(1)

        # Escena 3: Visualización de la fórmula π = C/d
        formula = MathTex(r"\pi = \frac{C}{d}")  # Crear la fórmula matemática
        self.play(Write(formula))  # Animación para escribir la fórmula
        self.wait(2)

        # Escena 4: Breve mención de su uso (puedes agregar imágenes o íconos aquí)
        # Por ejemplo, una imagen de una pirámide (asegúrate de tener la imagen en tu directorio)
        pyramid = ImageMobject("C:\\Users\\yotai\\Documents\\Algebra\\media\\images\\manin\\keops.jpg")
        self.play(FadeIn(pyramid))
        self.wait(1)

        # Escena 5: Transición a la historia de π
        self.play(FadeOut(circle), FadeOut(diameter), FadeOut(formula))  # Desvanecer todo para la transición
        self.wait(1)