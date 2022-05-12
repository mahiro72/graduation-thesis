
from cProfile import label


class Scraping:

    headers = {
        'Accept': 'application/vnd.github.v3+json'
    }


    def __init__(self, username : str, token : str) -> None:
        self.username = username
        self.token = token


    # csvを開き、リストにして返す
    def read_csv(self, path: str, col: str) -> list:
        import pandas as pd
        orgs_csv = pd.read_csv(path)
        return orgs_csv[col].to_list()


    # csvへの書き込み
    def to_csv(self, data : list, name : str):
        import pandas as pd
        df = pd.DataFrame(data)
        df.to_csv(f'../data/{name}.csv')
        print(f"Write {name}.csv success!\nCheck the data/{name} directory.\n")


    # リポジトリの取得
    def get_org_repos(self) -> list:
        import requests

        orgs = self.read_csv('../data/orgs.csv', 'org')
        repos = []
        for org in orgs:
            url = f'https://api.github.com/orgs/{org}/repos?access_token={self.token}'
            org_res = requests.get(
                url, 
                headers=self.headers,
                auth=requests.auth.HTTPBasicAuth(self.username, self.token)
                ).json()

            if not self.valid_response(res=org_res):
                print(f"ERROR : Validate or Request Failed\nCheck the {org} organization.\n")
                continue

            for repo in org_res:
                repos.append({
                    'name': repo['full_name'],
                    'url': repo['url'],
                })

        return repos


    # issueの取得
    def get_repo_issues(self) -> list:
        import requests

        urls = self.read_csv('../data/repos.csv', 'url')
        issues = []
        for url in urls:
            repo_res = requests.get(
                url, 
                headers=self.headers,
                auth=requests.auth.HTTPBasicAuth(self.username, self.token)
                ).json()
            if not self.valid_response(res=repo_res):
                print("ERROR : Validate or Request Failed\n")
                continue

            if repo_res['open_issues_count'] == 0:
                continue

            issue_url = f'{url}/issues'
            issue_res = requests.get(
                issue_url, 
                headers=self.headers,
                auth=requests.auth.HTTPBasicAuth(self.username, self.token)
                ).json()

            if not self.valid_response(res=repo_res):
                print("ERROR : Validate or Request Failed\n")
                continue

            for issue in issue_res:
                labels = issue['labels']
                if len(labels) == 0:
                    issues.append({
                        'title': issue['title'],
                        'body': issue['body'],
                        'label':None
                    })
                else:
                    for label in labels:
                        issues.append({
                            'title': issue['title'],
                            'body': issue['body'],
                            'label':label
                        })


        return issues


    # レスポンスのvalidate
    def valid_response(self, res) -> bool:
        if isinstance(res, dict) and 'message' in res.keys():
            return False
        return True
