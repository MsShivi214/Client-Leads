# Client-Leads

# How to Run the Multi-Agent Lead Generation System

# System Requirements
To run this multi-agent lead generation system properly, you'll need:

## 1.Python Environment:
Python 3.8 or higher
Virtual environment (recommended)

## 2.Required Dependencies:
langchain==0.1.0

openai==1.3.0

python-dotenv==1.0.0

pandas==2.1.0

requests==2.31.0

beautifulsoup4==4.12.2

matplotlib (for visualization)

## 3.API Keys:
OpenAI API key (required for AI analysis)

LinkedIn API credentials (optional but recommended)

Crunchbase API key (optional but recommended)

Glassdoor API key (optional but recommended)

# Step-by-Step Setup Instructions
## 1. Set Up Your Environment
Apply to .env
### Create a virtual environment
python -m venv venv

### Activate the virtual environment
### On Windows:
venv\Scripts\activate

### On Unix or MacOS:
source venv/bin/activate

### Install required packages
pip install -r requirements.txt

## 2. Configure API Keys
Create a .env file in the root directory with your API keys:
Apply to .env
### OpenAI API Key for AI-powered analysis
OPENAI_API_KEY=your_openai_api_key_here

### LinkedIn API credentials (if using LinkedIn API)
LINKEDIN_CLIENT_ID=your_linkedin_client_id
LINKEDIN_CLIENT_SECRET=your_linkedin_client_secret
LINKEDIN_ACCESS_TOKEN=your_linkedin_access_token

# Crunchbase API key (if using Crunchbase API)
CRUNCHBASE_API_KEY=your_crunchbase_api_key

### Glassdoor API key (if using Glassdoor API)
GLASSDOOR_API_KEY=your_glassdoor_api_key

## 3. Directory Structure
Ensure your project has the following structure:

Apply to .env

multi-agent-lead-generation/

├── .env                    # Environment variables

├── requirements.txt        # Python dependencies

├── README.md              # Documentation

├── lead_generation_system.py  # Main system file

├── test_run.py            # Test script

└── agents/

    ├── __init__.py
    
    ├── research_agent.py
    
    ├── analysis_agent.py
    
    ├── contact_agent.py
    
    └── coordinator_agent.py

## 4. Create Required Directories
Apply to .env
### Create exports directory for output files
mkdir exports

# Running the System
Basic Usage

##1. Run the test script:
Apply to .env
python test_run.py

This will:
Initialize the lead generation system

Search for leads in the specified industries and countries

Export the results to a CSV file

Display a sample of the generated leads

# Customizing the Search
You can modify the search parameters in test_run.py:
Apply to .env
### Define search parameters
industries = ["Technology", "Healthcare", "Finance"]
countries = ["United States", "United Kingdom", "Canada"]

# Advanced Usage
For more advanced usage, you can import and use the system directly in your own scripts:

Apply to .env

from lead_generation_system import LeadGenerationSystem

### Initialize the system
system = LeadGenerationSystem()

### Define your search parameters
industries = ["AI/ML", "Biotech", "Renewable Energy"]
countries = ["United States", "Germany", "Singapore"]

### Find leads
leads = system.find_leads(industries, countries)

### Export results
system.export_leads(leads)


# Troubleshooting

## 1. API Key Issues:

Ensure your API keys are correctly set in the .env file

Check that the keys have sufficient permissions and quota

## 2. Import Errors:
   
Make sure all required packages are installed

Check that your Python environment is activated

## 3. Rate Limiting:

Adjust the REQUEST_DELAY in .env if you're hitting rate limits

Consider using a proxy by setting USE_PROXY=true in .env

## 4. Output Issues:

Check that the exports directory exists and is writable

Verify that you have sufficient disk space

# System Architecture

The system uses a multi-agent architecture with four specialized agents:

## 1. Research Agent: 
Gathers company data from various sources

## 2. Analysis Agent: 
Analyzes and scores companies

## 3. Contact Agent:
Gathers and validates contact information

## 4. Coordinator Agent:
Manages and ranks the leads

The workflow follows these steps:
## 1. Research phase: 
Gather raw company data

## 2 .Analysis phase: 
Analyze and score companies

## 3. Contact enrichment: 
Add validated contact information

## 4.Coordination: 
Filter, rank, and categorize leads

# Lead Scoring System
Leads are scored based on weighted criteria:
Company Size (30%)

Market Position (20%)

Contact Information Completeness (20%)

Growth Potential (30%)

And categorized by quality:
Hot: Score ≥ 0.8

Warm: Score ≥ 0.6

Lukewarm: Score ≥ 0.4

Cold: Score < 0.4


