# Web Scraping Jobs

This script automates the process of finding jobs from the TimesJobs Mumbai job listing website based on a specific skill. It extracts job details such as company name, location, skills required, and provides a direct link to the job posting.

## Features
- Filters job listings based on the skill provided by the user.
- Extracts details such as:
  - Skills required for the job
  - Company name
  - Job location
  - Link to the job posting
- Runs in a loop, fetching updated job postings at regular intervals.

## Requirements
- Python 3.x
- `beautifulsoup4` library
- `requests` library

## Installation
1. Clone or download this repository to your local machine.
2. Install the required libraries by running the following command:
   ```bash
   pip install beautifulsoup4 requests
   ```

## Usage
1. Run the script using the command:
   ```bash
   python script_name.py
   ```
   Replace `script_name.py` with the actual file name.

2. Enter the skill you want to filter jobs by when prompted:
   ```
   enter skill: <your_skill>
   ```

3. The script will display job postings matching your skill and output the following details for each job:
   - Skills required
   - Company name
   - Location
   - Direct link to the job posting

4. The script will repeat this process at regular intervals (1 minute by default). To stop the script, press `Ctrl+C`.

## Example Output
```
enter skill: Python
Skills: Python,Django
Company Name: XYZ Technologies
Location: Mumbai
  
https://www.timesjobs.com/job-detail/xyz-technologies
waiting for 1 minutes
```

## Notes
- The script uses the TimesJobs Mumbai jobs listing page. If the website structure changes, modifications to the script may be required.
- Ensure you have a stable internet connection when running the script.

## Future Enhancements
- Implement file handling to save job details to a text or CSV file.
- Add error handling for network issues or changes in the website structure.
- Allow the user to specify multiple skills or additional filters like experience level.
## Disclaimer
This script is for educational purposes only. Ensure compliance with the website's terms of use when using web scraping tools.

