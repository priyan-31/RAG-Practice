from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage

model = ChatOpenAI(api_key="")

prompt_template = ChatPromptTemplate.from_messages(
    [
        SystemMessage("Explain about {topic}."),
        HumanMessage("Not more than {no_of_words}.")
    ]
)

uppercase_output = RunnableLambda(lambda x: x.upper())
count = RunnableLambda(lambda x: f"Word count: {len(x.split())}\n {x}")

chain = prompt_template | model | StrOutputParser() | uppercase_output | count

result = chain.invoke({"topic": "langchain", "no_of_words": "500"})
print(result)