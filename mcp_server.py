"""
MCP server exposing Code Chunker functionality.

This server provides a tool to chunk code into smaller, logical segments
and a resource to list supported file extensions.
"""

from mcp.server.fastmcp import FastMCP
from CodeParser import CodeParser
from Chunker import CodeChunker
from typing import Dict, List, Optional

# Create an MCP server with the name "Code Chunker Server"
mcp = FastMCP("Code Chunker Server")


@mcp.tool()
def chunk_code(code: str, file_extension: str, token_limit: int = 25) -> Dict[int, str]:
    """
    Chunks the provided code into logical segments based on token limit.
    
    Args:
        code: The source code to be chunked
        file_extension: The file extension (e.g., 'py', 'js', 'ts', 'css')
        token_limit: Target size of each chunk in tokens (default: 25)
        
    Returns:
        A dictionary with chunk numbers as keys and code segments as values
    """
    # Create a code chunker for the specified file extension
    chunker = CodeChunker(file_extension=file_extension)
    
    # Process the code through the chunker
    chunks = chunker.chunk(code, token_limit)
    
    return chunks


@mcp.resource("supported-file-types://list")
def get_supported_file_types() -> str:
    """
    Returns a list of file extensions supported by the Code Chunker.
    
    Returns:
        A string containing the list of supported file extensions
    """
    # Get the file extensions from CodeParser's language extension map
    code_parser = CodeParser()
    supported_extensions = list(code_parser.language_extension_map.keys())
    
    # Format the list for display
    extension_list = ", ".join(supported_extensions)
    return f"Supported file extensions: {extension_list}"


if __name__ == "__main__":
    # Run the server when the script is executed directly
    mcp.run()