#follows a str technique -> para -> sentences -> words(hierarchy of structuring)
#recursive text splitting

#para -> /n/n   line change ->\n    spaces->_(words)  char->""

#chunk_size = 10
#first we see for /n/n para then divide it into paras and if still greater 
# than chunk size then divide more , now divide on \n basis then divide into sentenses 
#still greater than aloowed limit, now on space basis word wise "_" 
#now it tries to join if less than limit till chunk size(merging again)
#count spaces also in between words 

from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.document_loaders import PyPDFLoader


text = """The  global  mortgage  market  is  a  major  component  of  the  financial  system,  with 
 the  United  States  alone  having  more  than  USD  12  trillion  in  outstanding  mortgage  debt 
 by  2023.  [1].  MBS  are  financial  instruments  that  convert  individual  mortgage  loans  into 
 tradeable   fixed-income   securities,   facilitating   efficient   capital   flow   between   mortgage 
 originators, institutional investors, and secondary market participants. 
 By   systematically   underestimating   the   risk   of   borrower   delinquency   in   MBS 
 pools,  this  pattern  was  demonstrated  with  devastating  accuracy  during  the  2008  financial 
 crisis.   The   structured   credit  market  experienced  mispricing  due  to  the  belief  that  MBS 
 products   were   priced   based   on   optimistic   assumptions   about   default   correlations   and 
 borrower behavior. 
 During   the   post-crisis   decade,   P2P   lending   platforms   emerged   as   a   significant 
 aspect   of   consumer   credit   markets.   This   occurred   concurrently.   Rather   than   using 
 intermediaries,  these  platforms  facilitate  direct  transactions  between  individual  investors 
 and borrowers. 
 This  seminar  aims  to  solve  these  problems  through  designing  and  developing  an 
 end-to-end  machine  learning  pipeline  for  the  classification  of  MBS  delinquency  risk.  The 
 Fannie   Mae   Single-Family   Loan   Performance   data   will   be   used   in   implementing   the 
 machine   learning   pipeline   with   Logistic   Regression   being   the   chosen   classification 
 algorithm.  Systematic  feature  engineering  will  be  performed"""

splitter = CharacterTextSplitter(
    chunk_size = 200,
    chunk_overlap = 0,
)

chunks = splitter.split_text(text)

print(len(chunks))
print(chunks)
