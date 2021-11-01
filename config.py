from PIL import Image


###################### CONFIG #######################

srcCombatImg = Image.open('./images/src/combat-src.png')
srcChestImg = Image.open('./images/src/chest-src.png')
srcStartImg = Image.open('./images/src/start-src.png')
srcCaveImg = Image.open('./images/src/cave-src.png')

# Positions of the screen to print the images to compare to src image
# The sumSquare is the level of likeleness between both images
statusPositions = [
    {
        "top": 370,
        "left": 650,
        "width": 620,
        "height": 390,
        "sumSquare": 1000000, 
        "name": "chest",
        "srcImage": srcChestImg
    },
    {
        "top": 270,
        "left": 430,
        "width": 1080,
        "height": 510,
        "sumSquare": 90000000,
        "name": "start",
        "srcImage": srcStartImg
    },
    {
        "top": 300,
        "left": 645,
        "width": 575,
        "height": 510,
        "sumSquare": 2571905302,
        "name": "combat",
        "srcImage": srcCombatImg
    },
    {
        "top": 305,
        "left": 580,
        "width": 750,
        "height": 600,
        "sumSquare": 1000000000,
        "name": "cave",
        "srcImage": srcCaveImg
    }
]

startPositions = [
    {
        "name": "detector",
        "pos": [500, 720],
    },
    {
        "name": "chest",
        "pos": [960, 560]
    }
]

combatPositions = {
    "posX": [750, 880, 1015],     # Columns
    "posY": [640, 670, 710, 750]  # Rows
}


# X Position on the screen of each of the 10 miners
minersX = [450, 540, 630, 715, 810, 905, 995, 1090, 1175, 1265]

# Y Position on the screen of miner (top row)
minersY = 350

# Chest position
cPos = [960, 560]

# Skip KM
skipKm = [-4, -3, -2, -1, 20, 45, 300, 301, 302, 303, 501]

# Chest storage space
storageSpace = 50

# Max KM
maxKm = 840

# Starting KM, if it starts from the top mining row, it should be 0
# If it starts from the surface, it should be -4
startAt = -4

#########################################################################