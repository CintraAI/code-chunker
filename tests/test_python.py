import unittest
from test_base import BaseChunkerTest, mock_count_tokens
from Chunker import CodeChunker

class TestCodeChunkerPython(BaseChunkerTest):
    def setUp(self):
        super().setUp()
        self.code_chunker = CodeChunker(file_extension='py')
    
    def test_chunk_simple_code(self):
        py_code = self.mock_codebase['simple.py']
        first_chunk_token_limit = mock_count_tokens("import sys")
        print(f"first_chunk_token_limit = {first_chunk_token_limit}")
        chunks = self.code_chunker.chunk(py_code, token_limit=25)
        token_count = self.mock_count_tokens(py_code)
        print(f"token_count = {token_count}")
        print(f"original code:\n {py_code}")
        
        chunks, full_code = self.run_chunker_test(py_code, token_limit=25)
        
        self.assertEqual(len(chunks), 2) # There should be 2 chunks
        self.assertIn("import sys", chunks[1]) # The first chunk should contain the import statement
        self.assertIn("print('Hello, world!')", chunks[2]) # The second chunk should contain the print statement

    def test_chunk_code_text_only(self):
        py_code = self.mock_codebase['text_only.py']
        chunks, final_code = self.run_chunker_test(py_code)
        
        self.assertEqual(len(chunks), 1)
        self.assertIn("This file is empty and should test the chunker's ability to handle empty files", chunks[1])

    def test_chunk_code_with_routes(self):
        py_code = self.mock_codebase['routes.py']
        self.run_chunker_test(py_code)

    def test_chunk_code_with_models(self):
        py_code = self.mock_codebase['models.py']
        self.run_chunker_test(py_code)

    def test_chunk_code_with_main(self):
        py_code = self.mock_codebase['main.py']
        self.run_chunker_test(py_code)

    def test_chunk_code_with_utilities(self):
        py_code = self.mock_codebase['utilities.py']
        self.run_chunker_test(py_code)

    def test_chunk_code_with_big_class(self):
        py_code = self.mock_codebase['big_class.py']
        self.run_chunker_test(py_code)

if __name__ == '__main__':
    unittest.main() 