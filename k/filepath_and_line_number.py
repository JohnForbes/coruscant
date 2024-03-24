class FilepathAndLineNumber:
  def __init__(self, filepath: str, line_number: int) -> None:
    self.filepath = filepath
    self.line_number = line_number

  def __str__(self) -> str:
    return f"{self.filepath}:{self.line_number}"

  def __repr__(self) -> str:
    return f"FilepathAndLineNumber({self.filepath}, {self.line_number})"

  def __eq__(self, other: object) -> bool:
    if not isinstance(other, FilepathAndLineNumber): return False
    return all([
      self.filepath == other.filepath,
      self.line_number == other.line_number
    ])

  def __hash__(self) -> int:
    return hash((self.filepath, self.line_number))

f = lambda x: FilepathAndLineNumber(**x)
t = lambda: 1
