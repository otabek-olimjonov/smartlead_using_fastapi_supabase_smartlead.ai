from app.services.supabase_service import SupabaseService
from typing import List, Dict, Any
from datetime import datetime, timedelta

class AnalyticsService:
    def __init__(self, supabase_service: SupabaseService):
        self.supabase_service = supabase_service
    
    async def get_campaign_performance(self, campaign_id: str, days: int = 30) -> Dict[str, Any]:
        """
        Generate performance analytics for a campaign
        
        :param campaign_id: ID of the campaign
        :param days: Number of days to analyze
        :return: Campaign performance metrics
        """
        try:
            # Retrieve leads for the campaign
            leads = await self.supabase_service.get_leads_for_campaign(campaign_id)
            
            # Calculate performance metrics
            total_leads = len(leads)
            recent_leads = [
                lead for lead in leads 
                if lead['created_at'] >= datetime.now() - timedelta(days=days)
            ]
            
            # Aggregate status distribution
            status_distribution = {}
            for lead in leads:
                status = lead.get('status', 'unknown')
                status_distribution[status] = status_distribution.get(status, 0) + 1
            
            return {
                "campaign_id": campaign_id,
                "total_leads": total_leads,
                "leads_in_last_30_days": len(recent_leads),
                "status_distribution": status_distribution,
                "conversion_rate": self._calculate_conversion_rate(leads)
            }
        except Exception as e:
            raise SupabaseError(f"Failed to retrieve campaign performance: {str(e)}")
    
    def _calculate_conversion_rate(self, leads: List[Dict[str, Any]]) -> float:
        """
        Calculate conversion rate for leads
        
        :param leads: List of lead records
        :return: Conversion rate percentage
        """
        if not leads:
            return 0.0
        
        converted_leads = [
            lead for lead in leads 
            if lead.get('status', '').lower() in ['converted', 'closed', 'won']
        ]
        
        return (len(converted_leads) / len(leads)) * 100