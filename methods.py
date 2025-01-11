"""
this script contains methods for random photo selection
"""

import os, random

# this function compiles the gallery from the 'CatImages' directory
def compileGallery() -> list[str]:
    files: list = os.listdir("CatImages")
    return [f for f in files if f.lower().endswith('jpeg')]

# this function returns a single photo from the gallery
def selectPhoto(gallery: list[str]) -> str:
    return random.choice(gallery)

# this function returns a sample of the gallery for a given number of photos
def selectMultiplePhotos(gallery: list[str], num: int) -> list[str]:
    # if the number of images exceeds the gallery size, a single photo is returned instead
    if num > len(gallery):
        print("This sample size is too large! Returning a single photo.")
        return random.sample(gallery, 1)
    else:
        return random.sample(gallery, num)