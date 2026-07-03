#if theres a piece of code not in plane text soo we need to organise by using certain keywords 
#like class , functions, loops -> keywords 
#same like plain text but diff is separators like :
#\nclass , \ndef,  \ntdef after this we do normal \n\n, \n, _ ,""
# same thing applied to markdown -> heading
#  using diff chunk_size to get perfect part of splitting

from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

text = """
import random
import statistics
import json
from datetime import datetime

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.marks = []

    def add_mark(self, mark):
        self.marks.append(mark)

    def average(self):
        if not self.marks:
            return 0
        return round(sum(self.marks) / len(self.marks), 2)

    def highest(self):
        return max(self.marks) if self.marks else 0

    def lowest(self):
        return min(self.marks) if self.marks else 0

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "marks": self.marks
        }
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,   #for lot of langs -> python, markdown
    chunk_size = 300,
    chunk_overlap = 0
)

chunks = splitter.split_text(text)

print(len(chunks))
print(chunks[1])