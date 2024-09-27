QUESTION_PROMPT = """Generate a {subject} question for {grade_level} level on the topic of {topic} and toughness level of {toughness_level}.
The question should involve numerical calculations.

Examples:
Example 1:
Generate a math or physics question for High School level on the topic of Kinematics and toughness level of Very Tough
Generated Question: A shell flying with velocity 500 m/s bursts into three identical fragments so that the kinetic energy of the system increases 1.5 times. What maximum velocity can one of the fragments obtain?


Only provide the Question:"""

NUMERICAL_EXTRACTION_PROMPT = """Extract all numerical values from the following question.
Return the result as a JSON object with keys and values, keys should be camel case and verbose.

Question: {question}

JSON Output:"""

SCRIPT_PROMPT = """Create a Python function that solves the following question:

{question}

The function should:
1. Take the numerical values from the question as arguments, arguments names should match the question
2. Return a dictionary with 'value' and 'units' as keys
3. Be general enough to solve similar questions with different numerical inputs

Function:"""

ANSWER_VARIATION_PROMPT = """
Given the correct answer to the following question:
{question}
generate {num_variations} slightly different incorrect answer variations. Provide the variations as a JSON array.
Correct Answer: {correct_answer}

JSON Output:"""
