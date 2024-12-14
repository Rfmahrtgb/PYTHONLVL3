class TextAnalysis:
    qwestions = {'как тебя зовут' : "Я супер-крутой-бот и мое ппредназначение помогать тебе!",
             "сколько тебе лет" : "Это слишком философский вопрос"}
    memory = {} # Class-level dictionary to store data

    def __init__(self, text, username):
        if username not in TextAnalysis.memory:
            TextAnalysis.memory[username] = []
        self.text = text
        self.username = username
        #Example analysis (replace with your actual analysis)
        if self.text.lower() in qwestions.keys():
            self.response = 
        else:
            self.response = self.get_answer() 
        self.response = f"You said: {self.text}"
        self.translation = f"Translation of '{self.text}': (Translation not implemented)" # Placeholder
        TextAnalysis.memory[username].append(self) # Add the object to memory


