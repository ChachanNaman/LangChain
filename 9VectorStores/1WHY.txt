sugeesting movies from one movie at the same page of the movie reco sys website 
keyword matching : m1 and m2 , compare of diff parameters -> actor  , director , genre -> matching and we cn reccomend 
But the flaw is -> movie can be having same keywords but the movie cant be similar 
                -> and sometime all diff keywords but movies can be same 

Rather than matching keywords we need to match plot of the movies 
Get the whole para of plot of all movies 
Compare and generate the similarity score 

Embedding is a technique of converting piece of text and by sending text to neural network and then represent in number form or vector form 
Using embedding to transform text to numbers 
Now easy to clac similarity bw numbers 

plot all the embedding in 512 dimension vector graphql
and calc dist bw two vectors to get the similarity bw 2 movies 

Challenges : 
1. generate embedding vectors
2. storage (cant store in oracle , mysql) -> need diff type of place to store
3. semantic search (serahc which vector most similar using cosing similarity)
    what if 10 lakh records soo cant compare all with one -> need intelligent semantic search 

ALL CHALLENGES SOLVED BY -> VECTOR STORE 

