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

Question: In a population of 10,000 individuals, a certain allele has a frequency of 0.3. Assuming Hardy-Weinberg equilibrium, if a dominant phenotype is expressed when at least one copy of this allele is present, how many individuals would you expect to show the recessive phenotype? Round your answer to the nearest whole number.
Input:

Subject: Mathematics
Grade Level: High School
Topic: Trigonometry
Toughness Level: Tough

Question: A ladder 10 meters long leans against a vertical wall. The foot of the ladder is 6 meters from the base of the wall. If the top of the ladder slides down 2 meters, how far will the foot of the ladder move out from the wall? Round your answer to two decimal places.
Input:

Subject: Physics
Grade Level: College
Topic: Thermodynamics
Toughness Level: Very Tough

Question: An ideal gas undergoes an isothermal expansion from 2.0 L to 5.0 L at a temperature of 300 K. If the initial pressure was 3.0 atm, calculate the work done by the gas during this process. Express your answer in joules, rounded to the nearest whole number. (R = 0.08206 L⋅atm/mol⋅K)
Input:

Subject: Chemistry
Grade Level: High School
Topic: Acid-Base Titration
Toughness Level: Medium

Question: A student titrates 25.0 mL of 0.1 M NaOH solution with 0.05 M HCl solution. How many milliliters of HCl solution are needed to completely neutralize the NaOH solution? Round your answer to one decimal place.
Input:

Subject: Mathematics
Grade Level: Middle School
Topic: Probability
Toughness Level: Tough

Question: A bag contains 5 red marbles, 3 blue marbles, and 2 green marbles. If two marbles are drawn without replacement, what is the probability of drawing a red marble followed by a blue marble? Express your answer as a fraction in its simplest form.
Input:

Subject: Physics
Grade Level: High School
Topic: Circuits
Toughness Level: Tough

Question: In a series circuit, three resistors with resistances of 2 Ω, 4 Ω, and 6 Ω are connected to a 12 V battery. If the current flowing through the 2 Ω resistor is 1 A, what is the power dissipated by the 6 Ω resistor? Express your answer in watts.
Input:

Subject: Chemistry
Grade Level: College
Topic: Electrochemistry
Toughness Level: Very Tough

Question: A voltaic cell is constructed using a zinc electrode in 1.0 M Zn²⁺ solution and a silver electrode in 1.0 M Ag⁺ solution at 25°C. Given that the standard reduction potentials are E°(Zn²⁺/Zn) = -0.76 V and E°(Ag⁺/Ag) = +0.80 V, calculate the Gibbs free energy change for the cell reaction. Express your answer in kJ/mol, rounded to two decimal places. (F = 96,485 C/mol)

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
2. Return a dictionary with 'value' and 'units'(note: if relevant) as keys
3. Be general enough to solve similar questions with different numerical inputs

Function:"""

ANSWER_VARIATION_PROMPT = """
Given the correct answer to the following question:
{question}
generate {num_variations} slightly different incorrect answer variations. Provide the variations as a JSON array.
Correct Answer: {correct_answer}

JSON Output:"""
