from typarse import BaseParser
from haystack.nodes import TextConverter, PDFToTextConverter, DocxToTextConverter, PreProcessor
import os

class Parser(BaseParser):
    path: str
    save_dir: str = './extracted/combinatorics'

    _abbrev = {
        'path': 'p',
        'save_dir': 's'
    }


def claude_fix():
    pass

def doc_parser():
    problems = []
    solutions = []
    problem_setmode = 0
    solution_mode = 0
    problem_statement = ''
    problem_solution = ''

    for each in docs_default:

        if 'Problem' in each.content:
            problem_setmode = 1
            solution_mode = 0
            solutions.append(problem_solution)
            problem_statement = ''
            problem_solution = ''

            problem_statement += each.content

        elif 'Solution' in each.content:
            solution_mode = 1
            problem_setmode = 0
            problems.append(problem_statement)
            problem_statement = ''
            problem_solution += each.content

        elif problem_setmode:
            problem_statement += each.content
        elif solution_mode:
            problem_solution += each.content
    return problems, solutions[1:]


if __name__ == "__main__":
    args = Parser()

    converter = PDFToTextConverter(remove_numeric_tables=True, valid_languages=["en"])
    doc_pdf = converter.convert(file_path=args.path, meta=None)[0]

    preprocessor = PreProcessor(
        split_by="sentence",
        split_length=1,
        split_respect_sentence_boundary=False)
    docs_default = preprocessor.process([doc_pdf])

    problems, solutions = doc_parser()

    os.makedirs(args.save_dir, exist_ok=True)

    for i, (problem, solution) in enumerate(zip(problems, solutions)):
        with open(os.path.join(args.save_dir, f'problem_{i}.txt'), 'w') as f:
            f.write(problem.strip())
        with open(os.path.join(args.save_dir, f'solution_{i}.txt'), 'w') as f:
            f.write(solution.strip())
