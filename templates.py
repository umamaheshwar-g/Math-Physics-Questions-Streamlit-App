QUESTION_PROMPT = """Generate a {subject} question for {grade_level} level on the topic of {topic} and toughness level of {toughness_level}.
The question should involve numerical calculations.

Examples:
Example 0:
Subject: Physics
Grade Level: High School
Topic: Dynamics
Toughness Level: Tough
Question: A shell flying with velocity 500 m/s bursts into three identical fragments so that the kinetic energy of the system increases 1.5 times. What maximum velocity can one of the fragments obtain?

Input:

Subject: Physics
Grade Level: High School
Topic: Kinematics
Toughness Level: Very Tough

Question: A shell flying with velocity 500 m/s bursts into three identical fragments so that the kinetic energy of the system increases 1.5 times. What maximum velocity can one of the fragments obtain?
Input:

Subject: Mathematics
Grade Level: Middle School
Topic: Geometry
Toughness Level: Medium

Question: A rectangular garden has a length that is 4 meters longer than its width. If the perimeter of the garden is 36 meters, what is the area of the garden in square meters?
Input:

Subject: Chemistry
Grade Level: High School
Topic: Stoichiometry
Toughness Level: Tough

Question: In a chemical reaction, 45.0 grams of glucose (C6H12O6) reacts completely with excess oxygen to produce carbon dioxide and water. If the reaction has a 92% yield, how many grams of carbon dioxide are produced? (Molar masses: C = 12 g/mol, H = 1 g/mol, O = 16 g/mol)
Input:

Subject: Biology
Grade Level: College
Topic: Population Genetics
Toughness Level: Very Tough

Output: In a population of 10,000 individuals, a certain allele has a frequency of 0.3. Assuming Hardy-Weinberg equilibrium, if a dominant phenotype is expressed when at least one copy of this allele is present, how many individuals would you expect to show the recessive phenotype? Round your answer to the nearest whole number.
Input:

Subject: Economics
Grade Level: High School
Topic: Compound Interest
Toughness Level: Tough

Question: An investor deposits $5,000 into an account that earns 6% interest compounded quarterly. If they make no additional deposits or withdrawals, how much money will be in the account after 10 years? Round your answer to the nearest cent.

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
