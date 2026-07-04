#2StrOutput_TypedDict.py

from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import TypedDict
##
load_dotenv()

model = ChatGroq(
    model="llama-3.1-8b-instant"
)

#Schema
class Review(TypedDict):

    summary : str
    sentiment : str

#ye model ke paas iss schema ka definition hai
structured_model = model.with_structured_output(Review)



result = structured_model.invoke("""
Extract the following from the review:

1. summary (short 1-2 lines)
2. sentiment (positive, negative, or neutral)

Return ONLY a JSON object with:
- summary
- sentiment

Do NOT include any extra text.

Review:
I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.""")

print(result)

