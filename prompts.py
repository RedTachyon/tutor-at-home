START_PROMPT = """
Human: Take the role of an expert mathematician, physicist and computer scientist. You will be helping students solve school problems given in the <problem> tags. 
You will also receive a model solution in the <model> tags.
The student will tell you their current attempt at a solution in <attempt> tags.
You should compare this attempted solution with the model solution, and verify whether it is correct. If it is incomplete, you should consider it to be incorrect.
First, state the final answer of both the model and attempted solutions, in <model_answer> and <attempt_answer> tags respectively.
Then, provide an analysis of the attempted solution in <analysis> tags. After your analysis, include either Y or N in <correct> tags to indicate whether the solution is correct.
Remember that the attempted solution can use a different approach than the model solution as long as it is logically valid.

<problem>
%s
</problem>

<solution>
%s
</solution>

<attempt>
%s
</attempt>


Assistant: 
""".strip()

NEW_ATTEMPT_PROMPT = """
Human: As a reminder, you will receive the problem (in <problem> tags), model solution (in <model> tags) and the student's new attempt at a solution (in <attempt> tags). 
You should compare this attempted solution with the model solution, and verify whether it is correct. If it is incomplete, you should consider it to be incorrect.
First, state the final answer of both the model and attempted solutions, in <model_answer> and <attempt_answer> tages respectively.
Then, provide an analysis of the attempted solution in <analysis> tags. After your analysis, include either Y or N in <correct> tags to indicate whether the solution is correct.
Remember that the attempted solution can use a different approach than the model solution as long as it is logically valid.

<problem>
%s
</problem>

<solution>
%s
</solution>

<attempt>
%s
</attempt>

Assistant:
""".strip()

CORRECT_PROMPT = """
Human: The student was correct! Based on the analysis, give them a brief encouraging comment congratulating them for the solution. Put it in <congrats> tags.

Assistant: 
""".strip()


WRONG_PROMPT = """
Human: The student's solution was not correct. Use the analysis provided in the <analysis> tags earlier, and give the student a hint on what they did wrong, and what they should do instead. Keep it brief and put it in <hint> tags.
At the end of your message, ask the student if they want to try solving the problem again, get another hint, or see the full solution. Put it in <question> tags.

Assistant: 
""".strip()

WRONG_AGAIN_PROMPT = """
Human: The student's solution was not correct. Use the analysis provided in the <analysis> tags earlier, and give the student a hint on what they did wrong, and what they should do instead. Keep it brief and put it in <hint> tags.
At the end of your message, ask the student if they want to try solving the problem again or get another hint. Put it in <question> tags.

Assistant: 
""".strip()


HINT_OR_SOL_OR_REVISE_PROMPT = """
Human: Take the role of a teaching assistant. The student was just asked if he wants to solve the problem again, get a hint, or receive the full solution, the question is in the <question> tags, and the response is provided in <answer> tags.
Return the output in <choice> tags, either "revise" (which stands for attepmting the problem again), "hint", "solution" or "unclear" (without the quotations). Choose "unclear" if you are not sure. Do not say anything before or after the choice.

<question>
%s
</question>

<answer>
%s
</answer>

Assistant: """.strip()

HINT_PROMPT = """
Human: The student asked for a hint. Based on their progress and the model solution, propose a hint that would guide them towards the right answer. Put it in <hint> tags. 
At the end of your message, ask the student if they want to try solving the problem again, get another hint, or see the full solution. Put this in <question> tags.
The student's message asking for the solution is in <query> tags.

<query>
%s
</query>

Assistant:
""".strip()

SOLUTION_PROMPT = """
Human: The student asked for a full solution. Based on the model solution provided before as well as the student's progress, provide them with a full description of the solution. Put it in <solution> tags. The student's message asking for the solution is in <query> tags.
After that, ask them if the solution is clear and they would like to attempt solving it in their own words again, or if they want any part to be explained. Put this in <question> tags.

<query>
%s
</query>

Assistant: 
""".strip()

REVISION_PROMPT = """
Human: The student wants to try solving the problem again. Give them slight encouragement to do so. Put it in <encourage> tages. The student's message asking to try again is in <query> tags.

<query>
%s
</query>

Assistant: 
""".strip()

SOLUTION_CLEAR_PROMPT = """
Human: Take the role of a teaching assistant. The student was just asked if he understands the solution and wants to try solving the problem again, or if he wants some more explanations about the solution. The question is in the <question> tags, and the student's response is provided in <answer> tags.
Return the output in <choice> tags, either "explain", "solve", "unclear" (without the quotations). You should choose "solve" only if the student indicated readiness to solve the problem. Choose "unclear" if students asks a question irrelevant to the problem or the solution. Choose "explain" if the student ask to explain the solution or they ask to learn more. Otherwise choose "unclear". Do not say anything before or after the choice.
<question>
%s
</question>

<answer>
%s
</answer>

Assistant: """.strip()

EXPLANATION_PROMPT = """
Human: The student asked you to explain the solution you provided earlier. Their exact question is in the <query> tags. Provide a helpful and understandable explanation tailored to their knowledge. Put it in <explanation> tags.
After that, ask the student if there's anything else that's unclear, or if they're ready to solve the problem using their own words. Put the question in <question> tags.

<query>
%s
</query>

Assistant:
""".strip()

EXPLANATION_DONE_PROMPT = """
Human: Take the role of a teaching assistant. The student was just asked if he understands the solution and wants to try solving the problem again, or if he wants some more explanations about the solution. The question is in the <question> tags, and the student's response is provided in <answer> tags.
Return the output in <choice> tags, either "explain", "solve" (without the quotations). You should choose "solve" only if the student indicated readiness to solve the problem. Otherwise, choose "explain". Do not say anything before or after the choice.

<question>
%s
</question>

<answer>
%s
</answer>

Assistant:
""".strip()

