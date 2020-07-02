from translate import Translator

translator = Translator(to_lang="portuguese")
translation = translator.translate("Hello")
print(translation)

translator = Translator(from_lang="portuguese", to_lang="english")
translation = translator.translate("Olá")
print(translation)
