import g_object
import pygame
class GraphicManager:
    __instance = None
    mSurface : pygame.Surface = None
    mObjectMap = {}
    
    def init(self,width_ : int,height_ : int):
        self.mSurface = pygame.display.set_mode([width_,height_])
    
    def addObject(self,Obj : g_object.GObject):
        self.mObjectMap[Obj.mID] = Obj
    
    def rmObject(self,Obj: g_object.GObject):
        self.mObjectMap.pop(Obj.mID,'rmObject: Not found key {}'.format(Obj.mID))
    
    def run(self):
        self.mSurface.fill((255, 255, 255))
        for e in self.mObjectMap.values():
            e.draw()
        pygame.display.flip()

    def __init__(self) -> None:
        if GraphicManager.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            pygame.init()
            GraphicManager.__instance = self

    def __del__(self) -> None:
        pygame.quit()
        
    @staticmethod
    def getInstance():
        if GraphicManager.__instance == None:
            GraphicManager()
        return GraphicManager.__instance
