from invoke import task


@task
def clean(c):
    """
    Clean build artifacts.
    """
    c.run('rm -rf build')
    c.run('rm -rf dist')
    c.run('rm -rf src/*.egg-info')


@task(pre=[clean])
def publish(c):
    """
    Publish python artifact.
    """
    c.run('devpi upload')
