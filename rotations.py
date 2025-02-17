# library of all the rotations possible that i will need

def rotatefaceFP(face):
    # Rotates a given 3x3 face of a Rubik's cube 90 degrees clockwise.
    # Args:
    #     face (list of list of str): A 3x3 matrix representing a face of the Rubik's cube.
    # Returns:
    #     list of list of str: The rotated 3x3 matrix.
    temp = face[0][0]
    face[0][0] = face[0][2]
    face[0][2] = face[2][2]
    face[2][2] = face[2][0]
    face[2][0] = temp
    temp = face[0][1]
    face[0][1] = face[1][2]
    face[1][2] = face[2][1]
    face[2][1] = face[1][0]
    face[1][0] = temp
    return face

def rotatefaceF(face):
    face = rotatefaceF2(rotatefaceFP(face))
    return face

def rotatefaceF2(face):
    face = rotatefaceFP(rotatefaceFP(face))
    return face

#F
def rotateF(cube):
    cube = rotateF2(rotateFP(cube))
    return cube

#F'
def rotateFP(cube):
    cube[2] = rotatefaceF(cube[2])
    temp = ""
    for i in range(3):
        temp = cube[0][i][2]
        cube[0][i][2] = cube[3][0][i]
        cube[3][0][i] = cube[4][2-i][0]
        cube[4][2-i][0] = cube[1][2][2-i]
        cube[1][2][2-i]= temp
    return cube

#F2
def rotateF2(cube):
    cube = rotateFP(rotateFP(cube))
    return cube

#R
def rotateR(cube):
    rotateY(cube)
    rotateF(cube)
    rotateYP(cube)
    return cube

#R2
def rotateR2(cube):
    return rotateR(rotateR(cube))

#R'
def rotateRP(cube):
    return rotateR(rotateR2(cube))

#D
def rotateD(cube):
    rotateX(cube)
    rotateF(cube)
    rotateXP(cube)
    return cube

#D2
def rotateD2(cube):
    return rotateD(rotateD(cube))

#D'
def rotateDP(cube):
    return rotateD(rotateD2(cube))

#L
def rotateL(cube):
    rotateYP(cube)
    rotateF(cube)
    rotateY(cube)
    return cube

#L2
def rotateL2(cube):
    return rotateL(rotateL(cube))

#L'
def rotateLP(cube):
    return rotateL(rotateL2(cube))

#U
def rotateU(cube):
    rotateXP(cube)
    rotateF(cube)
    rotateX(cube)
    return cube

#U2
def rotateU2(cube):
    return rotateU(rotateU(cube))

#U'
def rotateUP(cube):
    return rotateU(rotateU2(cube))

#B
def rotateB(cube):
    rotateY2(cube)
    rotateF(cube)
    rotateY2(cube)
    return cube

#B2
def rotateB2(cube):
    return rotateB(rotateB(cube))

#B'
def rotateBP(cube):
    return rotateB(rotateB2(cube))

#M
def rotateM(cube):
    rotateR(cube)
    rotateLP(cube)
    rotateXP(cube)
    return cube

#M2
def rotateM2(cube):
    return rotateM(rotateM(cube))

#M'
def rotateMP(cube):
    return rotateM(rotateM2(cube))

#E
def rotateE(cube):
    rotateU(cube)
    rotateDP(cube)
    rotateYP(cube)
    return cube

#E2
def rotateE2(cube):
    return rotateE(rotateE(cube))

#E'
def rotateEP(cube):
    return rotateE(rotateE2(cube))

#S'
def rotateSP(cube):
    rotateF(cube)
    rotateBP(cube)
    rotateZP(cube)
    return cube

#S
def rotateS(cube):
    return rotateSP(rotateS2(cube))

#S2
def rotateS2(cube):
    return rotateSP(rotateSP(cube))
#x
def rotateX(cube):
    temp = rotatefaceF2(cube[0].copy())
    cube[0] = cube[2]
    cube[2] = cube[4]
    cube[4] = rotatefaceF2(cube[5])
    cube[5] = temp
    cube[1] = rotatefaceF(cube[1])
    cube[3] = rotatefaceFP(cube[3])
    return cube

#x'
def rotateXP(cube):
    return rotateX(rotateX2((cube)))

#x2
def rotateX2(cube):
    return rotateX(rotateX(cube))

#y'
def rotateY(cube):
    temp = cube[1].copy()
    cube[1] = cube[2]
    cube[2] = cube[3]
    cube[3] = cube[5]
    cube[5] = temp
    cube[0] = rotatefaceFP(cube[0])
    cube[4] = rotatefaceF(cube[4])
    return cube

#f
def rotatef(cube):
    rotateF(cube)
    rotateS(cube)
    return cube

#f'
def rotatefp(cube):
    rotateFP(cube)
    rotateSP(cube)
    return cube

#f2
def rotatef2(cube):
    rotateF2(cube)
    rotateS2(cube)
    return cube

#u
def rotateu(cube):
    rotateU(cube)
    rotateEP(cube)
    return cube

#u'
def rotateup(cube):
    rotateUP(cube)
    rotateE(cube)
    return cube

#u2
def rotateu2(cube):
    rotateU2(cube)
    rotateE2(cube)
    return cube

#d
def rotated(cube):
    rotateD(cube)
    rotateE(cube)
    return cube

#d'
def rotatedp(cube):
    rotateDP(cube)
    rotateEP(cube)
    return cube

#d2
def rotated2(cube):
    rotateD2(cube)
    rotateE2(cube)
    return cube

#r
def rotater(cube):
    rotateR(cube)
    rotateMP(cube)
    return cube

#r'
def rotaterp(cube):
    rotateRP(cube)
    rotateM(cube)
    return cube

#r2
def rotater2(cube):
    rotateR2(cube)
    rotateM2(cube)
    return cube

#l
def rotatel(cube):
    rotateL(cube)
    rotateM(cube)
    return cube

#l'
def rotatelp(cube):
    rotateLP(cube)
    rotateMP(cube)
    return cube

#l2
def rotatel2(cube):
    rotateL2(cube)
    rotateM2(cube)
    return cube

#b
def rotateb(cube):
    rotateB(cube)
    rotateSP(cube)
    return cube

#b'
def rotatebp(cube):
    rotateBP(cube)
    rotateS(cube)
    return cube

#b2
def rotateb2(cube):
    rotateB2(cube)
    rotateS2(cube)
    return cube

#y'
def rotateYP(cube):
    return rotateY(rotateY2((cube)))

#y2
def rotateY2(cube):
    return rotateY(rotateY(cube))

#z'
def rotateZP(cube):
    return rotateX(rotateY(rotateXP(cube)))

#z
def rotateZ(cube):
    return rotateZP(rotateZ2((cube)))

#z2
def rotateZ2(cube):
    return rotateZP(rotateZP(cube))