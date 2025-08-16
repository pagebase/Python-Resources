from supabase import create_client, Client

url= "https://omvilaxadaowyogomizr.supabase.co"
key= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9tdmlsYXhhZGFvd3lvZ29taXpyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTM1NDU5NjIsImV4cCI6MjA2OTEyMTk2Mn0.DCy09VioZIO-6W68ETAYeV7nnTWbt1uYDyolmR7CSvc"

supabase: Client = create_client(url, key)

data = {
    "Sr.No": 1,
    "Show": "Dept Q",
    "Watched_Date": "2025-07-25"
}

response = supabase.table("TV_Show").insert(data).execute()

if response.data:
    print("Data inserted successfully:", response.data)
else:
    print("Error:", response.error)
