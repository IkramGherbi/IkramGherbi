from fastapi import FastAPI

app = FastAPI()

def extract_about_message(file_path: str):
    about_message = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            
            if not line.startswith('#'):
                break

            
            if line.startswith('##') or line.startswith('#'):
                if ':' in line:
                    key, value = line.lstrip('#').split(':', 1)
                    about_message[key.strip()] = value.strip()
    
    return about_message

@app.get("/")
def get_about_message():

    file_path = "C:\\Users\\Gherb\\Hg_api\\data_chrX.gff3"
    about_message = extract_about_message(file_path)
    return about_message