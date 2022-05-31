import g_manager
from g_object import GBall, GBar, GObject
import lg_object
class Script:
    mBallGroup = []
    mFPS = 0
    def init(self):
        self.mFPS = 30
        g_manager.GraphicManager.getInstance().init(500,500)
        obj = lg_object.LgObjectBuilder.createBall(0,[100.0,100.0,0],20,[100,100,100],[50.0,50.0,0],50)
        self.mBallGroup.append(obj)
        g_manager.GraphicManager.getInstance().addObject(GBall(obj))
        obj = lg_object.LgObjectBuilder.createBar(1,[5.0,0.0,0],[5.0,500.0,0],10,[180,200,40],50)
        g_manager.GraphicManager.getInstance().addObject(GBar(obj))

    def update(self):
        for ball in self.mBallGroup:
            ball.run(1/self.mFPS)

    def draw(self):
        g_manager.GraphicManager.getInstance().run(self.mFPS)
    
    def destroy():
        pass