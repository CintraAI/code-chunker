from dataclasses import dataclass
from typing import Dict

@dataclass
class CodeChunkerInput:
    """
    A dataclass representing input for the code chunker.
    
    Attributes:
        files (Dict[str, str]): A dictionary mapping file names to their content as strings
        token_limit (int): The maximum number of tokens allowed per chunk
    """
    files: Dict[str, str]
    token_limit: int