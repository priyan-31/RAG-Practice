from langchain.schema import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema.output_parser import StrOutputParser

model = ChatOpenAI(api_key="")
prompt_template = PromptTemplate.from_template(
    [
    SystemMessage(content="Explain in detail about {topic}."),
    HumanMessage(content="Not more than {no_of_words} words.")
]
)

chain = prompt_template | model | StrOutputParser()
result = chain.invoke({"topic": "flask framework", "no_of_words": "500"})
print(result)