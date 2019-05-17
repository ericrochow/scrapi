from __future__ import absolute_import, unicode_literals

import requests

import utils

from .__version__ import __title__, __version__


class Github(object):
    def __init__(self, timeout=30, verify_cert=True, raise_on_error=True):
        """
        """
        self.something = utils.GlobalUtils()
        self.github_config = self.something.full_config["github"]
        self.username = self.github_config["username"]
        self.logger = self.something.handler
        self.base_url = "https://api.github.com"
        self.timeout = timeout
        self.verify = verify_cert
        self.raise_on_error = raise_on_error
        self.headers = {
            "Accept": "application/vnd.github.v3+json",
            "Content-Type": "application/json",
            "User-Agent": f"{__title__}/{__version__}",
        }
        self.sess = requests.Session()

    def _get(self, request):
        """
        """
        url = f"{self.base_url}/{request}"
        resp = self.sess.get(
            url,
            headers=self.headers,
            auth=self.creds,
            timeout=self.timeout,
            verify=self.verify,
        )
        if resp.ok:
            return resp.json()
        else:
            resp.raise_for_status()

    def get_commits(self, user):
        """
        """
        request = f"/users/{self.username}/events"
        return self._get(request)


if __name__ == "__main__":
    print(__name__)
