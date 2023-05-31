# Saints App Data

<p align="left">
<img src="https://img.shields.io/github/languages/top/christopherlam888/saints-app-data.svg" >
<a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
<a href="https://www.gnu.org/licenses/gpl-3.0" alt="License: GPLv3"><img src="https://img.shields.io/badge/License-GPL%20v3-blue.svg"></a>
</p>

Python modules to scrape 250 of the most popular Catholic Saints and several of the most important Catholic prayers.

## Features

- Scrape hundreds of pages for saints and prayers
- Include saint name, feastday, and biography
- Include prayer name and content
- Faster scraping with multithreading
- Clean data using various methods
- Write saint and prayer object data to JSON files

## Supported Site

- Catholic Online: <https://www.catholic.org/>

## Installation

Clone/Download the GitHub repository:

```git clone https://github.com/christopherlam888/saints-app-data.git```

Navigate to the directory:

```cd saints-app-data```

Navigate to the module for saints:

```cd saints_data```

Install requirements:

```pip3 install -r requirements.txt```

Navigate to the module for prayers:

```cd prayers_data```

Install requirements:

```pip3 install -r requirements.txt```

## Usage

| **Command**                                   | **Description**                                                |
| :-------------------------------------------- | :------------------------------------------------------------- |
| `python3 -m saints_data`                      | Scrape 250 of the most popular Catholic Saints                 |
| `python3 -m prayers_data`                     | Scrape several of the most important Catholic prayers          |

## Features To Implement

- Improved data cleaning

## License
[![GNU GPLv3 Image](https://www.gnu.org/graphics/gplv3-127x51.png)](https://www.gnu.org/licenses/gpl-3.0.en.html)  

This project is licensed under the GNU General Public License v3.0.
