init python:
    #DefineImages('images/sprites', composite=True, offsets=(0, 100), zooms={'mc':0.5, 'le': 1.3, 'ju':1.3}, sides=['mc', 'le', 'ju'])
    DefineImages('images/sprites', composite=True,
        overrideLayerOrder=['base','mouth','eyes','brow'],
        offsets=(0, 50),
        zooms=1.5,
        # sides=['mc', 'le', 'ju'],
    )

    DefineImages('images/bgs', prepend='bg')
