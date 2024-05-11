from celery import shared_task


@shared_task(name='c_celery_teste', queue='fast')
def celery_teste(id):
    print(id)
    print('aaaaaaaaaaaaaaaaaaa')
