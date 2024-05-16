
from jinja2 import Environment, PackageLoader, select_autoescape
from jinja2 import PackageLoader
import yaml
from .problem import Problem

env = Environment(
    loader=PackageLoader(__name__),
    autoescape=select_autoescape()
)

class AssignmentManager:
    def __init__(self):
        self.assignments = self.read_assignments()

    def render_template(self, path, **kwargs):
        t = env.get_template(path)
        return t.render(**kwargs)

    def read_assignments(self):
        return {a['id']: a for a in yaml.safe_load(open("assignments.yml"))}

    def get_problems(self, assignment: int):
        names = self.assignments[assignment]['problems']
        return [Problem.find(name) for name in names]

    def render_solutions(self, assignment: int):
        title = f"Assignment {assignment:02d}"
        problems = self.get_problems(assignment)
        qmd = self.render_template(
                    "solution.md",
                    title=title,
                    problems=problems)

        path = f"assignment-{assignment:02d}.qmd"
        with open(path, "w") as f:
            f.write(qmd)
        print("Generated", path)