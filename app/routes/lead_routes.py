from fastapi import APIRouter, Depends, HTTPException
from typing import Any, List, Dict
from app.services.smartlead_service import SmartleadService
from app.services.supabase_service import SupabaseService
from app.models.lead_model import LeadCreate, LeadResponse

router = APIRouter()

@router.post("/campaigns", response_model=Dict[str, Any])
async def create_campaign(
    campaign_data: Dict[str, Any], 
    smartlead_service: SmartleadService = Depends(SmartleadService)
):
    """
    Create a new campaign in Smartlead
    """
    try:
        return await smartlead_service.create_campaign(campaign_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/leads", response_model=List[LeadResponse])
async def add_leads(
    campaign_id: str, 
    leads: List[LeadCreate],
    smartlead_service: SmartleadService = Depends(SmartleadService),
    supabase_service: SupabaseService = Depends(SupabaseService)
):
    """
    Add leads to a campaign and store in Supabase
    """
    try:
        # Add leads to Smartlead campaign
        smartlead_response = await smartlead_service.add_leads(campaign_id, [lead.dict() for lead in leads])
        
        # Store leads in Supabase
        stored_leads = []
        for lead in leads:
            lead_data = lead.dict()
            lead_data['campaign_id'] = campaign_id
            stored_lead = await supabase_service.insert_lead('leads', lead_data)
            stored_leads.append(stored_lead)
        
        return stored_leads
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))