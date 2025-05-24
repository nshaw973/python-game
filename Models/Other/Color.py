import random

class Color:
    """ANSI color codes for terminal text styling."""

    @staticmethod
    def cyan(text: str) -> str:
        return f"\033[36m{text}\033[0m"
    
    @staticmethod
    def magenta(text: str) -> str:
        return f"\033[1;35m{text}\033[0m"
    
    @staticmethod
    def green(text: str) -> str:
        return f"\033[32m{text}\033[0m"
    
    @staticmethod
    def yellow(text: str) -> str:
        return f"\033[33m{text}\033[0m"
    
    @staticmethod
    def red(text: str) -> str:
        return f"\033[31m{text}\033[0m"
    
    @staticmethod
    def blue(text: str) -> str:
        return f"\033[34m{text}\033[0m"
    
    @staticmethod
    def random(text: str) -> str:
        """Applies a random ANSI text color."""
        colors = [
            31,  # Red
            32,  # Green
            33,  # Yellow
            34,  # Blue
            35,  # Magenta
            36,  # Cyan
        ]
        code = random.choice(colors)
        return f"\033[{code}m{text}\033[0m"
                
