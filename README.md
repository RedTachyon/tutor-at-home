# We have a tutor at home

How to use the application:

Run UI via command line in your Terminal

python gradio_bot.py [--share] [--unicorn]

It will show chat bot for you. On the left there is a drop down list of the problems. On the right the app suggests the student to solve the problem.
The purpose of the app is to help student to get through the problem in the best interactive way.

The workflow is the following:
 - Student provides solution to the problem as they think is approprate for them
 - Based on the solution app reacts to it
      - If solution is partly correct, the Tutor will analyse and suggests to focus on problematic piece or to double check
      - If the student asks for a hint, the Tutor is able to provide a hint in interactive manner
      - The student can ask what exactly is not right with their solution, and Tutor will be able to provide constructive feedback that might help the student to find logical inconsistences
      - If solution is slightly incorrect, Tutor will be able to point to the slight calculation problem and to encourage to try again
      - If the answer is fully correct, but there is no explanation, the Tutor will ask for explanation
      - Once full correct solution is shown by Tutor to the Student, Student can ask for clarifications of each particular pieces of the solution in more details


Implementationwise the Tutor is based on State Machine (Automaton) depending on the Student solution or reaction the State might be switched. Depending on the State we use different Prompt to Communicate with Claude.
Terminal state is that Student provided Right answer AND description to the solution. If the Student did not provide solution, just right answer, we don't go to Terminal state, we ask Student for full solution.

Support of problems:
1. We support problems and solutions provided manually by teacher (or any human advisor)
2. We support loading Problem sets in Pdf and parsing for specific problems using haystack. This can be extendable to any text books.


