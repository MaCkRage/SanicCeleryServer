from celerybeat import task


@task
def add_together(a, b):
    return a + b
