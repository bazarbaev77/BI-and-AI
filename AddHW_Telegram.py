import os
import requests
import fitz  #pip install PyMuPDF 
from PIL import Image  #pip install Pillow

TELEGRAM_TOKEN = '7754312761:AAGRDyx5FAzPfpePLNPV7FRrsi9nr8c2hEs' 
CHANNEL_ID = '-1002489473041'

PDF_FOLDER = 'C:\\Users\\user\\Documents\\books' 
SCREENSHOT_FOLDER = 'C:\\Users\\user\\Documents\\books\\screenshots'  

if not os.path.exists(SCREENSHOT_FOLDER):
    os.makedirs(SCREENSHOT_FOLDER)

def take_screenshot(pdf_path, output_image_path):
    doc = fitz.open(pdf_path)  # Open the PDF file
    first_page = doc.load_page(0)  # Load the first page (page 0)
    
    # Render the first page as an image
    pix = first_page.get_pixmap()
    
    # Save the image to the output path
    pix.save(output_image_path)

# Function to send PDF and screenshot to the Telegram channel
def send_pdf_and_screenshot():
    # Get a list of all PDF files in the folder
    pdf_files = [f for f in os.listdir(PDF_FOLDER) if f.endswith('.pdf')]
    
    if not pdf_files:
        print('No PDF files found in the folder.')
        return
    
    # Loop through each PDF file
    for pdf_file_name in pdf_files:
        pdf_path = os.path.join(PDF_FOLDER, pdf_file_name)
        
        # Generate the screenshot image from the first page of the PDF
        screenshot_path = os.path.join(SCREENSHOT_FOLDER, f'{os.path.splitext(pdf_file_name)[0]}.png')  # Save as .png in screenshot folder
        take_screenshot(pdf_path, screenshot_path)
        
        # Send the screenshot and PDF to the Telegram channel
        send_message(f"Sending PDF: {pdf_file_name} to the channel.")
        
        # Send screenshot image
        with open(screenshot_path, 'rb') as img_file:
            data = {'chat_id': CHANNEL_ID}
            files = {'photo': img_file}
            response = requests.post(f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendPhoto', data=data, files=files)
            if response.status_code != 200:
                print(f"Failed to send screenshot: {response.text}")
            else:
                print(f"Screenshot for {pdf_file_name} sent successfully.")
        
        # Send PDF document
        with open(pdf_path, 'rb') as pdf_file:
            data = {'chat_id': CHANNEL_ID}
            files = {'document': pdf_file}
            response = requests.post(f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendDocument', data=data, files=files)
            if response.status_code != 200:
                print(f"Failed to send PDF: {response.text}")
            else:
                print(f"PDF {pdf_file_name} sent successfully.")

# Function to send a text message to Telegram channel (for debugging/logging purposes)
def send_message(text):
    data = {
        'chat_id': CHANNEL_ID,
        'text': text
    }
    response = requests.post(f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage', data=data)
    if response.status_code != 200:
        print(f"Failed to send message: {response.text}")
    else:
        print("Message sent successfully.")

# Main Execution
if __name__ == '__main__':
    send_pdf_and_screenshot()
