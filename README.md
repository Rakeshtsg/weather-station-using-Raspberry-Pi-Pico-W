# weather-station-using-Raspberry-Pi-Pico-W
Welcome to the Raspberry Pico Weather Station project! This repository contains code for creating a weather station using a Raspberry Pico microcontroller. The weather station collects data from a BMP180 sensor and presents it through a dynamic web page.

Features
Real-time Data: Get accurate and up-to-date weather information, including temperature, pressure, and altitude.

Interactive Web Interface: Access the weather station's data through a user-friendly web page that automatically refreshes.

Efficient Design: The code is optimized for memory usage and stability, ensuring consistent performance over time.

Overview
Page 1: Weather Station Overview
Import essential libraries like network, socket, and modules from machine and time for seamless operation.

Initialize onboard LED and I2C communication to control peripherals.

Set up WiFi credentials for seamless network connectivity.

Visualize WiFi connection status through the onboard LED.

Connect to the WiFi network and display the Raspberry Pico's IP address on successful connection.

Page 2: Web Page Generation and Sensor Data Collection
Define the web_page function, generating a visually appealing HTML web page for data display.

Utilize the BMP180 sensor to gather temperature, pressure, and altitude data via the I2C interface.

Set sensor parameters for accurate readings, including oversampling and sea level pressure.

Present collected data in both Celsius and Fahrenheit, enhancing user convenience.

Format the data elegantly in string form, complete with relevant units.

Design an HTML structure that organizes the sensor readings within visually appealing cards on the web page.

Page 3: Web Server Setup and Continuous Data Serving
Establish a web server using a socket on port 80 for data dissemination.

Employ an infinite loop to perpetually listen for incoming client connections.

Implement memory management by performing garbage collection to ensure smooth operation.

Handle client requests gracefully by processing them with low latency.

Generate the HTML content using the web_page function.

Craft a well-formed HTTP response with the correct status code and headers.

Seamlessly send the HTML content to clients, fostering an efficient user experience.

Ensure robustness by handling potential OS errors with connection closure.

Getting Started
Clone this repository to your local machine.
Follow the setup instructions in the respective code sections.
Deploy the code to your Raspberry Pico.
Access the weather station's web page by navigating to its IP address.
Contribution
Contributions are welcome! Whether you're fixing a bug, enhancing features, or adding examples, your contributions make this project better for everyone. Feel free to fork and submit pull requests.

License
