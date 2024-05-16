import yaml
import nbformat as nbf
from pathlib import Path
import markdown
from . import config


class Problem:
    def __init__(self, name, metadata):
        self.name = name
        self.metadata = metadata
        self.title = self.metadata['title']
        self.root = Path(config.PROBLEM_REPOSITORY_PATH) / name

        self.problem_type = metadata.get("problem_type")
        self.script_name = metadata.get("script_name")

    @classmethod
    def find(cls, name):
        path = Path(config.PROBLEM_REPOSITORY_PATH) / name / "problem.yml"
        metadata = yaml.safe_load(path.open())
        return cls(name, metadata)

    def open(self, path):
        return self.joinpath(path).open()

    def joinpath(self, path):
        p = self.root / path
        return p

    def get_description(self):
        return self.open("description.md").read()

    def get_initial_code(self):
        files = self.metadata['files'].get('code', [])
        if files:
            return self.open(files[0]).read()

    def get_description_html(self):
        desc = self.get_description()
        return self.markdown(desc)


    def get_solution(self):
        solution_file = self.metadata['files']['solution'][0]
        path = self.root / solution_file
        return path.read_text()

    def get_discussion(self):
        path = self.root / "solution" / "discussion.md"
        return path.read_text() if path.exists() else ""

    def markdown(self, text):
        return markdown.markdown(text, extensions=['fenced_code'])

