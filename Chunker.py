from abc import ABC, abstractmethod
from CodeParser import CodeParser
from Utils import count_tokens


class Chunker(ABC):
    def __init__(self, encoding_name="gpt-4"):
        self.encoding_name = encoding_name

    @abstractmethod
    def chunk(self, content, token_limit):
        pass

    @abstractmethod
    def get_chunk(self, chunked_content, chunk_number):
        pass

    @staticmethod
    def print_chunks(chunks):
        for chunk_number, chunk_code in chunks.items():
            print(f"Chunk {chunk_number}:")
            print("=" * 40)
            print(chunk_code)
            print("=" * 40)

    @staticmethod
    def consolidate_chunks_into_file(chunks):
        return "\n".join(chunks.values())

    @staticmethod
    def count_lines(consolidated_chunks):
        lines = consolidated_chunks.split("\n")
        return len(lines)


class CodeChunker(Chunker):
    def __init__(self, file_extension, encoding_name="gpt-4"):
        super().__init__(encoding_name)
        self.file_extension = file_extension

    def chunk(self, code, token_limit) -> dict:
        code_parser = CodeParser(self.file_extension)
        chunks = {}
        current_chunk = ""
        token_count = 0
        lines = code.split("\n")
        i = 0
        chunk_number = 1
        start_line = 0
        breakpoints = sorted(
            code_parser.get_lines_for_points_of_interest(code, self.file_extension)
        )
        comments = sorted(code_parser.get_lines_for_comments(code, self.file_extension))
        adjusted_breakpoints = []
        for bp in breakpoints:
            current_line = bp - 1
            highest_comment_line = None
            while current_line in comments:
                highest_comment_line = current_line
                current_line -= 1

            if highest_comment_line:
                adjusted_breakpoints.append(highest_comment_line)
            else:
                adjusted_breakpoints.append(bp)

        breakpoints = sorted(set(adjusted_breakpoints))

        while i < len(lines):
            line = lines[i]
            new_token_count = count_tokens(line, self.encoding_name)
            if token_count + new_token_count > token_limit:
                if i in breakpoints:
                    stop_line = i
                else:
                    stop_line = max(
                        [x for x in breakpoints if x <= i], default=start_line
                    )

                if stop_line == start_line and i not in breakpoints:
                    token_count += new_token_count
                    i += 1
                elif stop_line >= start_line:
                    current_chunk = "\n".join(lines[start_line : stop_line + 1])
                    if current_chunk.strip():
                        chunks[chunk_number] = current_chunk
                        chunk_number += 1
                    i = stop_line + 1
                    start_line = i
                    token_count = 0
            else:
                token_count += new_token_count
                i += 1

        current_chunk_code = "\n".join(lines[start_line:])
        if current_chunk_code.strip():
            chunks[chunk_number] = current_chunk_code

        return chunks

    def get_chunk(self, chunked_codebase, chunk_number):
        return chunked_codebase[chunk_number]
