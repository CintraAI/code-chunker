from mcp.server.fastmcp import FastMCP
from code_chunker_input import CodeChunkerInput
from Chunker import CodeChunker
from typing import Dict

# Initialize the MCP server
mcp = FastMCP("CodeChunkerServer")

@mcp.tool()
def execute_code_chunking(input_data: CodeChunkerInput) -> Dict[str, Dict[int, str]]:
    """
    Execute code chunking on multiple files using the CodeChunker.
    
    Args:
        input_data (CodeChunkerInput): Object containing files to chunk and token limit
        
    Returns:
        Dict[str, Dict[int, str]]: Dictionary mapping filenames to their chunked contents
    """
    results = {}
    
    for filename, content in input_data.files.items():
        # Extract file extension
        file_extension = filename.split('.')[-1] if '.' in filename else ''
        
        # Initialize code chunker for this file type
        chunker = CodeChunker(file_extension=file_extension)
        
        try:
            # Chunk the file content
            chunks = chunker.chunk(content, token_limit=input_data.token_limit)
            results[filename] = chunks
        except ValueError as e:
            # Handle unsupported file types or other chunking errors
            results[filename] = {
                0: f"Error chunking file: {str(e)}"
            }
        except Exception as e:
            # Handle any other unexpected errors
            results[filename] = {
                0: f"Unexpected error while chunking: {str(e)}"
            }
    
    return results

if __name__ == "__main__":
    # Run the MCP server
    mcp.run()