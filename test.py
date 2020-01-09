from schnittstelle.loader.style import LoaderStyle
from schnittstelle import Loader

if __name__ == '__main__':

    style = LoaderStyle.ascii()

    value = 0
    Loader()

    with Loader(style=style) as loader:
        while value < 500000000:
            if (value % 1000000) == 0:
                loader.brush.message = str(value)

            value += 1
