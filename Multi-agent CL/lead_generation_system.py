import os
from dotenv import load_dotenv
from agents.research_agent import ResearchAgent
from agents.analysis_agent import AnalysisAgent
from agents.contact_agent import ContactAgent
from agents.coordinator_agent import CoordinatorAgent

class LeadGenerationSystem:
    def __init__(self):
        load_dotenv()
        self.research_agent = ResearchAgent()
        self.analysis_agent = AnalysisAgent()
        self.contact_agent = ContactAgent()
        self.coordinator = CoordinatorAgent()

    def find_leads(self, industry_domains, countries):
        """
        Main method to find leads based on industry domains and countries
        """
        # Step 1: Research phase
        raw_data = self.research_agent.gather_company_data(industry_domains, countries)
        
        # Step 2: Analysis phase
        analyzed_leads = self.analysis_agent.analyze_companies(raw_data)
        
        # Step 3: Contact information gathering
        leads_with_contacts = self.contact_agent.enrich_contact_info(analyzed_leads)
        
        # Step 4: Final coordination and filtering
        final_leads = self.coordinator.filter_and_rank_leads(leads_with_contacts)
        
        return final_leads

    def export_leads(self, leads, format='csv'):
        """
        Export leads to a file
        """
        if format == 'csv':
            import pandas as pd
            df = pd.DataFrame(leads)
            df.to_csv('leads.csv', index=False)
            return "Leads exported to leads.csv"
        else:
            return "Unsupported format"

if __name__ == "__main__":
    # Example usage
    system = LeadGenerationSystem()
    
    # Define search parameters
    industries = ["Technology", "Healthcare", "Finance"]
    countries = ["United States", "United Kingdom", "Canada"]
    
    # Find leads
    leads = system.find_leads(industries, countries)
    
    # Export results
    system.export_leads(leads) 