import L_Language
import Turtle
import Display

if __name__ == "__main__":

    seed = "F"
    axioms = {}
    axioms['F'] = "F[-F][+F]"
    l_language = L_Language.L_Language(seed, axioms)

    turtle = Turtle.Turtle( (200,350) )

    sentence =  l_language.loop_n_times(5)
    print(sentence)

    display = Display.display( (400,400) )

    display.draw_turtle(turtle, sentence)
    display.loop()