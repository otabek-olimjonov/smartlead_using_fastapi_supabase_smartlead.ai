from fastapi import APIRouter, Request, HTTPException
from app.services.supabase_service import SupabaseService
from app.utils.error_handling import logger

router = APIRouter()

@router.post("/smartlead/webhook")
async def handle_smartlead_webhook(
    request: Request, 
    supabase_service: SupabaseService
):
    """
    Handle webhooks from Smartlead for lead status updates
    """
    try:
        # Parse webhook payload
        webhook_data = await request.json()
        
        # Extract necessary information
        lead_id = webhook_data.get('lead_id')
        status = webhook_data.get('status')
        
        # Update lead status in Supabase
        if lead_id and status:
            await supabase_service.update_lead_status(lead_id, status)
            
            logger.info(f"Updated lead {lead_id} with status: {status}")
            return {"status": "success"}
        
        raise HTTPException(status_code=400, detail="Invalid webhook payload")
    
    except Exception as e:
        logger.error(f"Webhook processing error: {str(e)}")
        raise HTTPException(status_code=500, detail="Webhook processing failed")