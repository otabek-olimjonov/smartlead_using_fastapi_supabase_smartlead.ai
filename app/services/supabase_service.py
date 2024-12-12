from datetime import datetime
from app.utils.error_handling import SupabaseError
from supabase import create_client, Client
from app.config import settings
from typing import Dict, Any, List

class SupabaseService:
    def __init__(self):
        self.client: Client = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)
    
    async def insert_lead(self, table: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Insert a lead into a specified Supabase table
        
        :param table: Name of the table
        :param data: Lead data to insert
        :return: Inserted record
        """
        try:
            response = self.client.table(table).insert(data).execute()
            return response.data[0] if response.data else None
        except Exception as e:
            raise ValueError(f"Failed to insert lead: {str(e)}")
    
    async def get_leads_for_campaign(self, campaign_id: str) -> List[Dict[str, Any]]:
        """
        Retrieve leads for a specific campaign
        
        :param campaign_id: ID of the campaign
        :return: List of leads
        """
        try:
            response = self.client.table('leads').select('*').eq('campaign_id', campaign_id).execute()
            return response.data
        except Exception as e:
            raise ValueError(f"Failed to retrieve leads: {str(e)}")
        
    async def update_lead_status(self, lead_id: str, status: str) -> Dict[str, Any]:
        """
        Update the status of a lead in Supabase
        
        :param lead_id: ID of the lead to update
        :param status: New status for the lead
        :return: Updated lead record
        """
        try:
            response = (
                self.client.table('leads')
                .update({'status': status, 'updated_at': datetime.now().isoformat()})
                .eq('id', lead_id)
                .execute()
            )
            return response.data[0] if response.data else None
        except Exception as e:
            raise SupabaseError(f"Failed to update lead status: {str(e)}")