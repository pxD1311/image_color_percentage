from config import COLOR_RANGES

class Pixel:
    def __init__(self, rgba : tuple) -> None:
        self.rgb = rgba[:-1]
        self.opacity = rgba[-1]*100/255
        self.color = self.__clamp()

    def __clamp(self) -> str:
        for color_name,color_range in COLOR_RANGES.items():
            if (color_range[0][0] <= self.rgb[0] <= color_range[1][0] and
                color_range[0][1] <= self.rgb[1] <= color_range[1][1] and
                color_range[0][2] <= self.rgb[2] <= color_range[1][2]):
                return color_name
        return "None"

    def __str__(self) -> str:
        return f"Pixel[Color = {self.color}, RGB = {self.rgb},Opacity = {self.opacity}]"