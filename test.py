from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(url, key)

def getVouches(userId, supabase):
    try:
        response = (
            supabase.schema("mccapes").table("vouches")
            .select("*")
            .eq("vouchee", userId)
            .execute()
        )

        print("SUCCESS:", response)
        return (True, response)

    except Exception as e:
        # print("ERROR inserting vouch:", e)
        return {False, e}
    

vouches = getVouches(894665274123513856, supabase=supabase)

print(vouches[1])
print(vouches[1].data)

totalVouches = 0
for vouch in vouches[1].data:
    print(vouch["id"])
    totalVouches += 1

print(totalVouches)