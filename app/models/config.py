from pydantic import BaseModel

class ConfigResponse(BaseModel):
    max_file_size: int
    allowed_file_types: list[str]
    storage_cleanup_days: int
