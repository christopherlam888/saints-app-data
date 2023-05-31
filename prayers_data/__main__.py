from .scraper import *

import multiprocessing.dummy as multiprocessing
import tqdm
import json

def main():

    prayers = []

    print("Scraping...")

    prayers_indexes = {
        "Hail, Holy Queen": "122",
        "The Our Father": "216",
        "Hail Mary": "217",
        "Glory Be to the Father": "218",
        "The Apostle's Creed": "220",
        "The Nicene Creed": "495"
    }

    # scrape pages
    with multiprocessing.Pool(8) as pool, tqdm.tqdm(
            total=len(prayers_indexes)
    ) as pbar:
        for prayer in pool.imap_unordered(
                scrape_page, prayers_indexes.values()
        ):
            prayers.append(prayer)
            pbar.update()

    print("Scraped.")

    # write to json file
    json_data = json.dumps([prayer.__dict__ for prayer in prayers])
    with open("prayers.json", "w") as f:
        f.write(json_data)

if __name__ == "__main__":
    main() 
