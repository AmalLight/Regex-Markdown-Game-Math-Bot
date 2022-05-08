
def getv( maps, x,y ):
    bx = x >= 0 and x < maps.n
    by = y >= 0 and y < maps.n
    if bx and by: return maps.Value[ x ][ y ]
    return None
    
def getxy( maps, v ):
    for x in range( maps.n ):
        for y in range( maps.n ):
            if getv( maps, x,y ) == v: return [x,y]
    return None
