from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    APP_HOST:str
    APP_PORT:int
    RELOAD:bool
    
    model_config=SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )
    
settings=Settings()    