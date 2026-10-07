from openai import OpenAI

client = OpenAI()

question = "What is the total sales?"

# ==========================================
# LOAD AUDIT RULES
# ==========================================

with open("audit_rules.txt", "r", encoding="utf-8") as file:
    rules = file.read()


# ==========================================
# AI PROMPT
# ==========================================

prompt = f"""
You are a Proof-Carrying Data Analyst.

The user asked:

{question}

The main dataset is already loaded into a pandas DataFrame
called sales_df.

You must generate Python code that answers the user's question.

IMPORTANT AUDIT RULES:

{rules}

AVAILABLE COLUMNS:

{list(__import__('pandas').read_csv("data/superstore.csv").columns)}

REQUIREMENTS:

1. Follow the audit rules.
2. Use only pandas operations on sales_df.
3. Do not import libraries.
4. Do not access files.
5. Do not access the internet.
6. Do not use operating system commands.
7. Do not invent columns or data.
8. Return ONLY executable Python code.
9. Store the final answer in a variable called `answer`.

Example:

answer = sales_df["Sales"].sum()
"""

# ==========================================
# ASK AI
# ==========================================

response = client.responses.create(
    model="gpt-6-luna",
    input=prompt
)

generated_code = response.output_text


# ==========================================
# DISPLAY GENERATED CODE
# ==========================================

print("\n========== AI GENERATED CODE ==========\n")

print(generated_code)