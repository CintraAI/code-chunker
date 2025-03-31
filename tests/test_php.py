import unittest
from test_base import BaseChunkerTest
from Chunker import CodeChunker

class TestCodeChunkerPHP(BaseChunkerTest):
    def setUp(self):
        super().setUp()
        self.code_chunker = CodeChunker(file_extension='php')

    def test_chunk_php_code(self):
        php_code = self.mock_codebase['example.php']
        chunks, _ = self.run_chunker_test(php_code)
        self.assertGreater(len(chunks), 1)  # Ensure the code is actually chunked

if __name__ == '__main__':
    unittest.main() 