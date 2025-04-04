import rmscene


def get_types(block_class):
    base_classes = []
    try:
        print(f"{block_class.__name__} - {getattr(block_class, 'BLOCK_TYPE')}")
    except AttributeError:
        base_classes.append(block_class.__name__)
    for sub_block_class in block_class.__subclasses__():
        base_classes.extend(get_types(sub_block_class))
    return base_classes


if __name__ == "__main__":
    print('', *get_types(rmscene.Block), sep='\n')
