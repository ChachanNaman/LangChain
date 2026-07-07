Tools -> Tool Calling(tool +llm) -> Agents 

Tools : 
LLMs have reasoning capability and language generation capability
LLMs dont have  access live data , perform tasks , call apis, run code 

Tools is just a python function that is packaged in a way the LLM can understand and call when needed 
Ex : Function like IRCTC booking perform -> LLM can talk to this and ask to book the train then Function can book 

Tools can be -> Built-in tools, Custom tools 

Agent : 
its an LLM powered system that can 
think, decide and take actions using external tools or API 
Agent-> reasoning and decision making(llm) + action(tools)


BUILT-IN TOOLS : 
Tools that langchain provides for you - its pre built , production ready, and requires minimal setup
DuckDuckGoSearchRun -> web search via DuckDuckGo
WikipediaQueryRun -> wikipedia summary 
PythonREPLTool -> writes and run raw py code 
ShellTool -> run shell cmnds
GmailSendMessageTool -> send emails via gmail 
SlackSendMessageTool -> Post message to slack 
