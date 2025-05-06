import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = 'https://gadgetandgear.com/category/phone'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all product containers
    product_containers = soup.find_all('div', class_='ProductCard_ProductCard___Lbvt ProductCard_sm__BA3zF')
    
    # List to store product details
    products = []

    # Loop through each product container and extract details
    for container in product_containers:
        # Extract product link
        product_link = container.find('a')['href']
        # Extract product image
        product_image = container.find('img')['src']
        # Extract product title
        product_title = container.find('h4', class_='ProductCard_cardTitle__HlwIo').text.strip()
        # Extract product price
        product_price = container.find('span', class_='ProductCard_price__t9DLm').text.strip()
        
        # Optional: Extract previous price if available
        previous_price = container.find('span', class_='ProductCard_prePrice__hRsk1')
        if previous_price:
            previous_price = previous_price.text.strip()
        else:
            previous_price = None
        
        # Optional: Extract reviews if available
        reviews = container.find('p', class_='text-[0.75rem] md:text-[0.83rem] text-primary-dark/80 font-semibold !mt-2').text.strip()
        
        # Append the product details to the list
        products.append({
            'link': product_link,
            'image': product_image,
            'title': product_title,
            'price': product_price,
            'previous_price': previous_price,
            'reviews': reviews
        })
        
    
    # Print the scraped product details
    for product in products:
        print(f"Title: {product['title']}")
        print(f"Price: {product['price']}")
        print(f"Previous Price: {product['previous_price']}")
        print(f"Reviews: {product['reviews']}")
        print(f"Link: {product['link']}")
        print(f"Image: {product['image']}")
        print('-' * 40)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
