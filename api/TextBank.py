from api.TextGenerator import TextGenerator

language = "python"

class TextBank: 

    models = {
       "python": ["Start typing......"],
       "swift": ["Start typing......"], 
    }

    def __init__ (self):
        self.text_generator = TextGenerator()

    def get_text(self, lang):
        print(lang)
        if len(self.models[lang]) > 0:
            print("poping")
            return self.models[lang].pop()
        else:
            print("generating")
            return self.text_generator.generate_more_text(lang)
    
    def generate_more(self, lang=language):
        language = lang
        print("pre fetching text")
        self.models[lang].append(self.text_generator.generate_more_text(language))
