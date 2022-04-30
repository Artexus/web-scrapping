from bs4 import BeautifulSoup
import requests
from constant.variable import BASE_URL
import sys


def main():
    if len(sys.argv) <= 1:
        print("[ERROR] Missing Arguments")
        return

    username = sys.argv[1]
    base_profile = BASE_URL + '/' + username + '?tab=repositories'
    pages = requests.get(base_profile)
    if pages.status_code != 200:
        print("[ERROR] There is an error code: ", pages.status_code)
        return

    soup = BeautifulSoup(pages.content, 'html.parser')
    repo_list = soup.find(id='user-repositories-list')

    github_repo_element = repo_list.find_all(
        class_='col-10 col-lg-9 d-inline-block')

    github_title = []
    github_desc = []
    for element in github_repo_element:
        title = element.find("a")
        desc = element.find("p")

        if desc != None:
            desc = desc.get_text().strip()
        else:
            desc = "--There is no Description--"

        title = title.get_text().strip()

        github_title.append(title)
        github_desc.append(desc)
    print('REPO FOR ' + username + ":")
    for index, _ in enumerate(github_title):
        print("Title: " + github_title[index] +
              " Description: " + github_desc[index])
    pass


if __name__ == '__main__':
    main()
