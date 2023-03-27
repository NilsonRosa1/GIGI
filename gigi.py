#@title Logic Calculator

class Calculation():
    def __init__(self, ler):
        self.mensagem = ler

    def fune(self):  
        x = self.mensagem
        i = 'V'
        j = 'F'
        for a in range(len(x)):
            if i in x[0]:
                if j not in x:
                    return ' seu  valor logico é V'
                else:
                    return 'seu  valor logico é F'
            else:
                return ' seu  valor logico é F'

    def funou(self):  
        x = self.mensagem
        i = 'V'
        j = 'F'
        for a in range(len(x)):
            if j in x[0]:
                if i not in x:
                    return ' seu  valor logico é F'
                else:
                    return ' seu  valor logico é V'
            else:
                return ' seu  valor logico é V'

    def funcond(self):  
        x = self.mensagem
        i = 'V'
        j = 'F'
        for a in range(len(x)):
            if i in x[0]:
                if j in x:
                    return ' seu  valor logico é F '
                else:
                    return ' seu  valor logico é V'
            else:
                return ' seu  valor logico é V'

    def funbic(self):  
        x = self.mensagem
        i = 'V'
        j = 'F'
        for a in range(len(x)):
            if j in x[0]:
                if i not in x:
                    return ' seu  valor logico é V'
                else:
                    return ' seu  valor logico é F'
            if i in x[0]:
                if j not in x:
                    return ' seu  valor logico é V'
                else:
                    return 'seu  valor logico é F'

    def inicial(self):
      while True:
        p = "E"
        x = self.mensagem.upper()
        if p in x:

          return self.fune()
        p = "OU"
        if p in x:

          return self.funou()
        p = "=>"
        if p in x:

          return self.funcond()
        p = "<>"
        if p in x:

          return self.funbic()
        
        
        
        #@title NoSQL Base

class Mongodb():
    def __init__(self):
        client = MongoClient("")
        db = client["fate"]
        self.collection = db["telegram_messages"]

    def save(self, message):
        document = {"chat_id": message.chat.id, "text": message.text}
        self.collection.insert_one(document)

        
        
        #@title Menu Gigi

import openai


db= Mongodb()

APIII = senha

gigi = telebot.TeleBot(APIII)





def fun(mensagem):
    if mensagem == "GIGI":
      return True
    else: 
         False
  
openai.api_key = "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"


def generate_response(message):
    prompt = message.text
    model = "text-davinci-002" # modelo da OpenAI para o idioma português
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text

@gigi.message_handler(func=lambda message: True)
def echo_all(message):
    response = generate_response(message)
    db.save(message)
    gigi.reply_to(message, response)
       

@gigi.message_handler(func=fun)
def ler(mensagem):
    ler = mensagem.text
    calculation = Calculation(ler)
    db.save(mensagem)
    gigi.reply_to(mensagem,calculation.inicial())

gigi.polling()
        
   
