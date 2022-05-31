import pygame
import lg_object
class GObject:
    mID : int = -1
    mHost = None
    def type(self)->int:
        pass
    def draw(self,suf : pygame.Surface):
        pass

class GBar(GObject):
    def __init__(self,host: lg_object.lgBar) -> None:
        super().__init__()
        self.mHost = host
        self.mID = host.mID

    def type(self)->int:
        return 'G_BAR'

    def draw(self,surf : pygame.Surface):
        data = self.mHost.mProperties
        start_pos = [data.mStartPoint[0], data.mStartPoint[1]]
        end_pos = [data.mEndPoint[0], data.mEndPoint[1]]
        pygame.draw.line(surf,data.mColor,start_pos,end_pos,data.mWidth)

class GBall(GObject):
    def __init__(self,host: lg_object.lgBall) -> None:
        super().__init__()
        self.mHost = host
        self.mID = host.mID
        
    def type(self)->int:
        return 'G_BALL'

    def draw(self,surf : pygame.Surface):
        data = self.mHost.mProperties
        pygame.draw.circle(surf,data.mColor,[data.mCenter[0],data.mCenter[1]],data.mRadius)