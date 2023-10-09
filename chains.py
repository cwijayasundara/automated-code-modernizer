from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

# llm = ChatOpenAI(
#     model_name='gpt-3.5-turbo-16k',
#     streaming=True,
#     callbacks=[StreamingStdOutCallbackHandler()],
#     temperature=0
# )

# GPT-4 gives a much better result than gpt-3.5-turbo-16k but costly

llm = ChatOpenAI(
    model_name='gpt-4',
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()],
    temperature=0
)

prompt = """

System:

Title: Business Logic Extraction and Diagrammatic Documentation

Objective: As a proficient Software Architect in {programming_language}, your task entails dissecting and 
articulating the business logic housed within the provided class file. Utilize a Mermaid Flowchart diagram for visual 
elucidation, accompanied by a succinct textual explanation. Your documentation, not exceeding 400 words, 
should be presented in a bullet-point format, providing a crisp yet insightful exposition of the code's functionality.

1. Mermaid Flowchart Diagram:
   - (Insert Mermaid Flowchart Diagram here)

2. Textual Explanation:
   - (Point-by-point textual elucidation here)


Programming Language: {programming_language}

Class File: {input}

Business Logic Documentation:
1. Mermaid Flowchart Diagram:
(Insert Mermaid Flowchart Diagram here)

2. Textual Explanation:

"""

business_logic_chain = LLMChain.from_string(
    llm=llm,
    template=prompt
)

prompt = """

System:

Title: Code Design Extraction and Diagrammatic Representation

Objective: As a Software Architect, you are assigned to extract the design encapsulated within the provided code. 
Your task is to create a Mermaid class diagram and a sequence diagram to represent the code's design accurately. 
Additionally, provide a succinct yet comprehensive explanation of the design illustrated by these diagrams.

Programming Language: {programming_language}

Class File: {input}

Design Diagrams:
1. Mermaid Class Diagram:
(Insert Mermaid Class Diagram here)

2. Sequence Diagram:
(Insert Sequence Diagram here)

Design Explanation:

"""

tech_design_chain = LLMChain.from_string(
    llm=llm,
    template=prompt
)

prompt = """

System:

Title: Code Refactoring and Modernization

Objective: Please refactor the provided code to conform to modern standards specific to {programming_language}, 
ensuring it's structured as efficient, accurate, and RESTful microservices in the most idiomatic manner suitable for 
the designated programming language.

Programming Language: {programming_language}

Software Description: {input}

Render the output in Markdown format.

Refactored Code:

"""
refactor_chain = LLMChain.from_string(
    llm=llm,
    template=prompt
)

prompt = """

System:

Title: Code Enhancement and Refactoring

Objective: As a proficient software engineer with expertise in {programming_language}, you are tasked to refine and 
enhance the provided code. Your goal is to refactor the code adhering to SOLID principles, ensuring a clean, 
efficient, and optimized output.

Programming Language: {programming_language}

Software Description: {input}

Render the output in Markdown format.

Improved Code:

"""

code_improvement_chain = LLMChain.from_string(
    llm=llm,
    template=prompt
)

prompt = """

System:

Title: Unit and Integration Testing

Objective: As a proficient software engineer specialized in {programming_language}, you are assigned to develop unit 
and integration tests for the provided code to ensure its robustness and reliability.

Programming Language: {programming_language}

Software Description: {input}

Render the output in Markdown format.

Testing Code:
1. Unit Tests:
(Insert Unit Testing Code here)

2. Integration Tests:
(Insert Integration Testing Code here)

Unit Tested Code:

"""
unit_testing_chain = LLMChain.from_string(
    llm=llm,
    template=prompt
)


