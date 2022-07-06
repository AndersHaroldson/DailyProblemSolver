import requests
from bs4 import BeautifulSoup
import smtplib
import time
import random

AMC_YR = random.randint(1985, 2019)

status = str(AMC_YR)

URL = 'https://artofproblemsolving.com/wiki/index.php/AMC_8_Problems_and_Solutions'


headers = {
	"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Brave Chrome/86.0.4240.198 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="mw-content-text").get_text()


def AMC_MAIN():
    if AMC_YR > 1998:
        URL2 = "https://artofproblemsolving.com/wiki/index.php/" + str(status) + "_AMC_8"
    elif AMC_YR < 1999:
        URL2 = "https://artofproblemsolving.com/wiki/index.php/" + str(status) + "_AJHSME"

    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Brave Chrome/86.0.4240.198 Safari/537.36'}
    page = requests.get(URL2, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title2 = soup.find(id="mw-content-text").get_text()

    AMC_PT = random.randint(1, 25)
    AMC_P = "Problem " + str(AMC_PT)

    if AMC_P in title2:
        problem_URL = URL2 + "_Problems/Problem_" + str(AMC_PT)
        print(problem_URL)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('mrsquinker@gmail.com', 'prvhmyalwnxxbzne')

    subject = 'Your Daily AMC 8 Problem!'
    body = 'Here it is: ' + str(problem_URL)

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('mrsquinker@gmail.com', 'andersharoldson@icloud.com', msg)
    print("Email Has Gone Though")

    server.quit()



AMC_MAIN()
