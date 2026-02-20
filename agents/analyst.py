from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from typing import List, Dict

class AnalystAgent:
    """Evaluates and ranks housing resources"""
    
    def __init__(self):
        self.llm = Ollama(
            model="llama3.2",
            temperature=0
        )
        
        self.prompt = PromptTemplate(
            template="""You are an Analyst Agent. Evaluate and rank housing resources based on how well they match user needs.

For each resource, provide a brief ranking reason.
Be concise and focus on the most relevant aspects.

User Request: {user_request}

Resources to evaluate:
{resources}

Rank these by relevance and explain briefly why:""",
            input_variables=["user_request", "resources"]
        )
    
    def analyze(self, user_request: str, resources: List[Dict]) -> List[Dict]:
        """Analyze and rank resources"""
        
        # Format resources for LLM
        resources_text = "\n\n".join([
            f"Resource {i+1}:\n" + 
            f"Name: {r['name']}\n" +
            f"Type: {r['resource_type']}\n" +
            f"Services: {r['services']}\n" +
            f"Location: {r['zip_code']}"
            for i, r in enumerate(resources)
        ])
        
        # Get analysis
        chain = self.prompt | self.llm
        response = chain.invoke({
            "user_request": user_request,
            "resources": resources_text
        })
        
        print(f"\n ANALYST AGENT EVALUATION:")
        print(response)
        
        # Add analysis to resources
        for i, resource in enumerate(resources):
            resource['rank'] = i + 1
        
        return resources[:5]  # Top 5

