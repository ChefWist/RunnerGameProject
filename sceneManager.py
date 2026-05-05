
# Class
class SceneManager:

    PLAYING: int = 0
    MENU: int = 1

    scene: int = 0

    def get_scene(self) -> int:
        return self.scene