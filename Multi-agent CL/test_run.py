from lead_generation_system import LeadGenerationSystem
import json
from pprint import pprint

def run_lead_generation():
    print("Initializing Lead Generation System...")
    system = LeadGenerationSystem()
    
    # Define search parameters
    industries = ["AI/ML", "Biotech", "Renewable Energy"]
    countries = ["United States", "Germany", "Singapore"]
    
    print(f"\nSearching for leads in industries: {industries}")
    print(f"Countries: {countries}\n")
    
    # Find leads
    leads = system.find_leads(industries, countries)
    
    # Export results
    export_result = system.export_leads(leads)
    print(f"\n{export_result}")
    
    # Display sample of results
    print("\nSample of Generated Leads:")
    print("=" * 80)
    for i, lead in enumerate(leads[:3], 1):
        print(f"\nLead {i}:")
        print(f"Company: {lead['name']}")
        print(f"Industry: {lead['industry']}")
        print(f"Country: {lead['country']}")
        print(f"Size: {lead['size']}")
        print(f"Lead Quality: {lead['lead_quality']}")
        print(f"Total Score: {lead['total_score']:.2f}")
        print("-" * 40)
    
    print(f"\nTotal leads generated: {len(leads)}")
    print("Full results have been exported to leads.csv")

if __name__ == "__main__":
    run_lead_generation() 