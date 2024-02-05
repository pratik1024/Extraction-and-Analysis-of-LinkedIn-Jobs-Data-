# Extraction-and-Analysis-of-LinkedIn-Jobs-Data-

## Objective
This project aims to extract and analyze job data from LinkedIn, focusing on worldwide job posts excluding USA and Canada. The extraction criteria include job location, type (Full time and Contract), work format (Remote), and collecting maximum information about the company and job poster. The goal is to maintain unique records based on Company, Job Location, Title, and Job Post URL. Additionally, the project is designed to be scalable by syncing the output to a Google Sheet, with each run appending unique data to the existing records.

## Project Structure

### Part 1: Data Extraction Using Scrapy
- Implemented web scraping using Scrapy to efficiently extract LinkedIn job data.
- Adhered to specified criteria such as job location, type, and work format.
- Ensured maximum information retrieval for both company and job poster.
- Maintained unique records based on Company, Job Location, Title, and Job Post URL.
- Referenced [LinkedIn Job Search](https://www.linkedin.com/jobs) for implementation.

**Note**: Please ensure that you are logged out from LinkedIn while running the scraper.

### Part 2: Google Sheet Integration
- Created a Python API to sync the scraped data to a Google Sheet.
- Integrated Google Sheets with the project using API keys.
- Ensured each run appends unique output to the existing data in the Google Sheet.

## Project Setup
1. Clone this repository to your local machine.
   ```bash
   git clone https://github.com/your-username/Extraction-Analysis-LinkedIn-Jobs.git
   ```
2. Install the required dependencies.
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Scrapy job extraction script.
   ```bash
   python scrape_jobs.py
   ```
4. Check the Google Sheet for the appended data.

## Important Note
Ensure that you keep yourself logged out from LinkedIn while scraping to avoid any issues.

## Contribution
Feel free to contribute to this project by submitting issues or pull requests.

## License
This project is licensed under the [MIT License](LICENSE).

Happy Coding! 🚀
