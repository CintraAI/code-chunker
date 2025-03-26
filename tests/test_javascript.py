import unittest
from test_base import BaseChunkerTest
from Chunker import CodeChunker

class TestCodeChunkerJavaScript(BaseChunkerTest):
    def setUp(self):
        super().setUp()
        self.code_chunker = CodeChunker(file_extension='js')

    def test_chunk_javascript_simple_code(self):
        js_code = self.mock_codebase['simple.js']
        self.run_chunker_test(js_code)

    def test_chunk_javascript_with_routes(self):
        js_code = self.mock_codebase['routes.js']
        self.run_chunker_test(js_code)

    def test_chunk_javascript_with_models(self):
        js_code = self.mock_codebase['models.js']
        self.run_chunker_test(js_code)

    def test_chunk_javascript_with_main(self):
        js_code = self.mock_codebase['main.js']
        self.run_chunker_test(js_code)

    def test_chunk_javascript_with_utilities(self):
        js_code = self.mock_codebase['utilities.js']
        self.run_chunker_test(js_code)

    def test_chunk_javascript_with_big_class(self):
        js_code = self.mock_codebase['big_class.js']
        self.run_chunker_test(js_code)

    def test_chunk_javascript_with_react_component(self):
        js_code = self.mock_codebase['react_component.js']
        self.run_chunker_test(js_code)

if __name__ == '__main__':
    unittest.main() 