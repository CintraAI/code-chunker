import unittest
from test_base import BaseChunkerTest
from Chunker import CodeChunker

class TestCodeChunkerCSS(BaseChunkerTest):
    def setUp(self):
        super().setUp()
        self.code_chunker = CodeChunker(file_extension='css')

    def test_chunk_css_with_media_query(self):
        css_code = self.mock_codebase['media_queries.css']
        self.run_chunker_test(css_code)

    def test_chunk_css_with_simple_css(self):
        css_code = self.mock_codebase['simple_styles.css']
        self.run_chunker_test(css_code)

if __name__ == '__main__':
    unittest.main() 