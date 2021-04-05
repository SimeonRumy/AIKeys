from api.TextGenerator import TextGenerator

class TextBank: 

    models = {
       "python": [],
       "swift": [], 
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
    
    def generate_more_text(self, lang):
        print("pre fetching text")
        self.models[key].append(self.text_generator.generate_more_text(lang))
