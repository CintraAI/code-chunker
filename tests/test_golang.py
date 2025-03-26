import unittest
from test_base import BaseChunkerTest
from Chunker import CodeChunker

class TestCodeChunkerGolang(BaseChunkerTest):
    def setUp(self):
        super().setUp()
        self.code_chunker = CodeChunker(file_extension='go')

    def test_chunk_golang_simple_code(self):
        go_code = self.mock_codebase['simple.go']
        chunks, _ = self.run_chunker_test(go_code)
        self.assertGreater(len(chunks), 1)  # Ensure the code is actually chunked

    def test_chunk_golang_with_structs(self):
        go_code = self.mock_codebase['structs.go']
        chunks, _ = self.run_chunker_test(go_code)
        self.assertGreater(len(chunks), 1)

    def test_chunk_golang_with_interfaces(self):
        go_code = self.mock_codebase['interfaces.go']
        chunks, _ = self.run_chunker_test(go_code)
        self.assertGreater(len(chunks), 1)

    def test_chunk_golang_with_goroutines(self):
        go_code = self.mock_codebase['goroutines.go']
        chunks, _ = self.run_chunker_test(go_code)
        self.assertGreater(len(chunks), 1)

if __name__ == '__main__':
    unittest.main() 