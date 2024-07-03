from celery import shared_task


@shared_task(name='c_celery_teste', queue='fast')
def celery_teste(id: int) -> int:
    """
    Tarefa Celery que recebe um ID e o retorna.

    Args:
        id (int): O ID a ser processado.

    Returns:
        int: O mesmo ID fornecido como entrada.
    """
    return id
