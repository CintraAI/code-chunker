---
title: CintraAI Code Chunker
emoji: 🧩
colorFrom: blue
colorTo: indigo
sdk: streamlit
sdk_version: 1.33.0
app_file: app.py
pinned: false
license: mit
---


# CintraAI Code Chunker

Cintra's Code Chunker is a novel open-source tool designed to enhance code readability and maintainability by intelligently chunking code files based on key points of interest. This tool leverages advanced parsing techniques to identify significant elements in your code, such as functions, classes, and comments, to organize your codebase into manageable, easily understandable chunks. It's an invaluable resource for applications such as RAG, code patching, and other use cases.

## Features

- **Intelligent Chunking:** Break down your code files into chunks around key points of interest like function definitions, class declarations, and crucial comments.
- **Customizable Token Limits:** Control the size of each chunk with customizable token limits, ensuring that chunks remain manageable and focused.
- **Support for Multiple Languages:** Initially supporting Python, JavaScript, and CSS, with plans to expand to more programming languages.

## Try Out Code Chunker!

Interested in seeing how it works? Check out our interactive demo on **Hugging Face Spaces**.

[**Click here to try it out!**](https://huggingface.co/spaces/CintraAI/code-chunker)
  
## Getting Started

### Prerequisites

- Python 3.8+

### Installation

1. Clone the repository:
```sh
git clone https://github.com/yourgithubusername/code-chunker.git
```

2. Navigate to the project directory
```sh
cd code-chunker
```
4. Install the required dependencies
```sh
pip install -r requirements.txt
```
## Usage
1. Chunking a Code File:
Use the CodeChunker class to chunk a specific code file. You can specify the file extension and token limit for chunking.
Example:
```py
chunker = CodeChunker(file_extension='py', encoding_name='gpt-4')
chunks = chunker.chunk(your_code_here, token_limit=1000)
CodeChunker.print_chunks(chunks)
```
2. Parsing Code for Points of Interest:

The CodeParser class allows you to parse code to identify points of interest and comments, which can then be used for chunking or other analysis.
Example:
```
parser = CodeParser(['py'])
tree = parser.parse_code(your_code_here, 'py')
points_of_interest = parser.extract_points_of_interest(tree, 'py')
```

3. Understanding the Token Limit in Chunking:

In the `chunk` method of the `Chunker` class, a `token_limit` parameter is used to control the size of each chunk of code. A 'token' can be thought of as the smallest unit of processing. In the context of text processing, a token could be a word, a sentence, or a similar unit.

The `token_limit` parameter limits the number of these tokens for each chunk. If the limit is, for instance, 100 tokens, that means each chunk of content produced by the `chunk` method should contain no more than 100 tokens.

It is worth noting that the way content is tokenized and how a token is defined depends on the specific implementation and the type of content being processed.

## Contributing
We welcome contributions from the community, whether it's through reporting bugs, submitting feature requests, or sending pull requests. Please check the CONTRIBUTING.md file for more details on how to contribute to the project.

## License
This project is licensed under the MIT license. See the License file for details

## Acknowledgments
- This project utilizes the tree-sitter project for parsing code.
- This also uses tiktoken to count tokens for determining chunk sizes.

