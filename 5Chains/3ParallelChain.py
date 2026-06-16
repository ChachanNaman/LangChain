from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel
load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template = 'Generate short and simple notes from following {text}',
    input_variables = ['text']
)
prompt2 = PromptTemplate(
    template = 'Give 5 question answers from following {text}',
    input_variables = ['text']
)
prompt3 = PromptTemplate(
    template = 'Merge the following notes and quiz into single document \n notes -> {notes} and quiz -> {quiz}',
    input_variables = ['notes' ,'quiz']
)

parallel_chain = RunnableParallel({
    'notes' : prompt1 | model | parser,
    'quiz' : prompt2 | model | parser
})

merge_chain = prompt3 | model | parser 

chain = parallel_chain | merge_chain

text = """
class sklearn.linear_model.LogisticRegression(penalty='deprecated', *, C=1.0, l1_ratio=0.0, dual=False, tol=0.0001, fit_intercept=True, intercept_scaling=1, class_weight=None, random_state=None, solver='lbfgs', max_iter=100, verbose=0, warm_start=False, n_jobs=None)[source]
Logistic Regression (aka logit, MaxEnt) classifier.

This class implements regularized logistic regression using a set of available solvers. Note that regularization is applied by default. It can handle both dense and sparse input X. Use C-ordered arrays or CSR matrices containing 64-bit floats for optimal performance; any other input format will be converted (and copied).

The solvers ‘lbfgs’, ‘newton-cg’, ‘newton-cholesky’ and ‘sag’ support only L2 regularization with primal formulation, or no regularization. The ‘liblinear’ solver supports both L1 and L2 regularization (but not both, i.e. elastic-net), with a dual formulation only for the L2 penalty. The Elastic-Net (combination of L1 and L2) regularization is only supported by the ‘saga’ solver.

For multiclass problems (whenever n_classes >= 3), all solvers except ‘liblinear’ optimize the (penalized) multinomial loss. ‘liblinear’ only handles binary classification but can be extended to handle multiclass by using OneVsRestClassifier.

Read more in the User Guide.

Parameters:
penalty{‘l1’, ‘l2’, ‘elasticnet’, None}, default=’l2’
Specify the norm of the penalty:

None: no penalty is added;

'l2': add an L2 penalty term and it is the default choice;

'l1': add an L1 penalty term;

'elasticnet': both L1 and L2 penalty terms are added.
"""
result = chain.invoke({'text' : text})

print(result)

chain.get_graph().print_ascii()