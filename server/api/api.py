from fastapi import APIRouter

# router for fast api
router = APIRouter()

@router.post('/register')
async def register():
    # Register user phtoos into proxy
    return { 'register_status': 'success' }

@router.post('/recognize')
async def recognize():
    # Recognise the user from the proxy
    return { "face_match": True, "background_ok": True }