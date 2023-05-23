# YouTube Views Generator

The YouTube Views Generator is a Python script that uses the Selenium WebDriver to simulate views on YouTube videos. It opens the specified YouTube video link and plays it for a specified number of times, generating realistic view counts.

## Requirements

- Python 3.x
- Selenium WebDriver
- Chrome WebDriver (chromedriver)

## Installation

1. Install Python 3.x from the official Python website: https://www.python.org/downloads/

2. Install the Selenium package by running the following command:

    ```bash
    pip install selenium
    ```

3. Download the Chrome WebDriver (chromedriver) compatible with your Chrome browser version and operating system. Make sure to download the appropriate version from: https://sites.google.com/a/chromium.org/chromedriver/downloads

4. Place the downloaded `chromedriver` executable in the same directory as the script.

## Usage

1. Open the `main.py` file and edit the `link` and `views` variables to specify the YouTube video link and the desired number of views.

2. Run the script using the following command:

    ```bash
    python main.py
    ```

3. The script will open the YouTube video link and simulate the specified number of views by playing the video for random durations. The sleep time between each view is randomized to mimic human behavior.

4. Monitor the console output to see the progress of the views generation.

5. Once the script finishes, the Chrome browser will close automatically.

6. Run `Setup.py` Script to build EXE by following command:

    ```bash
    python setup.py build
    ```

## Notes

- This script is intended for educational and testing purposes only. Generating artificial views violates YouTube's terms of service and can lead to penalties or account termination.

- The script uses the Chrome WebDriver, so make sure you have Google Chrome installed on your system.

- Ensure that you have a stable internet connection while running the script to avoid interruptions.

## Disclaimer

The YouTube Views Generator script is provided as-is and is not affiliated with or endorsed by YouTube. The use of this script is at your own risk. The author disclaim any responsibility for any misuse or damage caused by this script.

