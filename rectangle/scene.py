from manim import *

class First(Scene):
    def construct(self):
        # Definir los vértices del triángulo
        A = np.array([0, 3, 0])   
        B = np.array([0, -1, 0])   
        C = np.array([-3, -1, 0])   
        D = np.array([2, -1, 0])

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
        new_segment = Line(C, D)
        label_2 = MathTex('2').next_to((B +D) / 2, DOWN)
        self.play(Transform(hypotenuse, new_segment))
        self.play(Write(label_2))
        E = np.array([(2 + np.sqrt(20)), -1, 0])
        F = np.array([(2 + np.sqrt(20)), 3, 0])
        hipotenusa = Line(D, A)
        label_hipotenusa = MathTex(r'\sqrt{20}').next_to((D + A) / 2, RIGHT + UP)
        label_lado_grande = MathTex(r'\sqrt{20}+2').next_to((B + E) / 2, DOWN)
        label_techo = MathTex(r'\sqrt{20}+2').next_to((A + F) / 2, UP)
        label_lado_chico = MathTex('4').next_to((E + F) / 2, RIGHT )
        hipotenusa_piso = Line(D, E)
        lado_chico = Line(E, F)
        self.play(Create(hipotenusa))
        self.play(Write(label_hipotenusa))
        self.play(Transform(hipotenusa, hipotenusa_piso), Unwrite(label_2), Write(label_lado_grande))
        self.play(Create(lado_chico), Write(label_lado_chico))
        rectangulo = Polygon(E, F, A, B, color='ORANGE' )
        self.play(Create(rectangulo), Write(label_techo), Unwrite(AB_label, BC_label, CA_label ), FadeOut(triangle, new_segment))