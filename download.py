import datetime
import requests
import os

def download_images(dir_path, start_datetime, end_datetime):
    # Ensure the directory exists
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    
    current_datetime = start_datetime
    while current_datetime <= end_datetime:
        formatted_time = current_datetime.strftime('%Y%m%d%H%M')
        url = f"https://www.cwa.gov.tw/Data/radar/CV1_3600_{formatted_time}.png"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                file_path = os.path.join(dir_path, f"{formatted_time}.png")
                with open(file_path, 'wb') as file:
                    file.write(response.content)
                print(f"Downloaded {file_path}")
            else:
                print(f"Failed to download {url}")
        except Exception as e:
            print(f"Error downloading {url}: {e}")
        current_datetime += datetime.timedelta(minutes=10)

# Define the start and end datetime
start_datetime = datetime.datetime(datetime.datetime.now().year, 10, 1, 14, 10)
end_datetime = datetime.datetime.now()

# Start downloading images
typhoonName = "山陀兒"
download_images(typhoonName, start_datetime, end_datetime)