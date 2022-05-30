import g_manager
class Script:
    def init(self):
        g_manager.GraphicManager.getInstance().init(500,500)
    def update(self):
        pass
    def draw(self):
        g_manager.GraphicManager.getInstance().run()
    def destroy():
        pass