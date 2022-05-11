from scraping import Scraping
from settings import TOKEN,USERNAME

def main():
    s = Scraping(username=USERNAME, token=TOKEN)
    repo_list = s.get_org_repos()
    s.to_csv(repo_list, 'repos')
    issue_list = s.get_repo_issues()
    s.to_csv(issue_list, 'issues')

if __name__ == "__main__":
    main()
