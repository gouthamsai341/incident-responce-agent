from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    hindsight_url: str = "http://localhost:8888"
    hindsight_api_key: str | None = None
    hindsight_bank_id: str = "recallops"
    openrouter_api_key: str
    openrouter_model: str = "openai/gpt-4o-mini"
    openrouter_base_url: str = "https://openrouter.ai/api/v1"
    app_name: str = "RecallOps"
    cors_origins: str = "http://localhost:5173"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
