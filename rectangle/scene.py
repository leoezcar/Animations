from manim import *

class First(Scene):
    def construct(self):
        # Definir los vértices del triángulo
        A = np.array([0, 3, 0])   
        B = np.array([0, -1, 0])   
        C = np.array([-3, -1, 0])   
        
        # Crear el triángulo
        triangle = Polygon(A, B, C)
        
        # Crear las medidas como texto
        AB_label = MathTex("4").next_to((A + B) / 2, RIGHT)  
        BC_label = MathTex("3").next_to((B + C) / 2, DOWN)  
        CA_label = MathTex("5").next_to((C + A) / 2, LEFT + UP)  
        
        hypotenuse = Line(C, A)
        # Animar la creación del triángulo y las etiquetas
        self.play(Create(triangle))

        self.play(Write(AB_label), Write(BC_label), Write(CA_label))
        self.play(Create(hypotenuse))
        new_segment = Line(C, np.array([2, -1, 0]))
        self.play(Transform(hypotenuse, new_segment))  