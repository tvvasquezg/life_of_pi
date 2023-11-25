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