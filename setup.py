import re,random,os

script_dir = os.path.dirname(os.path.abspath(__file__))

def scrape_numbers(text):
    regex = r'\b\d{18,19}\b'
    return re.findall(regex, text)

    

if __name__ =="__main__":
    
    with open(f"{script_dir}\\text_Scrape.txt","r") as text:
        given_text = text.read()
        scraped_numbers = scrape_numbers(given_text)
    print(scraped_numbers)
    with open(f"{script_dir}\\assets\\hacks.txt","a") as PUt:
        for i in range(1,len(scraped_numbers)):
            try:
                txt_randomisation = ['','','','','\n','','']
                PUt.write(f"{scraped_numbers[(len(scraped_numbers))-i]}\n")
                PUt.write(f"{random.choice(txt_randomisation)}")
            except Exception as e:
                print(e)