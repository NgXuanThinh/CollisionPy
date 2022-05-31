class LgObject:
    mID  = -1
    def update(self,data):
        pass
    def run(self,time):
        pass

class lgBar(LgObject):
    #variable
    class Properties:
        mStartPoint = []
        mEndPoint = []
        mWidth = 0
        mColor = []
        mMass = 0.0
    mProperties : Properties = None
    #end_variable
    def __init__(self,id) -> None:
        super().__init__()
        self.mID = id

    def update(self,data):
        self.mProperties = data

    def run(self,time):
        pass

class lgBall(LgObject):
    #variable
    class Properties:
        mCenter = []
        mRadius = 0
        mColor = []
        mSpeed = []
        mMass = 0.0
    mProperties : Properties = None
    #end_variable
    def __init__(self,id) -> None:
        super().__init__()
        self.mID = id

    def update(self,data):
        self.mProperties = data

    def run(self,time):
        self.mProperties.mCenter = [self.mProperties.mCenter[i] + time*self.mProperties.mSpeed[i] for i in range(0,len(self.mProperties.mSpeed))]

class LgObjectBuilder:
    def createBar(id, startPoint, endPoint, width, color, mass)->lgBall:
        properties = lgBar.Properties()
        properties.mStartPoint = startPoint
        properties.mEndPoint = endPoint
        properties.mWidth = width
        properties.mColor = color
        properties.mMass = mass
        bar = lgBar(id)
        bar.update(properties)
        return bar

    def createBall(id, center, radius, color, speed, mass)->lgBall:
        properties = lgBall.Properties()
        properties.mCenter = center
        properties.mRadius = radius
        properties.mColor = color
        properties.mSpeed = speed
        properties.mMass = mass
        ball = lgBall(id)
        ball.update(properties)
        return ball
