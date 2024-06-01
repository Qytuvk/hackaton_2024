import json
import os

class ResumeManager:
    def __init__(self, filename):
        self.filename = filename
        self.resume_data = self.load_resume_data()

    def load_resume_data(self):
        try:
            file_path = os.path.abspath(self.filename)
            with open(file_path, "r", encoding = "utf-8") as json_file:
                return json.load(json_file)
        except FileNotFoundError:
            return {"resumes": []}

    def save_resume_data(self):
        file_path = os.path.abspath(self.filename)
        with open(file_path, "w",  encoding = "utf-8") as json_file:
            json.dump(self.resume_data, json_file, indent=4, ensure_ascii=False)

    def add_resume(self, resume):
        existing_resume = self.get_resume_by_name(resume["name"])
        if existing_resume:
            print(f"Резюме с именем '{resume['name']}' уже существует.")
            return
        self.resume_data["resumes"].append(resume)  # Add the new resume
        self.save_resume_data()  # Save the updated data

    def get_resume_by_name(self, name):
        for resume in self.resume_data["resumes"]:
            if resume["name"] == name:
                return resume
        return None

    def create_resume(self, name, skils):
        new_resume = {
            "name": name,
            "skills": [skils]
        }
        self.add_resume(new_resume)


if __name__ == "__main__":
    json_file_path = "db.json"
    manager = ResumeManager(json_file_path)

    target_resume = manager.get_resume_by_name(target_name)

    if target_resume:
        print("Имя:", target_resume["name"])
        print("Навыки:", ", ".join(target_resume["skills"]))
    else:
        print(f"Резюме с именем '{target_name}' не найдено.")
