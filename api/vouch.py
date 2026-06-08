import time

def submitVouch(voucher, vouchee, message, supabase):
    try:
        response = (
            supabase.schema("mccapes").table("vouches")
            .insert({
                "vouchee": vouchee,
                "voucher": voucher,
                "message": message
            })
            .execute()
        )

        print("SUCCESS:", response)

        whoVouchedWhoWhen[(voucher, vouchee)] = time.time()
        return (True, response)

    except Exception as e:
        # print("ERROR inserting vouch:", e)
        return {False, e}

whoVouchedWhoWhen = {
    
}