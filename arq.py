from manim import *

class ArchimedeanSpiral(Scene):
    def construct(self):
        circle = Circle(radius=2, color=WHITE)
        self.play(Create(circle))

        num_iterations = 6

        for sides in range(4, num_iterations + 4):
            inscribed_polygon, inscribed_label = self.get_polygon_inscribed_in_circle(circle, sides)
            circumscribed_polygon, circumscribed_label = self.get_polygon_circumscribed_about_circle(circle, sides)

            self.play(Create(inscribed_polygon), Write(inscribed_label), run_time=0.25)
            self.play(FadeOut(inscribed_polygon), FadeOut(inscribed_label), run_time=0.25)
            self.play(Create(circumscribed_polygon), Write(circumscribed_label), run_time=0.25)
            self.play(FadeOut(circumscribed_polygon), FadeOut(circumscribed_label), run_time=0.25)

        self.wait(1)

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
