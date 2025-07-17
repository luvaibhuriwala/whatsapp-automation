from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import pandas as pd

# Load contacts from Excel
file_path = "Book1.xlsx"
df = pd.read_excel(file_path)

# Initialize Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")  # Helps prevent crashes
options.add_argument("--disable-dev-shm-usage")  # Fix for some Chrome crashes
options.add_argument("--disable-gpu")  # Helps avoid rendering issues
options.add_argument("--remote-debugging-port=9222")  # Debugging workaround
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=options)

# Open WhatsApp Web
driver.get("https://web.whatsapp.com/")
input("🔄 Press Enter after scanning the QR code...")  # Wait for manual login

# Function to send message
def send_message(contact_number, message):
    #encoded_message = urllib.parse.quote(message)  # Encode message for URL
    whatsapp_url = f"https://web.whatsapp.com/send?phone={contact_number}"
    
    driver.get(whatsapp_url)  # Open chat
    time.sleep(5)  # Wait for chat to load
    
    try:
        # Find the message box
        message_box = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[3]/div/div[4]/div/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p"))
        )

        # Send the message line by line
        for line in message.split("\n"):
            message_box.send_keys(line)
            message_box.send_keys(Keys.SHIFT + Keys.ENTER)  # Add newline
        message_box.send_keys(Keys.ENTER)  # Finally, send the message

        print(f"✅ Message sent to {contact_number}")
    except Exception as e:
        print(f"❌ Failed to send message to {contact_number}: {e}")

'''def send_message(contact_number, message):
    search_box = driver.find_element(By.XPATH, "//div[@contenteditable='true']")
    search_box.clear()
    search_box.send_keys(contact_number)
    time.sleep(3)  # Wait for search results
    search_box.send_keys(Keys.ENTER)
    
    time.sleep(3)  # Wait for chat to load
    message_box = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div/div[4]/div/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p")
    
    message_box.send_keys(message)
    time.sleep(1)
    message_box.send_keys(Keys.ENTER)
def send_message(contact_number, message):
    search_box = driver.find_element(By.XPATH, "//div[@contenteditable='true']")
    search_box.clear()
    search_box.send_keys(contact_number)
    time.sleep(3)  # Wait for search results
    search_box.send_keys(Keys.ENTER)

    time.sleep(3)  # Wait for chat to load
    
    try:
        # Find the message box
        message_box = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[3]/div/div[4]/div/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p"))
        )

        # Send the message line by line
        for line in message.split("\n"):
            message_box.send_keys(line)
            message_box.send_keys(Keys.SHIFT + Keys.ENTER)  # Add newline
        message_box.send_keys(Keys.ENTER)  # Finally, send the message

        print(f"✅ Message sent to {contact_number}")

    except Exception as e:
        print(f"❌ Could not send message to {contact_number}: {e}")
'''

# Iterate through contacts
for index, row in df.iterrows():
    contact_number = str(row["Contact"]).strip()
    if not contact_number.startswith("+"):
        contact_number = "+92" + contact_number  # Add country code if missing
    
    contact_name = row.get("Name", "User")
    amount = row.get("Amount", "Unknown")
    duration = row.get("Time", "Unknown")
    
    message = f"""Hello\n{contact_name},

Thankyou
Best Regards"""

    attempts = 0
    sent = False

    while not sent and attempts < 3:
        try:
            send_message(contact_number, message)
            print(f"✅ Message sent to {contact_name} ({contact_number})")
            sent = True
        except Exception as e:
            attempts += 1
            print(f"❌ Failed to send message to {contact_name} (Attempt {attempts}/3): {e}")
            if attempts < 3:
                print("🔄 Retrying in 10 seconds...")
                time.sleep(10)  # Wait before retrying

    delay = random.randint(10, 25)  # Random delay between 10 to 25 seconds
    print(f"⏳ Waiting {delay} seconds before sending the next message...")
    time.sleep(delay)

# Close the browser after sending all messages
print("🚪 Closing WhatsApp Web...")
driver.quit()
