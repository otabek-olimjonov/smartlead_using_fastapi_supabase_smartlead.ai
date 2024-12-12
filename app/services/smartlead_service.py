import httpx
from typing import Dict, Any
from app.config import settings
from app.utils.error_handling import SmartleadAPIError

class SmartleadService:
    def __init__(self, api_key: str = settings.SMARTLEAD_API_KEY):
        self.api_key = api_key
        self.base_url = settings.SMARTLEAD_BASE_URL
    
    async def create_campaign(self, campaign_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new campaign in Smartlead
        
        :param campaign_data: Dictionary containing campaign details
        :return: Campaign creation response
        """
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{self.base_url}/campaigns",
                    headers={
                        "Authorization": f"Bearer {self.api_key}",
                        "Content-Type": "application/json"
                    },
                    json=campaign_data
                )
                response.raise_for_status()
                return response.json()
        except httpx.HTTPStatusError as e:
            raise SmartleadAPIError(f"Failed to create campaign: {e.response.text}")
    
    async def add_leads(self, campaign_id: str, leads: list) -> Dict[str, Any]:
        """
        Add leads to a specific campaign
        
        :param campaign_id: ID of the campaign
        :param leads: List of lead details
        :return: Lead addition response
        """
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{self.base_url}/campaigns/{campaign_id}/leads",
                    headers={
                        "Authorization": f"Bearer {self.api_key}",
                        "Content-Type": "application/json"
                    },
                    json={"leads": leads}
                )
                response.raise_for_status()
                return response.json()
        except httpx.HTTPStatusError as e:
            raise SmartleadAPIError(f"Failed to add leads: {e.response.text}")
