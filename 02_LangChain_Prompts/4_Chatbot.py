from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model="llama-3.1-8b-instant"
)

chat_history = []
#as its chatbot , it will run infinitely until user ends itself. 

while True:
    user_input = input('You : ')
    chat_history.append(user_input)
    if user_input == 'exit' : 
        break
    result = model.invoke(chat_history)
    chat_history.append(result.content)
    print("AI : ",result.content)

print(chat_history)

