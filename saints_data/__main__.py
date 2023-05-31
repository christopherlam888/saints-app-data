from .scraper import *

import multiprocessing.dummy as multiprocessing
import tqdm
import json

source_url = "https://www.catholic.org/saints/popular.php"

def main():

    saints = []
    
    print("Scraping...")

    saints_pages = get_pages(source_url)

    # scrape pages
    with multiprocessing.Pool(8) as pool, tqdm.tqdm(
        total=len(saints_pages)
    ) as pbar:
        for saint in pool.imap_unordered(
                scrape_page, saints_pages
        ):
            saints.append(saint)
            pbar.update()

    print("Scraped.")

    # write to json file
    json_data = json.dumps([saint.__dict__ for saint in saints])
    with open("saints.json", "w") as f:
        f.write(json_data)

if __name__ == "__main__":
    main() 
