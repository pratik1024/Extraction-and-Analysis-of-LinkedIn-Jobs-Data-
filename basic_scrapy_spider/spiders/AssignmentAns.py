import scrapy
import gspread
from google.oauth2 import service_account
from google.auth.transport.requests import Request
from google.auth.exceptions import RefreshError

class LinkedJobsSpider(scrapy.Spider):
    name = "linkedin_jobs"
    api_url = 'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=Data%2BScience&location=&geoId=&trk=public_jobs_jobs-search-bar_search-submit&start='

    credentials_file = 'D:/Internship/Assignment_LinkedIn_Scrapy/basic-scrapy-project/basic_scrapy_spider/assignment-ans-linked-job-data-283be7fe9ec5.json'

    def start_requests(self):
        first_job_on_page = 0
        first_url = self.api_url + str(first_job_on_page)
        yield scrapy.Request(url=first_url, callback=self.parse_job, meta={'first_job_on_page': first_job_on_page})

    def parse_job(self, response):
        first_job_on_page = response.meta['first_job_on_page']

        job_item = {}
        jobs = response.css("li")
        num_jobs_returned = len(jobs)

        for job in jobs:
            job_location = job.css('.job-search-card__location::text').get(default='not-found').strip()

            # Check if the job location is not in the United States or Canada
            if "United States" not in job_location and "Canada" not in job_location:
                job_item['job_title'] = job.css("h3::text").get(default='not-found').strip()
                job_item['job_detail_url'] = job.css(".base-card__full-link::attr(href)").get(default='not-found').strip()
                job_item['job_listed'] = job.css('time::text').get(default='not-found').strip()
                job_item['company_name'] = job.css('h4 a::text').get(default='not-found').strip()
                job_item['company_link'] = job.css('h4 a::attr(href)').get(default='not-found')
                job_item['company_location'] = job_location

                yield job_item

        # for next 25 pages
        if num_jobs_returned > 0:
            first_job_on_page = int(first_job_on_page) + 25
            next_url = self.api_url + str(first_job_on_page)

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            }

            # Save data to Google Sheets
            self.save_to_google_sheets(job_item)

            yield scrapy.Request(url=next_url, callback=self.parse_job, meta={'first_job_on_page': first_job_on_page})

    def save_to_google_sheets(self, job_item):
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

        credentials = service_account.Credentials.from_service_account_file(
            self.credentials_file, scopes=scope
        )

        # Check if the credentials are expired and refresh them if needed
        try:
            credentials.refresh(Request())
        except RefreshError:
            pass

        gc = gspread.authorize(credentials)

        # Open the Google Sheet by its title
        sheet = gc.open("Assignment Ans LinkedIn data (Pratik Dash)").sheet1

        # Append data to the sheet
        sheet.append_row([job_item['job_title'], job_item['job_detail_url'], job_item['job_listed'],
                          job_item['company_name'], job_item['company_link'], job_item['company_location']])
