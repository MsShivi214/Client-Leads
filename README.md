# Client-Leads

# How to Run the Multi-Agent Lead Generation System

# System Requirements
To run this multi-agent lead generation system properly, you'll need:

# 1.Python Environment:
Python 3.8 or higher
Virtual environment (recommended)
# 2.Required Dependencies:
a.langchain==0.1.0
b. openai==1.3.0
c. python-dotenv==1.0.0
d. pandas==2.1.0
e. requests==2.31.0
f. beautifulsoup4==4.12.2
g. matplotlib (for visualization)
# 3.API Keys:
OpenAI API key (required for AI analysis)
LinkedIn API credentials (optional but recommended)
Crunchbase API key (optional but recommended)
Glassdoor API key (optional but recommended)

# Step-by-Step Setup Instructions
# 1. Set Up Your Environment
Apply to .env
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On Unix or MacOS:
source venv/bin/activate
# Install required packages
pip install -r requirements.txt

# 2. Configure API Keys
Create a .env file in the root directory with your API keys:
Apply to .env
2. Directory Structure
Ensure your project has the following structure:
Apply to .env
3. Create Required Directories
Apply to .env
Run
Running the System
Basic Usage
Run the test script:
Apply to .env
Run
This will:
Initialize the lead generation system
Search for leads in the specified industries and countries
Export the results to a CSV file
Display a sample of the generated leads
Customizing the Search
You can modify the search parameters in test_run.py:
Apply to .env
Advanced Usage
For more advanced usage, you can import and use the system directly in your own scripts:
Apply to .env
Troubleshooting
API Key Issues:
Ensure your API keys are correctly set in the .env file
Check that the keys have sufficient permissions and quota
Import Errors:
Make sure all required packages are installed
Check that your Python environment is activated
Rate Limiting:
Adjust the REQUEST_DELAY in .env if you're hitting rate limits
Consider using a proxy by setting USE_PROXY=true in .env
Output Issues:
Check that the exports directory exists and is writable
Verify that you have sufficient disk space
System Architecture
The system uses a multi-agent architecture with four specialized agents:
Research Agent: Gathers company data from various sources
Analysis Agent: Analyzes and scores companies
Contact Agent: Gathers and validates contact information
Coordinator Agent: Manages and ranks the leads
The workflow follows these steps:
Research phase: Gather raw company data
Analysis phase: Analyze and score companies
Contact enrichment: Add validated contact information
Coordination: Filter, rank, and categorize leads
Lead Scoring System
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
Would you like me to explain any specific part of the setup or usage in more detail?
