from manim import *

# Asegúrate de que 'config' se importa correctamente si es necesario ajustar la configuración global

class MiEscena(Scene):
    def construct(self):
        title = MathTex("\\text{The Life of } \\pi \\text{ (2014)} ").scale(1.5)
        pi_symbol = MathTex("\\pi").next_to(title, DOWN).scale(4)
        autors = Tex("Daniel Rodriguez - Tania Vasquez")

        self.play(Write(title), run_time=2)
        self.play(Write(pi_symbol), FadeOut(title), run_time=2)
        self.play(Write(autors),FadeOut(pi_symbol))
        self.wait(2)
        self.play(FadeOut(pi_symbol))
        self.play(FadeOut(autors))


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

        # Añadir a la escena
        #self.add(pi_con_ojos)

        # Animación: mover las pupilas
        # for _ in range(2):
        #     self.play(pupila_izquierda.animate.shift(RIGHT*0.07), pupila_derecha.animate.shift(RIGHT*0.07), run_time=0.5)
        #     self.play(pupila_izquierda.animate.shift(LEFT*0.1), pupila_derecha.animate.shift(LEFT*0.1), run_time=0.5)

        # self.wait(2)
class PiEvolution(Scene):
    def construct(self):
        title = MathTex("\\text{The Life of } \\pi \\text{ (2014)} ").scale(1.5)
        pi_symbol1 = MathTex("\\pi").next_to(title, DOWN).scale(4)
        autors = Tex("Daniel Rodriguez - Tania Vasquez")
        pi_symbol = MathTex(r"\pi").set_color("#66ccff").scale(6.5)
        text1 = Tex("""Abordaremos la evolución de \( \pi \) a lo largo de las eras, desde Arquímedes
                    hasta la era de la computación.""").scale(0.8).to_edge(UP)
        text2 = Tex("""Destacaremos la prueba de la irracionalidad de \( \pi \) 
                    de Ivan Niven en 1947, fórmulas y algoritmos para su cálculo, como el BBP, y curiosidades, 
                    como el calculo de la una antigua aproximacion de \( \pi \) a travez de integrales definidas """).scale(0.8).next_to(text1, DOWN, buff=0.5)
        formula0 = MathTex("\\int_{0}^{t} \\frac{(1-x)^4x^4}{1+x^2} \\,dx = t^7\\left(\\frac{t^7}{7} - \\frac{2t^6}{3} + {t^5} - \\frac{4t^3}{3} + 4t - 4\\arctan{t}\\right)")
        formula1 = MathTex("\int_0^1 \\frac{ (1 - x)^4x^4 }{1 + x^2} dx = \\frac{22}{7} \\approx \pi ").scale(1).to_edge(UP)

        personaje_pi = PiConOjos()

        # Añadir a la escena
       # self.add(personaje_pi)

        # Ahora puedes animar personaje_pi como desees

        self.play(Write(title), run_time=2)
        self.play(Write(pi_symbol1), FadeOut(title), run_time=2)
        self.play(Write(autors),FadeOut(pi_symbol1))
        self.wait(2)
        self.play(FadeOut(pi_symbol))
        self.play(FadeOut(autors))
        self.play(pi_symbol.animate.scale(2).move_to(UP * 2), run_time=4)
        self.play(Write(text1), FadeOut(pi_symbol), run_time=5)
        self.play(Write(text2), FadeOut(text1), run_time=8)
        self.play(Write(formula0), FadeOut(text2), run_time=5)
        self.play(Write(formula1), FadeOut(formula0), run_time=3)
        self.play(personaje_pi.animate.shift(RIGHT*2))

        self.wait(2)

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



# No necesitas instanciar las escenas ni llamar a 'render()' manualmente