UNCLEAR_CHOICE_PROMPT = """
Human: Take the role of a teaching assistant. The student was just asked if they want to try solving the problem again, or if they want some more hints about the solution. The student's answer was irrelevant. Kindly ask the student to return to the topic and explain why their answer wasn't relevant to the problem. Keep the response short. The question is in the <question> tags (tags not included), and the student's response is provided in <answer> tags. Provide your response in <response> tags.

<question>
%s
</question>

<answer>
%s
</answer>

Assistant:
"""

###


COMBINATORICS_PROBLEM = """A girl puts 5 letters in 5 evelopes randomly. In how many cases no letters is sent correctly?"""
COMBINATORICS_MODEL = """
<step> You can consider problem is how many permutations of (1 2 3 4 5) that no number comes back to its own place. <\step>
<step> To solve the problem you could use inclusion exclusion theorem and calculate the following.
Number of all permutations is 5!. <\step>
<step>  Assume one is correct and on its right place, we can find this one C^{1}_{5} = 5 combinations, the rest is permutated in 4! ways.  <\step>
 <step> Then we keep two in place with C^{2}_{5} ways, permutting the rest with 2!. <\step>
  <step> According to inclusion exclusion theorem we calculate the whole sum:
<equation> 5! - C^{1}_{5} 4! + C^{2}_{5} 3! - C^{3}_{5} 2! + C^{4}_{5} 1! = 120 - 5*24 + 10*6 - 10*2 + 5*1 - 1*1 = 44 <\equation>   <\step>""".strip()
COMBINATORICS_PARTIAL = """I know only the number or permutations, 5!, but I don't know what to do next, I'm stuck """
COMBINATORICS_GOOD = """120 - 60 + 60 - 20 + 5 - 1 = 44"""
COMBINATORICS_ALMOST = """ 120 - 60 + 60 - 20 + 5 - 1 = 33 """
COMBINATORICS_BAD = """This is my solution and answer 5! - 5 = 115"""



SPRING_PROBLEM = "A block of mass m=2 kg is attached to a spring with spring constant k = 100 N/m. The block is pulled x=20 cm to the right of the spring's equilibrium position and released from rest. Find the maximum speed of the block."

SPRING_MODEL = """
We will use the principle of conservation of energy. The potential energy of a spring is equal to P=1/2 kx^2. 
When we release the spring, this energy will be converted into kinetic energy until the midpoint, where all energy is kinetic. The formula for kinetic energy is E=1/2 mv^2.
Due to conservation of energy, we know that the two values P and E must be equal. We apply algebraic operations to obtain v:
1. 1/2 kx^2 = 1/2 mv^2
2. kx^2 = mv^2
3. k/m x^2 = v^2
4. v = sqrt(k/m) x

Substituting the values, we get v = sqrt(100/2) * 0.2 = sqrt(2).
""".strip()

SPRING_PARTIAL = "Okay, so I know I can use the spring constant, it's like F=-kx, so it will start moving left at that acceleration. But I'm not sure what to do next."
SPRING_GOOD = """Using the principle of conservation of energy, we can equate the initial potential energy of the compressed spring to the maximum kinetic energy of the mass when released.

The potential energy stored in a spring is P = 1/2kx^2, where k is the spring constant and x is the compression distance.

At the midpoint of the motion, all of this potential energy will have converted to kinetic energy, which is given by E = 1/2mv^2, where m is the mass and v is its speed.

Setting the initial potential energy equal to the maximum kinetic energy and rearranging gives:

v = sqrt(k/m)x

Plugging in the values k = 100 N/m, m = 2 kg, and x = 0.2 m, we get:

v = sqrt(100/2) * 0.2 = sqrt(2) m/s

So the maximum speed of the mass is sqrt(2) m/s, found by equating the initial potential energy to the kinetic energy at the midpoint using conservation of energy.""".strip()

SPRING_ALMOSTGOOD = """
The equation for conservation of energy is:
Initial energy = Final energy
For this problem: 
Initial elastic potential energy = Final maximum kinetic energy

The initial elastic potential energy stored in the spring is given by:
U = 1/2 kx^2
Where k is the spring constant (100 N/m) 
And x is the stretch distance (0.2 m)

The final maximum kinetic energy is given by: 
Kmax = 1/2 mv^2
Where m is the mass (2 kg)
And v is the maximum speed we want to find.

Setting the initial and final energies equal:
1/2 (100 N/m)(0.2 m)^2 = 1/2 (2 kg)v^2
Solving this gives v = 2 m/s.

So the maximum speed of the block is 2 m/s.""".strip()


SPRING_BAD = """
So I was thinking that due to energy conservation, the speed of the block will be the same across the entire trajectory. Since it starts at rest, the maximum velocity will be 0 m/s.
""".strip()




PROBLEMS = {
    "combinatorics": COMBINATORICS_PROBLEM,
    "spring": SPRING_PROBLEM
}

MODELS = {
    "combinatorics": COMBINATORICS_MODEL,
    "spring": SPRING_MODEL
}



CLAUDE_FIX = """
Human: Fix the formatting of the problem given in <problem> tags. It contains mathematical notation and combinatorical formulas. It was parsed from a PDF so it likely contains weird characters and newlines in weird spots. If you need to format weird elements like the Newton's Symbol, you can use alternative notation such as C_n^k. Format it in a way that is a readable text format. Return the answer in <result> tags. Only return the answer, do not attempt the solution.

<problem>
%s
</problem>

Assistant:
""".strip()