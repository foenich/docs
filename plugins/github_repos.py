import json
import os
import time
import logging
from datetime import datetime
from pathlib import Path

import requests
from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options

logger = logging.getLogger("mkdocs.plugins.github_repos")

class GitHubReposPlugin(BasePlugin):
    config_scheme = (
        ('organization', config_options.Type(str, default='PPUC')),
        ('cache_minutes', config_options.Type(int, default=60)),
        ('github_token', config_options.Type(str, default='')),
        ('exclude_repos', config_options.Type(list, default=[])),
        ('include_archived', config_options.Type(bool, default=False)),
        ('forked_repos', config_options.Type(list, default=[])),
    )

    def __init__(self):
        super().__init__()
        self.cache_dir = Path("data/github_cache")
        self.repos_cache_file = self.cache_dir / "repos.json"
        self.releases_cache_file = self.cache_dir / "releases.json"
        self.cache = {
            'repos': {},
            'releases': {}
        }
        self.load_cache()

    def on_page_markdown(self, markdown, page, config, files):
        if 'github_repos.md' in page.file.src_path:
            try:
                return self.generate_repos_markdown()
            except Exception as e:
                logger.error(f"Failed to generate GitHub repos markdown: {str(e)}")
                return "## GitHub Repositories\n\n⚠️ Failed to load repository data. Please try again later."
        return markdown

    def generate_repos_markdown(self):
        repos = self.get_organization_repos()

        if not repos:
            return "## GitHub Repositories\n\nNo repositories found."

        # Split into main and forked repositories
        main_repos = []
        forked_repos = []

        for repo in repos:
            if repo['name'] in self.config['forked_repos']:
                forked_repos.append(repo)
            elif repo['name'] not in self.config['exclude_repos']:
                main_repos.append(repo)

        markdown = "## PPUC Repositories\n\n"

        # Main repositories section
        if main_repos:
            markdown += "<div class=\"github-repos\">\n\n"
            for repo in sorted(main_repos, key=lambda x: x['name'].lower()):
                markdown += self.generate_repo_card(repo)
            markdown += "</div>\n\n"
        else:
            markdown += "<p>No main repositories found.</p>\n\n"

        # Forked repositories section (only if there are any)
        if forked_repos:
            markdown += "## Forked Repositories with adjustments for PPUC\n\n"
            markdown += "We always try to get the adjustmens merged into the upstream repositories. But to ease the installtions, we sometimes provide preview builds.\n\n"
            markdown += "<div class=\"github-repos forked-repos\">\n\n"
            for repo in sorted(forked_repos, key=lambda x: x['name'].lower()):
                markdown += self.generate_repo_card(repo, is_forked=True)
            markdown += "</div>\n"

        return markdown

    def generate_repo_card(self, repo, is_forked=False):
        archived = repo.get('archived', False)
        card_classes = ["github-repo-card"]
        if archived:
            card_classes.append("archived")
        if is_forked:
            card_classes.append("forked")

        card = (
            f"<div class=\"{' '.join(card_classes)}\">\n"
            f"  <h3><a href=\"{repo['html_url']}\">{repo['name']}</a></h3>\n"
            f"  <p class=\"repo-description\">{repo['description'] or '<em>No description</em>'}</p>\n"
        )

        # Add stats if available
        if repo.get('stargazers_count', 0) > 0 or repo.get('forks_count', 0) > 0:
            card += (
                f"  <div class=\"repo-stats\">\n"
                f"    <span class=\"stars\">⭐ {repo['stargazers_count']}</span>\n"
                f"    <span class=\"forks\">⑂ {repo.get('forks_count', 0)}</span>\n"
            )
            if is_forked:
                card += f"    <span class=\"fork-flag\">Fork</span>\n"
            card += "  </div>\n"

        # Add release info if available
        if repo.get('latest_release'):
            release = repo['latest_release']
            date = datetime.strptime(release['published_at'], '%Y-%m-%dT%H:%M:%SZ').strftime('%b %d, %Y')
            card += (
                f"  <div class=\"github-repo-release\">\n"
                f"    <strong>Latest Release:</strong>\n"
                f"    <a href=\"{release['html_url']}\">{release['tag_name']}</a>\n"
                f"    <span class=\"release-date\">({date})</span>\n"
                f"  </div>\n"
            )
        else:
            card += "  <div class=\"github-repo-release\">No releases yet</div>\n"

        card += "</div>\n\n"
        return card

    def get_organization_repos(self):
        return self.get_cached_data(
            key='repos',
            fetch_fn=self.fetch_organization_repos,
            cache_file=self.repos_cache_file
        )

    def fetch_organization_repos(self):
        headers = self.get_request_headers()
        url = f"https://api.github.com/orgs/{self.config['organization']}/repos"
        repos = []

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            raw_repos = response.json()

            for repo in raw_repos:
                if repo['archived'] and not self.config['include_archived']:
                    continue

                release_info = self.get_latest_release(repo['name'])
                repos.append({
                    'name': repo['name'],
                    'description': repo['description'],
                    'html_url': repo['html_url'],
                    'stargazers_count': repo['stargazers_count'],
                    'forks_count': repo['forks_count'],
                    'archived': repo['archived'],
                    'latest_release': release_info
                })
        except requests.RequestException as e:
            logger.error(f"Failed to fetch GitHub repos: {str(e)}")
            if self.cache['repos'].get('data'):
                logger.warning("Using cached repository data")
                return self.cache['repos']['data']
            raise

        return repos

    def get_latest_release(self, repo_name):
        return self.get_cached_data(
            key=f"release_{repo_name}",
            fetch_fn=lambda: self.fetch_latest_release(repo_name),
            cache_file=self.releases_cache_file
        )

    def fetch_latest_release(self, repo_name):
        headers = self.get_request_headers()
        url = f"https://api.github.com/repos/{self.config['organization']}/{repo_name}/releases/latest"

        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return response.json()
            return None
        except requests.RequestException as e:
            logger.error(f"Failed to fetch release for {repo_name}: {str(e)}")
            return None

    def get_request_headers(self):
        headers = {'Accept': 'application/vnd.github.v3+json'}
        if self.config['github_token']:
            headers['Authorization'] = f"token {self.config['github_token']}"
        return headers

    def get_cached_data(self, key, fetch_fn, cache_file):
        if key in self.cache[cache_file.stem] and not self.is_cache_expired(self.cache[cache_file.stem][key]):
            return self.cache[cache_file.stem][key]['data']

        if cache_file.exists():
            with open(cache_file) as f:
                disk_cache = json.load(f)
                if key in disk_cache and not self.is_cache_expired(disk_cache[key]):
                    self.cache[cache_file.stem][key] = disk_cache[key]
                    return disk_cache[key]['data']

        data = fetch_fn()
        self.cache[cache_file.stem][key] = {
            'timestamp': time.time(),
            'data': data
        }
        self.save_cache(cache_file)
        return data

    def is_cache_expired(self, cache_entry):
        if not cache_entry or 'timestamp' not in cache_entry:
            return True
        return (time.time() - cache_entry['timestamp']) > (self.config['cache_minutes'] * 60)

    def load_cache(self):
        if self.repos_cache_file.exists():
            with open(self.repos_cache_file) as f:
                self.cache['repos'] = json.load(f)
        if self.releases_cache_file.exists():
            with open(self.releases_cache_file) as f:
                self.cache['releases'] = json.load(f)

    def save_cache(self, cache_file):
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        with open(cache_file, 'w') as f:
            json.dump(self.cache[cache_file.stem], f)
