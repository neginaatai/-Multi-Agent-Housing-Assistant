from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from typing import List, Dict

class ScoutAgent:
    """Searches and retrieves relevant housing resources"""
    
    def __init__(self):
        self.llm = Ollama(
            model="llama3.2",
            temperature=0
        )
        
        self.prompt = PromptTemplate(
            template="""You are a Scout Agent. Your job is to analyze user requests and identify relevant housing resources.

Extract key search criteria:
- Resource type (emergency, transitional, permanent)
- Location (zip code, neighborhood)
- Special needs (families, pets, disabilities, etc.)
- Urgency level (immediate, soon, planning)

Return My analysis in this format:
RESOURCE_TYPE: [type]
LOCATION: [location]
SPECIAL_NEEDS: [needs]
URGENCY: [urgency level]

User Request: {user_request}

My Analysis:""",
            input_variables=["user_request"]
        )
    
    def search(self, user_request: str, all_resources: List[Dict]) -> List[Dict]:
        """Search for relevant resources based on user request"""
        
        # Use LLM to analyze the request
        chain = self.prompt | self.llm
        analysis = chain.invoke({"user_request": user_request})
        
        print(f"\n🔍 SCOUT AGENT ANALYSIS:")
        print(analysis)
        
        # Filter resources
        relevant_resources = []
        user_lower = user_request.lower()
        
        for resource in all_resources:
            resource_text = (
                f"{resource['name']} {resource['resource_type']} "
                f"{resource['services']} {resource['zip_code']}"
            ).lower()
            
            # Simple keyword matching
            if any(word in resource_text for word in user_lower.split()):
                relevant_resources.append(resource)
        
        # If no matches, return all
        if not relevant_resources:
            relevant_resources = all_resources
        
        print(f" Found {len(relevant_resources)} relevant resources")
        return relevant_resources[:10]
