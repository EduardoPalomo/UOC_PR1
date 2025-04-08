import csv
import time
import os
import requests
from bs4 import BeautifulSoup

def get_soup(url):
    """
    Gets the HTML content from a URL and converts it into a BeautifulSoup object
    Implements a delay to avoid overloading the server
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    time.sleep(1)  # 1 second delay between requests
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        return BeautifulSoup(response.text, 'lxml')
    except Exception as e:
        print(f"Error fetching URL: {e}")
        return None

def extract_toc(url):
    """
    Extracts the table of contents from a Wikipedia page
    Returns a list of dictionaries with number and text of each section
    """
    print(f"Requesting {url}...")
    soup = get_soup(url)
    
    if not soup:
        return []

    # Find all elements that could be headings in the new Wikipedia layout
    headings = soup.find_all("li", class_="vector-toc-list-item")
    
    if not headings:
        print("No headings found in new layout, trying alternative...")
        # Try finding the old layout headings
        toc = soup.find("div", {"id": "toc"})
        if toc:
            headings = toc.find_all("li", class_=lambda x: x and "toclevel-" in x)
    
    if not headings:
        print("Could not find any table of contents elements")
        return []
        
    print(f"Found {len(headings)} potential heading elements")
    data = []
    
    for heading in headings:
        # For new layout
        if "vector-toc-list-item" in heading.get("class", []):
            number = heading.find("span", class_="vector-toc-numb")
            text = heading.find("div", class_="vector-toc-text")
            
            if not text:
                text = heading.find("a", class_="vector-toc-link")
                if text:
                    text = text.find("div", class_="vector-toc-text")
        
        # For old layout
        else:
            number = heading.find("span", class_="tocnumber")
            text = heading.find("span", class_="toctext")
        
        if text and number:
            data.append({
                'heading_number': number.text.strip(),
                'heading_text': text.text.strip(),
            })
    
    print(f"Successfully extracted {len(data)} sections")
    return data

def save_to_csv(data, filename):
    """
    Saves the data to a CSV file
    """
    if not data:
        return False
        
    try:
        # Ensure directory exists
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        
        with open(filename, "w", newline="", encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['heading_number', 'heading_text'])
            writer.writeheader()
            writer.writerows(data)
            
        return True
    except Exception as e:
        print(f"Error saving CSV file: {e}")
        return False

def main():
    # Using English Wikipedia for better compatibility
    url = "https://en.wikipedia.org/wiki/Web_scraping"
    
    # Use absolute path
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    output_file = os.path.join(project_root, "dataset", "wikipedia_toc.csv")
    
    print(f"Starting web scraping process...")
    data = extract_toc(url)
    
    if data and save_to_csv(data, output_file):
        print(f"Data successfully saved to {output_file}")
        print(f"Number of sections extracted: {len(data)}")
        
        # Print first few entries as verification
        print("\nFirst few entries:")
        for entry in data[:3]:
            print(f"{entry['heading_number']} - {entry['heading_text']}")
    else:
        print("Failed to extract or save data")

if __name__ == '__main__':
    main()