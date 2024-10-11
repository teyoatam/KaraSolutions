import logging
from cleaning_raw_data import clean_data

# Configure logging
logging.basicConfig(filename='logs/data_cleaning.log', level=logging.INFO, 
                    format='%(asctime)s :: %(levelname)s :: %(message)s')

if __name__ == "__main__":
    csv_files = [
        '../telegram_data_scrapper/output/data/cheMed.csv',
        '../telegram_data_scrapper/output/data/Doctorset.csv',
        '../telegram_data_scrapper/output/data/EAHCI.csv ']