import unittest
from test_base import BaseChunkerTest
from Chunker import CodeChunker

class TestCodeChunkerTypeScript(BaseChunkerTest):
    def setUp(self):
        super().setUp()
        self.code_chunker = CodeChunker(file_extension='ts')

    def test_chunk_typescript_code(self):
        ts_code = self.mock_codebase['example.ts']
        chunks, _ = self.run_chunker_test(ts_code)
        self.assertGreater(len(chunks), 1)  # Ensure the code is actually chunked

if __name__ == '__main__':
    unittest.main() 