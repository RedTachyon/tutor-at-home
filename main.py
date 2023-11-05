from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
import os
from dotenv import load_dotenv

from tutor import Tutor

load_dotenv()

anthropic = Anthropic(api_key=os.getenv("ANTHROPIC_KEY"))

tutor = Tutor(anthropic, "What number, when squared, gives 1?", "Either 1 or -1 produce 1 when squared.")

tutor.naive_loop()
