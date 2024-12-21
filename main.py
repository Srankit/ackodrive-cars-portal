import requests
import bs4
import re
import csv



url = input("Enter your URL: ")

try:
    response = requests.get(url, verify=False)
    response.raise_for_status()  
except requests.exceptions.RequestException as e:
    print(f"Error fetching the URL: {e}")
    exit()  
bs = bs4.BeautifulSoup(response.text, "html.parser")

try:
    filename = "temp.html"
    with open(filename, "w+", encoding='utf-8') as file:
        file.write(bs.prettify())
    print(f"HTML saved to {filename}")
except Exception as e:
    print(f"Error saving file: {e}")
car_names = []
prices = []
features = []
image_urls = []

for car in bs.find_all('a', class_='styles__AnchorTagWithoutUnderline-sc-aa3bd0b2-33 entJqy'):
    car_name = car.find('h4', class_='styles__VariantTitle-sc-aa3bd0b2-10 kqHbXK')
    if car_name:
        car_names.append(car_name.get_text(strip=True))

for price in bs.find_all('div', class_='styles__VariantPrice-sc-aa3bd0b2-15 bgsgnE'):
    price_tag = price.find('div', class_='styles__Price-sc-aa3bd0b2-18 bzmdsn')
    if price_tag:
        prices.append(price_tag.get_text(strip=True))

for feature in bs.find_all('div', class_='styles__VariantInfo-sc-aa3bd0b2-12 kCNdrj'):
    fuel_type = feature.find('p', class_='styles__ParaWithoutMargins-sc-aa3bd0b2-34 hVfpJl')
    transmission = feature.find_all('p', class_='styles__ParaWithoutMargins-sc-aa3bd0b2-34 hVfpJl')
    feature_text = [fuel_type.get_text(strip=True) if fuel_type else '']
    for trans in transmission:
        feature_text.append(trans.get_text(strip=True))
    features.append(", ".join(feature_text))

for img in bs.find_all('img', attrs={'src': re.compile("^https://")}):
    img_url = img.get('src');
    if img_url:
        image_urls.append(img_url);

for noscript in bs.find_all('noscript'):
    noscript_img = noscript.find('img');
    if noscript_img:
        img_url = noscript_img.get('src');
        if img_url:
            image_urls.append(img_url);
            
anchor_count = len(bs.find_all('a'))
image_count = len(image_urls)            

print("Car Names:", car_names);
print("Prices:", prices);
print("Features:", features);
print("Image URLs:", image_urls);
print(f"Number of anchor tags ===========> {anchor_count}")
print(f"Number of image URLs=============> {image_count}")
if len(car_names) > 0: 
    try:
        csv_filename = "car_data.csv"
        with open(csv_filename, 'w+', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Car Name', 'Price', 'Features', 'Image URL']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames);
            writer.writeheader();
            max_len = max(len(car_names), len(prices), len(features), len(image_urls));
            print(f"Max Length for Rows: {max_len}");
            
            for i in range(max_len):
                
                writer.writerow({
                    'Car Name': car_names[i] if i < len(car_names) else '',
                    'Price': prices[i] if i < len(prices) else '',
                    'Features': features[i] if i < len(features) else '',
                    'Image URL': image_urls[i] if i < len(image_urls) else ''
                })

        print(f"Data has been saved to {csv_filename}")
        print(f"First 5 Car Names: {car_names[:5]}")  
        print(f"First 5 Prices: {prices[:5]}")  
        print(f"First 5 Features: {features[:5]}")  
        print(f"First 5 Image URLs: {image_urls[:5]}")  

    except Exception as e:
        print(f"Error saving CSV file: {e}")
else:
    print("No car data was extracted. Please check the page structure and adjust the extraction logic.")
