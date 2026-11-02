import csv


students = {
    "student_a": {
        "knowledge_level": "beginner",
        "learning_preference": "simple examples",
        "learning_goal": "understand basic concepts"
    },

    "student_b": {
        "knowledge_level": "intermediate",
        "learning_preference": "step-by-step explanations",
        "learning_goal": "solve practice problems"
    },

    "student_c": {
        "knowledge_level": "advanced",
        "learning_preference": "mathematical reasoning",
        "learning_goal": "understand the underlying theory"
    }
}
print(students)

def build_user_context(profile):
    return (
        f"Learner's knowledge level: {profile['knowledge_level']}\n"
        f"Learning preference: {profile['learning_preference']}\n"
        f"Learning goal: {profile['learning_goal']}"
    )


for student_id, profile in students.items():
    print(f"\n--- {student_id} ---")
    print(build_user_context(profile))



def build_baseline_prompt(question):
     return f"""   
You are an educational AI tutor.
Answer the following question clearly and accurately.

Question: {question}
"""


def build_personalized_prompt(question, profile):
    user_context = build_user_context(profile)

    return f"""
You are an educational AI tutor.
Adapt your explanation to the learner's profile below.
Use the profile to adjust the explanation's depth, examples, and approach.
Do not assume anything about the learner beyond the provided information.

Learner profile:
{user_context}

Question: {question}
"""

question = "Explain what a derivative is in mathematics."

experiment_cases = []

for student_id, profile in students.items():
    experiment_cases.append({
        "student_id": student_id,
        "condition": "baseline",
        "prompt": build_baseline_prompt(question)
    })

    experiment_cases.append({
        "student_id": student_id,
        "condition": "personalized",
        "prompt": build_personalized_prompt(question, profile)
    })

for case in experiment_cases:
    print(
        f"\n{case['student_id']} | {case['condition']}"
    )
    print(case["prompt"])
    print("-" * 40)

print(f"\nTotal experiment cases: {len(experiment_cases)}")

# Export experiment prompts without using an API

csv_file = "experiment_prompts.csv"

fieldnames = [
    "student_id",
    "condition",
    "question",
    "prompt"
]

with open(csv_file, "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    for case in experiment_cases:
        writer.writerow({
            "student_id": case["student_id"],
            "condition": case["condition"],
            "question": question,
            "prompt": case["prompt"]
        })

print(f"\nExperiment prompts saved to {csv_file}")
print(f"Total experiment cases: {len(experiment_cases)}")