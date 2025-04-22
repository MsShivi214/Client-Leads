# Multi-Agent Lead Generation System

This system uses multiple AI agents to find and analyze potential client leads based on industry domains and countries. The system consists of four specialized agents working together:

1. **Research Agent**: Gathers company data from various sources
2. **Analysis Agent**: Analyzes and scores companies based on multiple criteria
3. **Contact Agent**: Gathers and validates contact information
4. **Coordinator Agent**: Manages and ranks the leads

## Features

- Multi-agent architecture for specialized tasks
- Industry and country-based lead filtering
- AI-powered company analysis
- Contact information validation
- Lead scoring and ranking
- Export functionality to CSV

## Installation

1. Clone the repository
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file with your API keys:
```
OPENAI_API_KEY=your_openai_api_key
```

## Usage

```python
from lead_generation_system import LeadGenerationSystem

# Initialize the system
system = LeadGenerationSystem()

# Define search parameters
industries = ["Technology", "Healthcare"]
countries = ["United States", "Canada"]

# Find leads
leads = system.find_leads(industries, countries)

# Export results
system.export_leads(leads)
```

## Lead Scoring Criteria

The system scores leads based on the following criteria:

1. Company Size (30%)
2. Market Position (20%)
3. Contact Information Completeness (20%)
4. Growth Potential (30%)

## Lead Quality Categories

- Hot: Score >= 0.8
- Warm: Score >= 0.6
- Lukewarm: Score >= 0.4
- Cold: Score < 0.4

## Output Format

The system exports leads in CSV format with the following information:

- Company Name
- Industry
- Country
- Size
- Website
- Contact Information
- Market Analysis
- Lead Score
- Lead Quality
- Processing Date

## Notes

- The system requires an active internet connection to gather data
- API rate limits may apply when using external services
- Some features require API keys for external services "# Multi-agent-CL" 
