from dataclasses import dataclass

@dataclass(eq=True)
class Prayer:
    name: str
    content: str
    
