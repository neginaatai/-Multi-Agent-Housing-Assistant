from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from typing import List, Dict

class AdvisorAgent:
    """Communicates recommendations to users"""
    
    def __init__(self):
        self.llm = Ollama(
            model="llama3.2",
            temperature=0.7
        )
        
        self.prompt = PromptTemplate(
            template="""You are an Advisor Agent. Communicate housing resource recommendations in a compassionate, clear, and actionable way.

Guidelines:
- Be warm and supportive
- Present information clearly with specific details
- Explain WHY each resource is recommended
- Provide actionable next steps
- Use emojis sparingly (🏠 📍 ☎️)
- Be concise but thorough

Format:
1. Brief empathetic acknowledgment
2. Top 3 recommendations with details
3. Next steps
4. Offer for additional help

User's Request: {user_request}

Top Recommended Resources:
{ranked_resources}

Your compassionate response:""",
            input_variables=["user_request", "ranked_resources"]
        )
    
    def advise(self, user_request: str, ranked_resources: List[Dict]) -> str:
        """Generate final advice for user"""
        
        # Format resources
        resources_text = ""
        for i, resource in enumerate(ranked_resources[:3], 1):
            resources_text += f"\nOption {i}:\n"
            resources_text += f"Name: {resource['name']}\n"
            resources_text += f"Address: {resource['address']}, Chicago, IL {resource['zip_code']}\n"
            resources_text += f"Phone: {resource['phone']}\n"
            resources_text += f"Type: {resource['resource_type']}\n"
            resources_text += f"Services: {resource['services']}\n"
        
        # Get advice
        chain = self.prompt | self.llm
        response = chain.invoke({
            "user_request": user_request,
            "ranked_resources": resources_text
        })
        
        print(f"\n💬 ADVISOR AGENT RESPONSE:")
        print(response)
        
        return response
