import os
import logging
from telethon import TelegramClient
from telethon.tl.types import InputMessagesFilterPhotos
from datetime import datetime
import csv

# Define constants
API_ID = '26559639'  # Replace with your API ID
API_HASH = '3299ed6b2b0cbd2243470f18e1a77272'  # Replace with your API Hash
PHONE = '+251984956023'  # Replace with your phone number
SAVE_DIR = 'telegram_images'  # Directory to save images
CSV_FILE = 'imageoflobeli.csv'  # CSV file to save text data
CHANNELS = [
    'Chemed Telegram Channel',
    'lobelia4cosmetics'
    
]  # Add other channels as needed

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# Create a directory to save images
os.makedirs(SAVE_DIR, exist_ok=True)

# Connect to Telegram
client = TelegramClient(PHONE, API_ID, API_HASH)

async def download_images(channel):
    try:
        async for message in client.iter_messages(channel, filter=InputMessagesFilterPhotos):
            if message.photo:
                file_path = os.path.join(SAVE_DIR, f'{message.id}.jpg')
                await client.download_media(message.photo, file=file_path)
                logger.info(f'Downloaded image: {file_path}')
    except Exception as e:
        logger.error(f'Error downloading images from {channel}: {e}')

async def scrape_channel_data(channel):
    try:
        async for message in client.iter_messages(channel):
            if message.message:  # Check if the message has text
                data = {
                    'channel': channel,
                    'message_id': message.id,
                    'date': message.date.isoformat(),
                    'text': message.message
                }
                save_data_to_csv(data)
                logger.info(f'Scraped data from {channel}: {message.message}')
    except Exception as e:
        logger.error(f'Error scraping data from {channel}: {e}')

def save_data_to_csv(data):
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as file:
        fieldnames = ['channel', 'message_id', 'date', 'text']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()  # Write header only if file is new
        writer.writerow(data)

async def main():
    async with client:
        for channel in CHANNELS:
            logger.info(f'Starting to scrape images from {channel}')
            await download_images(channel)
            logger.info(f'Starting to scrape text data from {channel}')
            await scrape_channel_data(channel)

# Start the client
if __name__ == '__main__':
    import asyncio
    asyncio.run(main())