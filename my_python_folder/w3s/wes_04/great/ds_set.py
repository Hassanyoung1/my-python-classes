bri = set(['brazil', 'russia', 'india'])
'india' in bri
True
'usa' in bri
False
bric = bri.copy()
bric.add('china')
bri.issuperset(bri)
True
bri.remove('russia')
bri & bric

print('brazil', 'india')
