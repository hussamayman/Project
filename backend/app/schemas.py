from pydantic import BaseModel
from typing import List, Optional

class TankFact(BaseModel):
    label: str
    value: str

class PredictResponse(BaseModel):
    tank_id: str
    name: str
    confidence: float
    description: str
    facts: List[TankFact] = []
    wiki_url: Optional[str] = None
