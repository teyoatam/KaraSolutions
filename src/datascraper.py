import os
import logging
from telethon import TelegramClient
from datetime import datetime
import csv

# Define constants
API_ID = '26559639'  # Replace with your API ID
API_HASH = '3299ed6b2b0cbd2243470f18e1a77272'  # Replace with your API Hash
PHONE = '+251984956023'  # Replace with your phone number
CHANNELS = [
    'DoctorsET',
    'lobelia4cosmetics',
    'yetenaweg',
    'EAHCI',
    'Chemed Telegram Channel'
]  # Add other channels as needed

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

def save_data_to_csv(channel, data):
    # Create a directory for the channel if it doesn't exist
    os.makedirs('scraped_data', exist_ok=True)
    filename = os.path.join('scraped_data', f'{channel}.csv')
    
    file_exists = os.path.isfile(filename)
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        fieldnames = ['message_id', 'date', 'text']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()  # Write header only if file is new
        writer.writerow(data)

async def scrape_channel_data(channel):
    try:
        async for message in client.iter_messages(channel):
            if message.message:  # Check if the message has text
                data = {
                    'message_id': message.id,
                    'date': message.date.isoformat(),
                    'text': message.message
                }
                save_data_to_csv(channel, data)
                logger.info(f'Scraped data from {channel}: {message.message}')
    except Exception as e:
        logger.error(f'Error scraping data from {channel}: {e}')

async def main():
    async with client:
        for channel in CHANNELS:
            logger.info(f'Starting to scrape text data from {channel}')
            await scrape_channel_data(channel)

# Connect to Telegram
client = TelegramClient(PHONE, API_ID, API_HASH)

# Start the client
if __name__ == '__main__':
    import asyncio
    asyncio.run(main())