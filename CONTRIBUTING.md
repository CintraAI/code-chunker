# Contributing to Code Chunker

Thank you for your interest in contributing to Code Chunker! This document provides guidelines and information for contributing to this project.

## Table of Contents
- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Development Setup](#development-setup)
- [Pull Request Process](#pull-request-process)
- [Testing Guidelines](#testing-guidelines)
- [Style Guidelines](#style-guidelines)

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment. We expect all contributors to:
- Use welcoming and inclusive language
- Be respectful of differing viewpoints and experiences
- Gracefully accept constructive criticism
- Focus on what is best for the community

## Getting Started

1. Fork the repository
2. Clone your fork locally
3. Create a new branch for your feature or bugfix
4. Make your changes following our guidelines
5. Push to your fork
6. Submit a Pull Request

## How to Contribute

There are several ways to contribute to Code Chunker:

1. **Bug Reports**: Submit detailed bug reports using the GitHub issue tracker
2. **Feature Requests**: Propose new features through GitHub issues
3. **Code Contributions**: Submit Pull Requests with improvements or new features
4. **Documentation**: Help improve or translate documentation
5. **Testing**: Add or improve test coverage

## Pull Request Process

1. Update the README.md with details of changes if applicable
2. Add appropriate unit tests for any new functionality
3. Ensure all tests pass by running:
   ```bash
   python -m unittest discover
   ```
4. Update documentation as needed
5. Ensure your code follows our style guidelines
6. Create a Pull Request with a clear title and description

## Testing Guidelines

- Write unit tests for all new functionality
- Maintain or improve code coverage
- Follow the existing test structure in `test_code_chunker.py`
- Test multiple file types and edge cases
- Include both positive and negative test cases

### Test Examples
- Test basic functionality with simple code files
- Test edge cases (empty files, large files)
- Test different programming languages (Python, JavaScript, CSS, etc.)
- Test with various token limits
- Test error handling scenarios

## Style Guidelines

### Python Code Style
- Follow PEP 8 guidelines
- Use type hints for function parameters and return values
- Keep functions focused and single-purpose
- Write clear docstrings for classes and functions
- Use meaningful variable and function names

### Code Organization
- Keep related functionality together
- Maintain clear separation of concerns
- Follow the existing project structure
- Use appropriate design patterns

## Language Support

When adding support for new programming languages:
1. Update the `language_extension_map` in `CodeParser.py`
2. Add appropriate node types in `_get_node_types_of_interest`
3. Include test files for the new language
4. Update documentation accordingly

## Documentation

- Keep README.md up to date
- Document all new features
- Include docstrings for new functions and classes
- Add comments for complex logic
- Update API documentation if applicable

## Questions or Need Help?

Feel free to:
- Open an issue for general questions
- Join our discussions in GitHub Discussions
- Reach out to maintainers for guidance

## License

By contributing to Code Chunker, you agree that your contributions will be licensed under the same license as the main project.

Thank you for contributing to Code Chunker!