# Smart Resume Analyzer (ATS Simulator)
def extract_keywords(resume_text):
    keywords = ["python", "data", "analysis", "project", "team", "communication"]
    found = {kw: resume_text.lower().count(kw) for kw in keywords}
    return found

if __name__ == "__main__":
    print("Enter your resume text (paste all at once):")
    resume = input(">> ")
    result = extract_keywords(resume)
    print("\nKeyword Match Summary:")
    for k, v in result.items():
        print(f"{k.title()}: {v}")
