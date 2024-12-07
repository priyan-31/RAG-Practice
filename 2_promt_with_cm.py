from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

model = ChatOpenAI(api_key="")

template = "Tell me a fact about {}."
prompt_template = ChatPromptTemplate.from_template(template)
prompt = prompt_template.invoke(template)
result = model.invoke(prompt)
print(result.content)



# part 2

messages = [
    ("system", "Explain about {topic}"),
    HumanMessage(content="In about {no_of_words} words.")
]

prompt_template_2 = ChatPromptTemplate.from_messages(messages)
prompt2 = prompt_template_2.invoke({"topic": "langchain", "no_of_words": "250"})
result2 = model.invoke(prompt2)
print(result2.content)