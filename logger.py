import datetime, os

def log(message : str, name : str = 'log', path : str = os.getcwd()):
    if not message:
        raise ValueError('message is required')
    with open(os.path.join(path, name), 'a') as fh:
        fh.write(f'{datetime.datetime.now().strftime("%Y/%m/%d-%H:%M")} - {message}')


if __name__ == '__main__':
    log('test')
