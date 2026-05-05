
# Class
class SceneManager:

    PLAYING: int = 0
    MENU: int = 1

    scene: int = MENU

    def get_scene(self) -> int:
        return self.scene
    def set_scene(self, scene: int):
        self.scene = scene