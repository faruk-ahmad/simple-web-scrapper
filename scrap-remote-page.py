from bs4 import BeautifulSoup
import requests
import json

def find_job_posts_brur():
    link = "https://brur.ac.bd/career/"

    jobs = []

    try:
        source = requests.get(link).text

        soup = BeautifulSoup(source, 'lxml')

        #print(soup)

        posts = soup.find_all('div', class_='item col-sm-12 col-md-6 col-lg-4')

        for idx, post in enumerate(posts):
            title = post.find('div', class_='content').find('h6').text
            link = post.find('div', class_='content').a["href"]
            deadline = post.find('div', class_='date').p.text

            job = {'title': title, 'link': link, 'deadline': deadline}
            jobs.append(job)
    except Exception as e:
        return []
    else:
        return jobs


def make_filtering(keywords, jobs):
    results = []

    for job in jobs:
        title = job["title"]
        #print(title.split())
        
        for key in keywords:
            if key in title.split():
                results.append(job)
                break

    return results


if __name__ == '__main__':
    jobs = find_job_posts_brur()

    #print(jobs)

    keywords = ['cse', 'CSE', 'সিএসই', 'কম্পিউটার', 'teacher', 'Teacher']

    #print(keywords)

    results = make_filtering(keywords, jobs)

    data = {}

    for idx, result in enumerate(results):
        data[f'job-{idx + 1}'] = result

    with open('job_found.json', 'w') as js:
        js.write(json.dumps(data, indent = 4))