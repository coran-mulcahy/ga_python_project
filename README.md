# Australian supermarket scraper - Selenium (Python)

This repository is documentation of my final project for the General Assembly Python course I attended (November 2019 - March 2020).

My goal for this project was to tackle a problem that incorporates web scraping and data analysis using Python and relevant Python libraries.

The final product is envisaged to be a scraper than can be deployed on websites to extract store location data (store names and addresses) of retailers. This data will then be processed and cleaned up, resulting in a structured .csv file containing all of a retailers stores across Australia. 

This final output .csv can then be geocoded into GIS mapping software for analysis. 


RESULTS:

The final product of this project includes Python scripts for multiple supermarket brands in Australia which can be deployed to scrape store name and address data.

To do this, I used a Python library called Selenium to simulate a user traversing the website. The script will input postcodes into the search box and scrape the resulting store suggestions into a dictionary, to be output as a .csv file.

It has been intentionally left in a Jupyter Notebook for ease of use by staff with little to no programming experience.
