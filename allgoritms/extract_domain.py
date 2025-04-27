# این برنامه از کاربر به عنوان ورودی یک یو ار ال میگیرد و ان را تجزیه میکند و فقط دامین اصلی ان را بر میگرداند



def extract_domain(url):
  
    if "://" in url:
        url = url.split("://")[1]


    domain_parts = url.split("/")[0].split(".")

    if 'www' in domain_parts:
        domain_parts.remove('www')

    domain = domain_parts[0]

    return domain


url = input("please enter your url --> ")

print(f"url = {url} -> domain name = {extract_domain(url)}")

