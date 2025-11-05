from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FastAPI Shop"
    debug: bool = True
    database_url: str = "sqlite:///./shop.db"
    cors_origins: list = []
    static_dir: str = "static"
    image_dir: str = "static/images"

    class Config:
        env_file = ".env"

settings = Settings()