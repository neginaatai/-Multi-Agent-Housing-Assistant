# python library for operating system
import os
# let load venv libraries and packages into this application
from dotenv import load_dotenv
# access database for search
# data_loader to fetch and process raw data before use
from data_loader import load_housing_data
from agents.scout import ScoutAgent
from agents.analyst import AnalystAgent
from agents.advisor import AdvisorAgent

# Load environment variables
load_dotenv()

class MultiAgentHousingAssistant:
    """Orchestrates multiple agents to help find housing"""
    
    def __init__(self):
        print(" Initializing Multi-Agent Housing Assistant...")
        
        # Load housing data
        self.housing_data = load_housing_data()
        print(f" Loaded {len(self.housing_data)} housing resources")
        
        # Initialize agents
        self.scout = ScoutAgent()
        self.analyst = AnalystAgent()
        self.advisor = AdvisorAgent()
        print(" All agents initialized\n")
    
    def process_request(self, user_request: str) -> str:
        """Process a user request through all agents"""
        
        print(f"\n{'='*60}")
        print(f"USER REQUEST: {user_request}")
        print(f"{'='*60}")
        
        # Step 1: Scout searches for relevant resources
        print("\n📍 STEP 1: Scout Agent searching...")
        relevant_resources = self.scout.search(user_request, self.housing_data)
        
        if not relevant_resources:
            return "I apologize, but I couldn't find any resources matching your needs. Could you provide more details?"
        
        # Step 2: Analyst evaluates and ranks
        print("\n📊 STEP 2: Analyst Agent evaluating...")
        ranked_resources = self.analyst.analyze(user_request, relevant_resources)
        
        # Step 3: Advisor communicates recommendations
        print("\n💬 STEP 3: Advisor Agent formulating response...")
        final_response = self.advisor.advise(user_request, ranked_resources)
        
        print(f"\n{'='*60}")
        print(" PROCESS COMPLETE")
        print(f"{'='*60}\n")
        
        return final_response


def main():
    """Test the multi-agent system"""
    assistant = MultiAgentHousingAssistant()
    
    # Test query
    test_query = "I need emergency housing assistance"
    
    response = assistant.process_request(test_query)
    print("\n" + "="*60)
    print("FINAL RESPONSE TO USER:")
    print("="*60)
    print(response)
    print("\n" + "="*60 + "\n")


if __name__ == "__main__":
    main()

