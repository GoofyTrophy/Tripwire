import RPi.GPIO as GPIO
import time
from telegram import Bot

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
LDR_PIN = 17  # Replace with your GPIO pin number
GPIO.setup(LDR_PIN, GPIO.IN)

# Initialize Telegram Bot
BOT_API_TOKEN = "YOUR_BOT_API_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"  # Replace with your Telegram chat ID
bot = Bot(token=BOT_API_TOKEN)

# Set the initial light level (adjust this value as needed)
initial_light_level = GPIO.input(LDR_PIN)

# Function to send a message on Telegram
def send_telegram_message(message):
    bot.send_message(chat_id=CHAT_ID, text=message)

try:
    while True:
        # Read the current light level
        current_light_level = GPIO.input(LDR_PIN)

        # Check for a significant change in light level
        if current_light_level != initial_light_level:
            if current_light_level == 1:
                print("Intruder Detected!")
                send_telegram_message("Intruder Detected!")

            # Update the initial light level
            initial_light_level = current_light_level

        # Wait for a moment before checking again (adjust as needed)
        time.sleep(2)

except KeyboardInterrupt:
    GPIO.cleanup()
