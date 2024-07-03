import requests
from bs4 import BeautifulSoup
import os
import re
from urllib.parse import urljoin, urlparse

BASE_URL = 'https://protocols.opentrons.com/'
OUTPUT_FOLDER = 'output_files'

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

def get_soup(url):
    response = requests.get(url)
    response.raise_for_status()
    return BeautifulSoup(response.text, 'html.parser')

def is_valid_url(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def extract_links(soup, base_url):
    links = []
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        full_url = urljoin(base_url, href)
        if is_valid_url(full_url):
            links.append(full_url)
    return links

def download_script(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def process_page(url, visited, outputs):
    if url in visited:
        return
    visited.add(url)
    print(f'Visiting: {url}')
    
    soup = get_soup(url)
    links = extract_links(soup, url)
    
    for link in links:
        if link.endswith('.py'):
            script_content = download_script(link)
            title = soup.title.string if soup.title else 'No Title'
            link_html = str(soup.find('a', href=link))
            outputs.append({
                'title': title,
                'link_html': link_html,
                'script': script_content,
                'url': link
            })
        elif link not in visited:
            process_page(link, visited, outputs)

def save_outputs(outputs):
    for output in outputs:
        filename = re.sub(r'[^\w\s]', '', output['title']) + '.txt'
        filepath = os.path.join(OUTPUT_FOLDER, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write('protocol\n')
            f.write(output['title'] + '\n')
            f.write(output['link_html'] + '\n')
            f.write('script\n')
            f.write(output['script'] + '\n')

def main():
    visited = set()
    outputs = []
    process_page(BASE_URL, visited, outputs)
    save_outputs(outputs)
    print(f'Saved {len(outputs)} scripts.')

if __name__ == '__main__':
    main()
