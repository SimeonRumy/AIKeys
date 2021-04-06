from api.TextGenerator import TextGenerator

language = "python"

class TextBank: 

    models = {
       "python": ["Start typing......"],
       "swift": ["Start typing....."], 
    }

    def __init__ (self):
        self.text_generator = TextGenerator()

    def get_text(self, lang):
        print(lang)
        if len(self.models[lang]) > 10:
            return self.models[lang].pop() + self.models[lang].pop()
        elif len(self.models[lang]) > 0:
            return self.models[lang].pop()
        else:
            return self.text_generator.generate_more_text(lang)
    
    def generate_more(self, lang=language):
        language = lang
        self.models[lang].append(self.text_generator.generate_more_text(language, n_chars=50))

    def generate_more_for_all(self):
        for key in self.models.keys():
            self.models[key].append(self.text_generator.generate_more_text(key, n_chars=250))
