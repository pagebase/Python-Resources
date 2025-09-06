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

# Delete data. Takes 3 parameters. `Table name` and `column name` and `column id`
def delete_date(table_name, column_name, column_id):
    response = (
    supabase.table(table_name)
    .delete()
    .eq(column_name, column_id)
    .execute()
)
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
name: str = os.environ.get("name")
supabase: Client = create_client(url, key)
TABLE_NAME="Movies"
TABLE_ATTRIBUTES=["sr", "movie_name", "watched_date"]

# Insert data function call
# for i in range(4,1001):
    # insert_data(supabase, "Movies", i, "Spider-man", "2025-09-03")

# Delete data functino call
# for i in range(1,1001):
#     delete_date(TABLE_NAME, TABLE_ATTRIBUTES[0], i)