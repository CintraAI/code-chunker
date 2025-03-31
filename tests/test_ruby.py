import unittest
from test_base import BaseChunkerTest
from Chunker import CodeChunker

class TestCodeChunkerRuby(BaseChunkerTest):
    def setUp(self):
        super().setUp()
        self.code_chunker = CodeChunker(file_extension='rb')

    def test_chunk_ruby_code(self):
        rb_code = self.mock_codebase['example.rb']
        chunks, _ = self.run_chunker_test(rb_code)
        self.assertGreater(len(chunks), 1)  # Ensure the code is actually chunked

if __name__ == '__main__':
    unittest.main() 