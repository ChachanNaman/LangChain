why use PRromptTemplate over f string in python ?
-> gives validation error
-> reusable code : template.json can be used in any file 
-> langChain ecosystem


Langchain have three type of messages -> 
1.System messages
2.Human messages
3.AI messages
Coded in messages.py


Model can be invoked in 2 ways : 
1. Single Messages : Static Messages , Dynamic Messages(Prompt Template)
2. List of Messages(multi-turn convo) : Static Messages(system, human,AI messages), Dynamic Messages(ChatPromptTemplate)

Message Placeholder : 
in a langchain its a special Placeholder used inside a ChatPromptTemplate to dynamically insert chat history or a list of messages at runtime
ex : amazon refund -> 1 day user asked , and then after 3 days come back and ask again , to main this history message placeholder is used 