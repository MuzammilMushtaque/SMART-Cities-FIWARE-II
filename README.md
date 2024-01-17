# Smart Weather System using Fiware/Orion

This repository contains a Python application for simulating and managing real-time weather data using Fiware/Orion Context Broker and a Flask web application to display the current weather status.

## Prerequisites

- Docker
- Docker Compose

## Introduction

This project showcases a Smart Weather System built on Fiware technology, leveraging the Orion Context Broker and NGSIv2 protocol. The Context Broker is a crucial component for managing context information in a scalable and standardized manner. NGSIv2 (Next Generation Service Interface) is the API specification used for interactions with the Context Broker.

## Setup

1. **Create Docker Images/Containers for MongoDB and FIWARE Context Broker**

   Open the terminal and run the following commands:

   ```bash
   docker pull mongo
   docker run -d --name mongodb -p 27017:27017 mongo
   docker pull fiware/orion
   docker run -d --name orion -p 1026:1026 --link mongodb:mongodb fiware/orion -dbhost mongodb
   ```

2. **Run the `weather_manager.py` Application**

   `weather_manager.py` is the Python application that interacts with the Context Broker to collect and manage real-time weather data using NGSI-V2. The `WeatherObserved` data model is implemented to gather information from the OpenWeatherMap API. In the same directory as `Dockerfile`, `requirements.txt`, and `weather_manager.py` files, open the terminal and run:

   ```bash
   docker build -t weather-manager .
   docker run weather-manager
   ```

3. **Display Current Weather Status**

   Build a new Docker container to extract the outcomes of weather-manager from Orion. To achieve this, go to the `Display` folder and run:

   ```bash
   docker build -t weather-app .
   docker run -p 5000:5000 weather-app
   ```

   Results are displayed on [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Why Fiware/Orion and NGSIv2?

- **Scalability:** Orion Context Broker provides a scalable solution for managing and processing context information in real-time, making it suitable for applications with varying data volumes.

- **Standardization:** NGSIv2 is a standardized API that allows interoperability between different components and systems, promoting consistency and ease of integration.

- **Real-time Updates:** NGSIv2 enables real-time updates and queries, making it ideal for applications that require up-to-date context information, such as a Smart Weather System.

- **WeatherObserved Data Model:** The WeatherObserved data model plays a crucial role in representing real-time weather information. It provides a standardized structure for capturing key weather parameters such as temperature, humidity, wind speed, illuminance, etc. This model ensures consistency and interoperability when collecting and managing weather data.

- **Applications:** The WeatherObserved data model can be utilized in various applications, including but not limited to:

  - **Smart Cities:** Enhance urban planning and resource management by integrating real-time weather data into smart city applications.
  
  - **Agriculture:** Optimize agricultural practices by leveraging weather information for crop management, irrigation, and pest control.
  
  - **Emergency Response:** Improve disaster preparedness and response mechanisms with accurate and timely weather observations.
  
  - **Transportation:** Enhance transportation systems by considering weather conditions for route planning and traffic management.

## Contributing

Feel free to contribute to enhancing functionality or fixing issues. Create a pull request or open an issue for discussions.