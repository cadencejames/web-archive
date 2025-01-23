import os
import requests
from datetime import datetime
from newspaper import Article
from urllib.parse import urlparse
from bs4 import BeautifulSoup

# Directory to save the archive
ARCHIVE_DIR = 'archive'  # Update this as needed
INDEX_FILE_PATH = 'archive/index.html'  # Path to your index.html file

# Ensure the archive directory exists
os.makedirs(ARCHIVE_DIR, exist_ok=True)

# Function to fetch and save webpage or article text
def save_content(url):
    # Try to determine if the URL is a webpage or an image
    if url.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp')):
        save_image(url)
    else:
        # Ask user for input on whether to save full HTML or article text
        save_type = input("Do you want to save the full webpage (1) or just the article text (2)? ")
            
        if save_type == '1':
            save_full_html(url)
        elif save_type == '2':
            save_article_text(url)

# Function to save a webpage's full HTML content
def save_full_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        # Clean the URL for the file name
        file_name = clean_filename(url)
        
        # Save HTML content to a file
        html_path = os.path.join(ARCHIVE_DIR, "pages", f"{file_name}.html")
        with open(html_path, 'w', encoding='utf-8') as file:
            file.write(response.text)
        
        # Get the current date and time
        date_saved = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        html_path = os.path.join("pages", f"{file_name}.html")
        # Add entry to index.html
        add_entry_to_index(url, date_saved, html_path)
        
        print(f"Webpage saved successfully: {html_path}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching webpage: {e}")

# Function to save only the article text
def save_article_text(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        
        # Clean the URL for the file name
        file_name = clean_filename(url)
        
        # Save article text to a file
        text_path = os.path.join(ARCHIVE_DIR, "pages", f"{file_name}.txt")
        with open(text_path, 'w', encoding='utf-8') as file:
            file.write(article.text)
        
        # Get the current date and time
        date_saved = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        text_path = os.path.join("pages", f"{file_name}.txt")
        # Add entry to index.html
        add_entry_to_index(url, date_saved, text_path)
        
        print(f"Article saved successfully: {text_path}")
        
    except Exception as e:
        print(f"Error saving article: {e}")

# Function to save an image
def save_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        # Parse URL to get file name
        file_name = os.path.basename(urlparse(url).path)
        
        # Save image to archive
        image_path = os.path.join(ARCHIVE_DIR, "images", file_name)
        with open(image_path, 'wb') as file:
            file.write(response.content)
        
        # Get the current date and time
        date_saved = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        

        image_path = os.path.join("images", file_name)
        # Add entry to index.html
        add_entry_to_index(url, date_saved, image_path)
        
        print(f"Image saved successfully: {image_path}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching image: {e}")

# Function to clean and create a valid filename from the URL
def clean_filename(url):
    parsed_url = urlparse(url)
    file_name = parsed_url.netloc + parsed_url.path
    file_name = file_name.replace('/', '_').replace('?', '_').replace('&', '_')
    
    return file_name.strip('_')

# Function to add a new entry to index.html
def add_entry_to_index(url, date_saved, saved_link):
    # Open the existing index.html file and read its content
    try:
        with open(INDEX_FILE_PATH, 'r', encoding='utf-8') as file:
            html_content = file.read()
        
        # Find the closing </tbody> tag where the rows are inserted
        tbody_start = html_content.find('<tbody>')
        tbody_end = html_content.find('</tbody>')
        
        if tbody_start == -1 or tbody_end == -1:
            print("Error: <tbody> tag not found in the HTML file.")
            return
        
        # The part of the file containing the table body (rows)
        table_body = html_content[tbody_start+7:tbody_end]
        
        # Extract the title from the URL for the table row
        title = f"{url.split('/')[-1]}"
        if title == "":
            title = f"{url.split('/')[-2]}"
        
        # Create a new row with the new article info (this goes at the top)
        new_row = f'''
            <tr>
                <td>{title}</td>
                <td><a href="{url}" target="_blank">Original</a></td>
                <td>{date_saved}</td>
                <td><a href="{saved_link}" target="_blank">Saved</a></td>
            </tr>
        '''
        
        # Prepend the new row to the existing table body
        updated_table_body = new_row + table_body
        
        # Rebuild the entire HTML content with the updated table body
        updated_html_content = html_content[:tbody_start+7] + updated_table_body + html_content[tbody_end:]
        
        # Write the updated HTML content back to the index.html file
        with open(INDEX_FILE_PATH, 'w', encoding='utf-8') as file:
            file.write(updated_html_content)
        
        print(f"Entry added to index.html for {url}")
    
    except FileNotFoundError:
        print(f"Error: {INDEX_FILE_PATH} not found.")
    except Exception as e:
        print(f"Error updating index.html: {e}")

# Main function to run the script
def main():
    url = input("Enter the URL to save: ")
    save_content(url)

if __name__ == "__main__":
    main()
