from pydantic_settings  import BaseSettings # type: ignore

class Settings(BaseSettings):
    """Settings for the application."""
    db_name: str
    db_username: str
    db_host: str
    db_port: str
    db_password: str
    
    class Config:
        env_file = ".env"
        
        
settings = Settings()