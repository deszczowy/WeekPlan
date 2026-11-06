from PIL import ImageFont
from options import WrappingMethod, WRAPPING_METHOD_MAPPER


class Captions:

    def __init__(self, wrapping_method: WrappingMethod, font: str) -> None:
        self.method = wrapping_method
        self.font = font
    
    def get(self, caption: str, font_size: int, max_width: int) -> [str]:
        ufont = ImageFont.truetype(self.font, font_size)
        caption_width = ufont.getlength(caption)

        if caption_width < max_width:
            return[caption]
        else:
            if self.method == WrappingMethod.MULTILINE:
                return self._multiline(ufont, caption, max_width)
            if self.method == WrappingMethod.CUT:
                return self._cut(ufont, caption, max_width)
            if self.method == WrappingMethod.SHORT:
                return self._short(ufont, caption, max_width)

    def _multiline(self, font: ImageFont, text: str, limit_px: int) -> [str]:
        
        lines = []

        for p in text.splitlines() or [""]:
            words = p.split()
            line = ""

            for w in words:
                txt = f"{line} {w}".strip()

                if font.getlength(txt) <= limit_px:
                    line = txt
                    continue

                if line:
                    lines.append(line)
                    line = ""

                # split the word if exceedes the limit
                part = ""
                for char in w:
                    txt = part + char
                    if part and font.getlength(txt) > limit_px:
                        lines.append(part)
                        part = char
                    else:
                        part = txt

                line = part

            if line or not words:
                lines.append(line)

        return lines
    
    def _cut(self, font: ImageFont, text: str, limit_px: int) -> [str]:
        caption = self._get_part(font, text, limit_px)
        return [caption]

    def _short(self, font: ImageFont, text: str, limit_px: int) -> [str]:
        shortener = "..."
        shortener_len = font.getlength(shortener)
        part = self._get_part(font, text, limit_px - shortener_len)
        caption = "{0}{1}".format(part, shortener)
        return [caption]

    def _get_length(self, text: str, size: int) -> float:
        return ImageFont.truetype(self.font, size).getlength(text)
    
    def _get_part(self, font: ImageFont, text: str, limit: int) -> str:
        text_width = font.getlength(text)
        text_length = len(text)

        if text_width < limit:
            return text
        else:
            i = int((limit * text_length) / text_width)
            result = text[:i]
            
            while True:
                i += 1
                new_str = text[:i]
                if font.getlength(new_str) < limit:
                    result = new_str
                else:
                    break
            
            return result
