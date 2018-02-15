import pygal

# wm = pygal.maps.world.World()
# wm.title = 'North, Central, and South America'
#
# wm.add('North America', ['ca', 'mx', 'us'])
# wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
# wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
#     'gy', 'pe', 'py', 'sr', 'uy', 've'])
#
# wm.render_to_file('americas.svg')


wm = pygal.maps.world.World()
wm.title = 'Populations of Countries in North America'
wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})

wm.render_to_file('na_populations.svg')
