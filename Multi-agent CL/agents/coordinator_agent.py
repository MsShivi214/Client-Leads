from typing import List, Dict
import pandas as pd
from datetime import datetime

class CoordinatorAgent:
    def __init__(self):
        self.ranking_weights = {
            'company_size': 0.3,
            'market_position': 0.2,
            'contact_completeness': 0.2,
            'growth_potential': 0.3
        }

    def filter_and_rank_leads(self, leads: List[Dict]) -> List[Dict]:
        """
        Filter and rank leads based on various criteria
        """
        # Filter out invalid leads
        valid_leads = self._filter_invalid_leads(leads)
        
        # Calculate scores for each lead
        scored_leads = self._calculate_lead_scores(valid_leads)
        
        # Sort leads by score
        ranked_leads = sorted(scored_leads, key=lambda x: x['total_score'], reverse=True)
        
        # Add metadata
        for lead in ranked_leads:
            lead['processed_date'] = datetime.now().isoformat()
            lead['lead_quality'] = self._determine_lead_quality(lead['total_score'])
        
        return ranked_leads

    def _filter_invalid_leads(self, leads: List[Dict]) -> List[Dict]:
        """
        Filter out invalid or incomplete leads
        """
        valid_leads = []
        
        for lead in leads:
            if self._is_valid_lead(lead):
                valid_leads.append(lead)
        
        return valid_leads

    def _is_valid_lead(self, lead: Dict) -> bool:
        """
        Check if a lead is valid
        """
        # Check for minimum required fields
        required_fields = ['name', 'industry', 'country']
        if not all(field in lead for field in required_fields):
            return False
        
        # Check if contact information exists
        if 'contacts' not in lead:
            return False
        
        # Check if at least one contact method is available
        contacts = lead['contacts']
        if not any([
            contacts.get('email'),
            contacts.get('phone'),
            contacts.get('social_media')
        ]):
            return False
        
        return True

    def _calculate_lead_scores(self, leads: List[Dict]) -> List[Dict]:
        """
        Calculate scores for each lead
        """
        scored_leads = []
        
        for lead in leads:
            # Calculate individual component scores
            size_score = self._calculate_size_score(lead)
            market_score = self._calculate_market_score(lead)
            contact_score = self._calculate_contact_score(lead)
            growth_score = self._calculate_growth_score(lead)
            
            # Calculate total score
            total_score = (
                size_score * self.ranking_weights['company_size'] +
                market_score * self.ranking_weights['market_position'] +
                contact_score * self.ranking_weights['contact_completeness'] +
                growth_score * self.ranking_weights['growth_potential']
            )
            
            lead['total_score'] = total_score
            lead['component_scores'] = {
                'size_score': size_score,
                'market_score': market_score,
                'contact_score': contact_score,
                'growth_score': growth_score
            }
            
            scored_leads.append(lead)
        
        return scored_leads

    def _calculate_size_score(self, lead: Dict) -> float:
        """
        Calculate score based on company size
        """
        size = lead.get('size', '')
        if '1000+' in size:
            return 1.0
        elif '500-1000' in size:
            return 0.8
        elif '100-500' in size:
            return 0.6
        elif '50-100' in size:
            return 0.4
        else:
            return 0.2

    def _calculate_market_score(self, lead: Dict) -> float:
        """
        Calculate score based on market position
        """
        market_analysis = lead.get('market_analysis', {})
        market_share = market_analysis.get('market_share', '')
        
        if market_share == 'High':
            return 1.0
        elif market_share == 'Medium':
            return 0.7
        elif market_share == 'Low':
            return 0.4
        else:
            return 0.2

    def _calculate_contact_score(self, lead: Dict) -> float:
        """
        Calculate score based on contact information completeness
        """
        contacts = lead.get('contacts', {})
        score = 0.0
        
        if contacts.get('email'):
            score += 0.4
        if contacts.get('phone'):
            score += 0.3
        if contacts.get('social_media'):
            score += 0.3
        
        return score

    def _calculate_growth_score(self, lead: Dict) -> float:
        """
        Calculate score based on growth potential
        """
        market_analysis = lead.get('market_analysis', {})
        growth_rate = market_analysis.get('growth_rate', '')
        
        if growth_rate == 'High':
            return 1.0
        elif growth_rate == 'Moderate':
            return 0.7
        elif growth_rate == 'Low':
            return 0.4
        else:
            return 0.2

    def _determine_lead_quality(self, score: float) -> str:
        """
        Determine lead quality based on total score
        """
        if score >= 0.8:
            return 'Hot'
        elif score >= 0.6:
            return 'Warm'
        elif score >= 0.4:
            return 'Lukewarm'
        else:
            return 'Cold' 