from dataclasses import dataclass

@dataclass(eq=True)
class Saint:
    name: str
    feastday: str
    content: str

