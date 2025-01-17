from invoke import task

from tasks.common import VENV_PREFIX


@task
def check_package(ctx):
    """Check package security"""
    ctx.run(f"{VENV_PREFIX} safety check", pty=True, warn=True)


@task
def bandit(ctx):
    """Check common software vulnerabilities through bandit"""
    ctx.run(
        f"{VENV_PREFIX} bandit -iii -lll -r . -f html -o tasks/bandit.report.html",
        pty=True,
        warn=True,
    )


@task(pre=[check_package, bandit], default=True)
def run(ctx):
    """Check security check throguh safety and bandit"""
    pass
