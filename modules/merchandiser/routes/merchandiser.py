"""
Merchandiser Department API - Empty placeholder for future implementation
This module will handle merchandiser-specific operations related to:
- Style variants management
- Styling coordination
- Other merchandising tasks
"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_merchandiser_info():
    """
    Placeholder endpoint for merchandiser module
    Returns module information
    """
    return {
        "module": "merchandiser",
        "status": "placeholder",
        "description": "Merchandiser department module - coming soon",
        "features": []
    }
