def pointCollision(Ax, Ay, Bx, By, Bwidth, Bheight):
    return (Ax >= Bx and Ax <= Bx + Bwidth) and (Ay >= By and Ay <= Ay <= By + Bheight)
    
def rectCollision(Ax, Ay, Awidth, Aheight, Bx, By, Bwidth, Bheight):
    return (Ax + Awidth > Bx) and (Ax < Bx + Bwidth) and (Ay + Aheight > By) and (Ay < By + Bheight)

def lineCollision(Alines, Bx, By, Bwidth, Bheight):
    for line in Alines:
        if rectCollision(line[0], line[1], line[2], line[3], Bx, By, Bwidth, Bheight):
            return line[4]
def cubePlayerCollision(player, cube):
    rightOfPlayer = player.vec2.pos[0]+player.size[0]
    bottomOfPlayer = player.vec2.pos[1]+player.size[1]
    rightOfCube = cube.vec2.pos[0] + cube.size[0]
    bottomOfCube = cube.vec2.pos[1] + cube.size[1]

    playerPushingcuberight = rightOfPlayer < cube.vec2.pos[0]+(cube.size[0]/2) and player.vec2.vel[0] > 0
    playerPushingcubeleft = player.vec2.pos[0] > cube.vec2.pos[0]+(cube.size[0]/2) and player.vec2.vel[0] < 0
    playerPushingcubedown = bottomOfPlayer < cube.vec2.pos[1]+(cube.size[1]/2) and player.vec2.vel[1] > 0
    playerPushingcubeup = player.vec2.pos[1] > cube.vec2.pos[1]+(cube.size[1]/2) and player.vec2.vel[1] < 0
    
    
    
    cubePushingplayerright = rightOfCube < player.vec2.pos[0]+(player.size[0]/2) and cube.vec2.vel[0] > 0
    cubePushingplayerleft = cube.vec2.pos[0] > player.vec2.pos[0]+(player.size[0]/2) and cube.vec2.vel[0] < 0
    cubePushingplayerup = cube.vec2.pos[1] > player.vec2.pos[1]+(player.size[1]/2) and cube.vec2.vel[1] < 0
    cubePushingplayerdown = bottomOfCube < player.vec2.pos[1]+(player.size[1]/2) and cube.vec2.vel[1] > 0
    
    if rectCollision(player.vec2.pos[0], player.vec2.pos[1], player.size[0], player.size[1], cube.vec2.pos[0], cube.vec2.pos[1], cube.size[0], cube.size[1]):
        if playerPushingcubeleft or playerPushingcuberight or cubePushingplayerright or cubePushingplayerleft:
            vandm = (player.vec2.vel[0] * player.weight) - (cube.vec2.vel[0] * cube.weight)
            m = player.weight + cube.weight
            cube.vec2.vel[0] = vandm / m
            player.vec2.vel[0] = vandm / m
        
        if playerPushingcubeup or playerPushingcubedown or cubePushingplayerdown or cubePushingplayerup:
            vandm = (player.vec2.vel[1] * player.weight) - (cube.vec2.vel[1] * cube.weight)
            m = player.weight + cube.weight
            cube.vec2.vel[1] = vandm / m
            player.vec2.vel[1] = vandm / m