# Supabase connection
import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

# Insert data function
def insert_data(supabase_obj, table_name, sr_num, movie_name, watched_date):
    response = (
    supabase_obj.table(f"{table_name}")
    .insert({"sr": f"{sr_num}", "movie_name": f"{movie_name}", "watched_date":f"{watched_date}"})
    .execute()
)

# Delete data
def delete_date():
    response = (
    supabase.table("countries")
    .delete()
    .eq("id", 1)
    .execute()
)
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
name: str = os.environ.get("name")
supabase: Client = create_client(url, key)

for i in range(4,1001):
    insert_data(supabase, "Movies", i, "Spider-man", "2025-09-03")