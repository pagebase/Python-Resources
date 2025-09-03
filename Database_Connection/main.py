import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()


url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
name: str = os.environ.get("name")
supabase: Client = create_client(url, key)

response = (
    supabase.table("Movies")
    .insert({"sr": 1, "movie_name": "Mission impossible: Final reckoning", "watched_date":"2025-09-01"})
    .execute()
)