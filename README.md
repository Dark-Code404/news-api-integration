# Simple News Aggregator Using Django

## Overview

This project demonstrates the implementation of a simple news aggregator application using Django. It fetches real-time news data from the [NewsAPI](https://newsapi.org/) and displays it based on user preferences such as country and category.

## Technologies Used

- **Django**: For web application development and template rendering.
- **NewsAPI**: For fetching real-time news data.
- **Python's** `requests Library`: For making HTTP requests to fetch data from NewsAPI.
- **Decouple**: For managing sensitive information like API keys.
- **HTML/CSS**: For creating a simple and user-friendly interface.

## Features

- **Real-Time News Updates**: Fetches and displays the latest news headlines using NewsAPI.
- **Search by Country**: Users can enter a country code to get news specific to that country.
- **Category Filtering**: Allows filtering news by categories like business, health, sports, etc.
- **Formatted Display**: News articles include titles, descriptions, images, authors, and publication dates.
- **Responsive UI**: Optimized for a seamless browsing experience.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Dark-Code404/news-api-integration.git
    cd news-api-integration
   ```

2. **Configure API Key**:
   - `Create .env file and add your NewsAPI key to the .env file -> api_key='your_news_api_key.'`


4. **Run Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Start the Development Server**:
   ```bash
   python manage.py runserver
   ```

***For more details on using the NewsAPI and Django, refer to their respective official documentation.***


   

 **Sample**

![image_2025-01-23_012507798](https://github.com/user-attachments/assets/991f5f27-84dd-4cfd-b41f-20a13c840730)
![image_2025-01-23_012929375](https://github.com/user-attachments/assets/1b4f3a6f-0a4f-4732-89fa-b06b954c22ee)


    
