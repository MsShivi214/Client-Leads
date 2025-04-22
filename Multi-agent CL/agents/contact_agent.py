from typing import List, Dict
import re
import requests
from bs4 import BeautifulSoup

class ContactAgent:
    def __init__(self):
        self.email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        self.phone_pattern = r'^\+?1?\d{9,15}$'

    def enrich_contact_info(self, companies: List[Dict]) -> List[Dict]:
        """
        Enrich company data with contact information
        """
        enriched_companies = []
        
        for company in companies:
            # Get contact information
            contact_info = self._gather_contact_info(company)
            
            # Validate contact information
            validated_contacts = self._validate_contacts(contact_info)
            
            # Add contact information to company data
            company['contacts'] = validated_contacts
            enriched_companies.append(company)
        
        return enriched_companies

    def _gather_contact_info(self, company: Dict) -> Dict:
        """
        Gather contact information from various sources
        """
        # This is a placeholder implementation
        # In a real implementation, you would:
        # 1. Scrape company website for contact information
        # 2. Use APIs to gather contact data
        # 3. Cross-reference with other data sources
        
        return {
            'email': f'contact@{company["name"].lower().replace(" ", "")}.com',
            'phone': '+1-555-0123',
            'address': f'123 Business St, {company["country"]}',
            'social_media': {
                'linkedin': f'https://linkedin.com/company/{company["name"].lower().replace(" ", "")}',
                'twitter': f'https://twitter.com/{company["name"].lower().replace(" ", "")}'
            }
        }

    def _validate_contacts(self, contact_info: Dict) -> Dict:
        """
        Validate contact information
        """
        validated = {}
        
        # Validate email
        if 'email' in contact_info:
            if re.match(self.email_pattern, contact_info['email']):
                validated['email'] = contact_info['email']
        
        # Validate phone
        if 'phone' in contact_info:
            if re.match(self.phone_pattern, contact_info['phone']):
                validated['phone'] = contact_info['phone']
        
        # Validate address
        if 'address' in contact_info:
            validated['address'] = contact_info['address']
        
        # Validate social media
        if 'social_media' in contact_info:
            validated['social_media'] = {}
            for platform, url in contact_info['social_media'].items():
                if self._validate_url(url):
                    validated['social_media'][platform] = url
        
        return validated

    def _validate_url(self, url: str) -> bool:
        """
        Validate if a URL is accessible
        """
        try:
            response = requests.head(url, timeout=5)
            return response.status_code == 200
        except:
            return False

    def _extract_contacts_from_website(self, url: str) -> Dict:
        """
        Extract contact information from a company website
        """
        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # This is a placeholder implementation
            # In a real implementation, you would:
            # 1. Look for contact forms
            # 2. Extract email addresses
            # 3. Find phone numbers
            # 4. Locate social media links
            
            return {}
        except:
            return {} 