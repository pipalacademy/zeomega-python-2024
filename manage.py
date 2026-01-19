from sigma.assignment import AssignmentManager
from sigma import config

config.PROBLEM_REPOSITORY_PATH = "problems"

m = AssignmentManager()
m.render_solutions(3)
m.render_solutions(4)