import unittest
from unittest.mock import patch
import tiktoken
import sys
import os

# Add parent directory to path to allow imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Chunker import Chunker, CodeChunker
from utils import load_json

# Mocking the count_tokens function as it's external and not the focus of these tests
def mock_count_tokens(string: str, encoding_name='gpt-4') -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.encoding_for_model(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

class BaseChunkerTest(unittest.TestCase):
    """Base class for all code chunker tests with common setup and utilities."""
    
    def setUp(self):
        self.patcher = patch('utils.count_tokens', side_effect=mock_count_tokens)
        self.mock_count_tokens = self.patcher.start()
        self.mock_codebase = load_json('mock_codefiles.json')
        
    def tearDown(self):
        self.patcher.stop()
    
    def run_chunker_test(self, code, token_limit=20):
        """Helper method to run standard chunker tests."""
        chunks = self.code_chunker.chunk(code, token_limit=token_limit)
        Chunker.print_chunks(chunks)
        final_code = Chunker.consolidate_chunks_into_file(chunks)
        num_lines = Chunker.count_lines(final_code)
        
        # Common assertions
        self.assertEqual(num_lines, len(code.split("\n")))
        self.assertIn(code, final_code)
        
        return chunks, final_code 