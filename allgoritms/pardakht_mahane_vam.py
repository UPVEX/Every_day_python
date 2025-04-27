#pardakht_mahane_vam




def pardakht_mahane_vam(principle, interest_rate_per_year, duration):
    
    if interest_rate_per_year == 0:
        return principle/(duration*12)
    
    r=interest_rate_per_year/100/12
    n=duration*12
    montly_payment=principle*(r*((1.0+r)**n))/(float((1.0+r)**n)-1.0)
    
    return montly_payment

#main

