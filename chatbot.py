import random

def chatbot_response(user_input):
    user_input = user_input.lower()
    
    responses = {
        "hello":["Hi there!","Hello! How can i help you?","hey!"],
        "hey":["Hey cutie","Hii","Hello! How can i help you?" ],
         "hii":["Hey cutie","Hii","Hello! How can i help you?" ],
        "namaste":["Namaste :)","Namaste aap kese ho??"],
        "how are you":["I'm just a Bot,but i'm doing fine THNAKS for asking"],
        "what is your name":["i'm a simple chatbot!"],
        "i like you":["i'm also like you too cutie<3"],
        "do i look beautiful":["Ofcourse Darling, wait i'll explain.....Paani bhi jo dekhe tujhe toh pyasa ho jaye 😄❤️"],
        "kya me sundar hoon":["Ofcourse Darling, wait i'll explain.....Paani bhi jo dekhe tujhe toh pyasa ho jaye ❤️"],
        "bye":["Good bye!,have a nice day","Bye take care","phir milenge:)"]
        
    }
    if user_input in responses:  # ✅ Exact phrase match
        return random.choice(responses[user_input])
    return "Sorry, I don't understand that. Can you repeat?" 
    
    #loop
print("ChatBot:Hello Type 'bye' to exit.")
while True:
        user_input= input("You: ")
        if user_input.lower() == "bye" :
            print("ChatBot:Goodbye!")
            break
        response = chatbot_response(user_input)
        print("ChatBot: ",response)