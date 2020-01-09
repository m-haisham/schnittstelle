from schnittstelle.loader.style import LoaderStyle
from schnittstelle import Loader, RunnableLoader, Completer

if __name__ == '__main__':
    with Completer('complete') as c:
        c.complete()

    with Completer('fail') as c:
        c.fail()
