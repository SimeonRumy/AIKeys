from api.TextGenerator import TextGenerator

class TextBank: 

    models = {
       "python": [],
       "swift": [], 
    }

    def __init__ (self):
        self.text_generator = TextGenerator()
        for i in range(10):
            print(f"Iteration {1}")
            for key in self.models.keys(): 
                self.models[key].append(self.text_generator.generate_more_text(key))

    def get_text(self, lang):
        print(lang)
        if len(models[lang]) > 0:
            return self.models[lang].pop()
        else:
            return self.text_generator.generate_more_text(lang)
    
    def generate_more_text(self):
        for key in self.models.keys(): 
            self.models[key].append(self.text_generator.generate_more_text(key))
