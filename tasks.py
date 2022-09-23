from invoke import task

"""komento: poetry run invoke _task_"""

@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)

@task
def ui(ctx):
    ctx.run("python3 src/ui.py", pty=True)

@task
def test(ctx):
    ctx.run("pytest src", pty=True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)

@task
def lint(ctx):
    ctx.run("pylint src", pty=True)

@task
def format(ctx):  # pylint: disable=redefined-builtin
    ctx.run("autopep8 --in-place --recursive src", pty=True)