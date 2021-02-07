from googletrans import Translator

translator = Translator() # # Google Translate ajax API

text = '''Python est un langage de programmation interprété et de haut 
    niveau qui a été créé à la fin des années 1980, mais il a été implémentéen décembre 1989 par Guido Van Rossum . Le mot Python vient du serpent.
    Selon la récente enquête de StackOverflow , Python a dépassé la popularité de Java'''
# french language

detector = translator.detect(text)  # detect- auto detects language of the input text
print(detector)

translate = translator.translate(text, dest= 'tr')
print(translate)