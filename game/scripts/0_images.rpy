init python:
    #DefineImages('images/sprites', composite=True, offsets=(0, 100), zooms={'mc':0.5, 'le': 1.3, 'ju':1.3}, sides=['mc', 'le', 'ju'])
    DefineImages('images/sprites', composite=True,
        overrideLayerOrder=['base','mouth','eyes','brow'],
        offsets=(0, 50),
        zooms=1.5,
        # sides=['mc', 'le', 'ju'],
    )

    DefineImages('images/bgs', prepend='bg')

layeredimage bg_sky:
    group base:
        attribute day default:
            "bg sky_day"
        attribute night:
            "bg sky_night"

    group snowing:
        attribute lightsnow:
            "bg snow_day"
        attribute darksnow:
            "bg snow_night"

image bg apartmenthallway_grayscale = im.Grayscale("images/bgs/apartmenthallway.png")
image bg controlroom_grayscale = im.Grayscale("images/bgs/controlroom.png")