from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
import os
import requests
from third_parties.TO_Link_Gist_Pull import scrape_TO_linkedin_gist

if __name__ == '__main__':
    load_dotenv()
    
    information_TO = scrape_TO_linkedin_gist('https://gist.githubusercontent.com/TJO1225/d7799663f922a813f79ee7293a04c491/raw/c448337d354d469a4f13810d07ebc6a8d1802a69/TO_Link.json')
    
    summary_template = """
     given the information {information} about a person I want you to create:
     1. A short summary
     2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(input_variables=['information'],template=summary_template)

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    res = chain.run(information=information_TO)

    print(res)