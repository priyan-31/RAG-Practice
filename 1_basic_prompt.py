from langchain.schema import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

template = "Tell me a fact about the city {context}."
prompt_template = ChatPromptTemplate.from_template(template)

prompt = prompt_template.invoke({"context": "Chennai"})
print(prompt)


#Part 2

template2 = "Tell me some advantages of {context_1} over {context_2}."
prompt_template_2 = ChatPromptTemplate.from_template(template2)

prompt2 = prompt_template_2.invoke({"context_1": "python", "context_2": "java"})
print(prompt2)


# Part 3

messages = [
    ("system", "Explain about {topic}."),
    ("human", "With maximun of {no_of_words} words.")
]
prompt_template_3 = ChatPromptTemplate.from_messages(messages)
promt3 = prompt_template_3.invoke({"topic": "RAG", "no_of_words": "100"})
print(promt3)


# alter part 3

messages = [
    ("system", "Explain about {topic}."),
    HumanMessage(content="In about 100 words.") # this works but - humanmessage(content ="human", "With maximun of {no_of_words} words.") this doesnt work, we can interpoalte in humanmessage.
]
prompt_template_3 = ChatPromptTemplate.from_messages(messages)
promt3 = prompt_template_3.invoke({"topic": "RAG", "no_of_words": "100"})
print(promt3)




#  prompt = PromptTemplate(                                                                # defines prompt to extract details of prod.
  #  template="Extract the information specified.\n{format_instructions}\n{context}",    # here we give only the context as input
 #   input_variables=["context"],
#    partial_variables={"format_instructions": parser.get_format_instructions()}