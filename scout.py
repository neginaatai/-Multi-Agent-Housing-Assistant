from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from typing import List, Dict
from vector_store import search_resources  # ADD THIS

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
        """Search for relevant resources using vector similarity"""
        
        # Use LLM to analyze the request
        chain = self.prompt | self.llm
        analysis = chain.invoke({"user_request": user_request})
        
        print(f"\n🔍 SCOUT AGENT ANALYSIS:")
        print(analysis)
        
        # USE VECTOR SEARCH INSTEAD OF KEYWORD MATCHING
        relevant_resources = search_resources(user_request, top_k=10)
        
        print(f"✅ Found {len(relevant_resources)} relevant resources via vector search")
        return relevant_resources
