d1={'fruit':'apple', 'climate':'cold', 'color':'pink'}
print("d1=",d1)
d2={'x':'100', 'y':'200'}
print("d2=",d2)
d=d1.copy()
d.update(d2)
print("merged dictionaries=",d)
