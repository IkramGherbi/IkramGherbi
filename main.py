from fastapi import FastAPI

app = FastAPI()

def extract_about_message(file_path: str):
    """
    Extracts the "about" message from the GFF3 file.

    Args:
        file_path (str): Path to the GFF3 file.

    Returns:
        dict: A dictionary containing the metadata from the GFF3 file.
    """
    about_message = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Stop reading when reaching sequence-region or main data
            if not line.startswith('#'):
                break

            # Extract key-value pairs from metadata lines
            if line.startswith('##') or line.startswith('#'):
                if ':' in line:
                    key, value = line.lstrip('#').split(':', 1)
                    about_message[key.strip()] = value.strip()
    
    return about_message

@app.get("/")
def get_about_message():
    """
    Endpoint to get the "about" message from the GFF3 file.

    Returns:
        dict: A dictionary containing the metadata from the GFF3 file.
    """
    file_path = "C:\\Users\\Gherb\\Hg_api\\data_chrX.gff3"  # Replace with the actual path to your GFF3 file
    about_message = extract_about_message(file_path)
    return about_message