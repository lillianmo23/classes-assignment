class AshleyFruitNinja:
    def __init__(self, screen_width: int, screen_height: int) -> None:
        self.set_screen_width(screen_width)
        self.set_screen_height(screen_height)
        self.total_score = 0
    
    def get_screen_width(self) -> int:
        return self.screen_width
    
    def set_screen_width(self, screen_width: int) -> None:
        if screen_width <= 0:
            raise ValueError("Screen width cannot be set to 0 or less.")
        self.screen_width = screen_width
    
    def get_screen_height(self) -> int:
        return self.screen_height

    def set_screen_height(self, screen_height: int) -> None:
        if screen_height <= 0:
            raise ValueError("Screen height cannot be set to 0 or less.")
        self.screen_height = screen_height
    
    def get_total_score(self) -> int:
        return self.total_score

    def set_total_score(self, score_to_add) -> None:
        self.total_score += score_to_add
