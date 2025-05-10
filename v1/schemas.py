from pydantic import BaseModel
from typing_extensions import Optional

class CreateCommentSchemas(BaseModel):
    content: str
    parent_id: Optional[int] = None