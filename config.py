outputdir = "/datadrive/http"
texturepath = "/datadrive/resource_packs/MYTHIC+-+1.15.zip"
worlds["Mordor"] = "/datadrive/worldstorage/world/"

def signFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        return "\n".join([poi['Text1'], poi['Text2'], poi['Text3'], poi['Text4']])

def chestFilter(poi):
    if poi['id'] == "Chest" or poi['id'] == 'minecraft:chest':
        return "Chest with %d items" % len(poi.get('Items', []))

markers = [
    dict(name="Chests", filterFunction=chestFilter),
    dict(name="Signs", filterFunction=signFilter),
]

renders["Normal"] = {
    "world": "Mordor",
    "title": "Overworld",
    "rendermode": "smooth_lighting",
    "dimension": "overworld",
    "markers" : markers
}
renders["Cave"] = {
    "world": "Mordor",
    "title": "Caves",
    "rendermode": "cave",
    "dimension": "overworld",
    "markers" : markers
}
renders["Nether"] = {
    "world": "Mordor",
    "title": "Nether",
    "rendermode": "nether_smooth_lighting",
    "dimension": "nether",
    "markers" : markers
}
