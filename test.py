import tkinter as tk
from tkinter import messagebox
from experta import *
import ast

# Lớp hệ thống chẩn đoán bệnh
class MedicalExpert(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.disease = "unknown"
        self.predicted_disease = ""
        



    @DefFacts()
    def needed_data(self):
        yield Fact(findDisease='true')

    # Các quy tắc xác định bệnh
# luật dựa trên các sự kiện
# 1
    @Rule(Fact(findDisease='true'),
          Fact(memory_loss='y'),
          Fact(confusion='y'),
          Fact(drowsiness='y'),
          Fact(joint_pain='n'),
          Fact(stiffness='n'),
          Fact(back_pain='n'),
          Fact(wheezing='n'),
          Fact(shortness_of_breath='n'),
          Fact(chest_tightness='n'),
          Fact(anxiety='n'),
          Fact(fever='n'),
          Fact(cough='n'),
          Fact(fatigue='n'),
          Fact(excessive_thirst='n'),
          Fact(seizures='n'),
          Fact(headache='n'),
          Fact(eye_pain='n'),
          Fact(blurred_vision='n'),
          Fact(chest_pain='n'),
          Fact(dizziness='n'),
          Fact(weakness='n'),
          Fact(sweating='n'),
          Fact(shivering='n'),
          Fact(nasal_congestion='n'),
          Fact(yellowing_skin='n'))
    def disease_0(self):
        self.declare(Fact(disease='Alzheimer'))

# 2
    @Rule(Fact(findDisease='true'),
          Fact(memory_loss='n'),
          Fact(confusion='n'),
          Fact(drowsiness='n'),
          Fact(joint_pain='y'),
          Fact(stiffness='y'),
          Fact(back_pain='y'),
          Fact(wheezing='n'),
          Fact(shortness_of_breath='n'),
          Fact(chest_tightness='n'),
          Fact(anxiety='n'),
          Fact(fever='n'),
          Fact(cough='n'),
          Fact(fatigue='n'),
          Fact(excessive_thirst='n'),
          Fact(seizures='n'),
          Fact(headache='n'),
          Fact(eye_pain='n'),
          Fact(blurred_vision='n'),
          Fact(chest_pain='n'),
          Fact(dizziness='n'),
          Fact(weakness='n'),
          Fact(sweating='n'),
          Fact(shivering='n'),
          Fact(nasal_congestion='n'),
          Fact(yellowing_skin='n'))
    def disease_1(self):
        self.declare(Fact(disease='Arthritis'))

# 3
    @Rule(Fact(findDisease='true'),
          Fact(memory_loss='n'),
          Fact(confusion='n'),
          Fact(drowsiness='n'),
          Fact(joint_pain='n'),
          Fact(stiffness='n'),
          Fact(back_pain='n'),
          Fact(wheezing='y'),
          Fact(shortness_of_breath='y'),
          Fact(chest_tightness='y'),
          Fact(anxiety='y'),
          Fact(fever='n'),
          Fact(cough='n'),
          Fact(fatigue='n'),
          Fact(excessive_thirst='n'),
          Fact(seizures='n'),
          Fact(headache='n'),
          Fact(eye_pain='n'),
          Fact(blurred_vision='n'),
          Fact(chest_pain='n'),
          Fact(dizziness='n'),
          Fact(weakness='n'),
          Fact(sweating='n'),
          Fact(shivering='n'),
          Fact(nasal_congestion='n'),
          Fact(yellowing_skin='n'))
    def disease_2(self):
        self.declare(Fact(disease='Asthma'))

# 4
    @Rule(Fact(findDisease='true'),
          Fact(memory_loss='n'),
          Fact(confusion='n'),
          Fact(drowsiness='n'),
          Fact(joint_pain='n'),
          Fact(stiffness='n'),
          Fact(back_pain='n'),
          Fact(wheezing='n'),
          Fact(shortness_of_breath='n'),
          Fact(chest_tightness='y'),
          Fact(anxiety='n'),
          Fact(fever='y'),
          Fact(cough='y'),
          Fact(fatigue='y'),
          Fact(excessive_thirst='n'),
          Fact(seizures='n'),
          Fact(headache='n'),
          Fact(eye_pain='n'),
          Fact(blurred_vision='n'),
          Fact(chest_pain='n'),
          Fact(dizziness='n'),
          Fact(weakness='n'),
          Fact(sweating='n'),
          Fact(shivering='n'),
          Fact(nasal_congestion='n'),
          Fact(yellowing_skin='n'))
    def disease_3(self):
        self.declare(Fact(disease='Covid'))

# 5
    @Rule(Fact(findDisease='true'),
          Fact(memory_loss='n'),
          Fact(confusion='n'),
          Fact(drowsiness='n'),
          Fact(joint_pain='n'),
          Fact(stiffness='n'),
          Fact(back_pain='n'),
          Fact(wheezing='n'),
          Fact(shortness_of_breath='n'),
          Fact(chest_tightness='n'),
          Fact(anxiety='y'),
          Fact(fever='n'),
          Fact(cough='n'),
          Fact(fatigue='y'),
          Fact(excessive_thirst='y'),
          Fact(seizures='n'),
          Fact(headache='n'),
          Fact(eye_pain='n'),
          Fact(blurred_vision='n'),
          Fact(chest_pain='n'),
          Fact(dizziness='n'),
          Fact(weakness='y'),
          Fact(sweating='n'),
          Fact(shivering='n'),
          Fact(nasal_congestion='n'),
          Fact(yellowing_skin='n'))
    def disease_4(self):
        self.declare(Fact(disease='Diabetes'))

# 6
    @Rule(Fact(findDisease='true'),
          Fact(memory_loss='n'),
          Fact(confusion='y'),
          Fact(drowsiness='n'),
          Fact(joint_pain='n'),
          Fact(stiffness='n'),
          Fact(back_pain='n'),
          Fact(wheezing='n'),
          Fact(shortness_of_breath='n'),
          Fact(chest_tightness='n'),
          Fact(anxiety='n'),
          Fact(fever='n'),
          Fact(cough='n'),
          Fact(fatigue='n'),
          Fact(excessive_thirst='n'),
          Fact(seizures='y'),
          Fact(headache='y'),
          Fact(eye_pain='n'),
          Fact(blurred_vision='n'),
          Fact(chest_pain='n'),
          Fact(dizziness='n'),
          Fact(weakness='n'),
          Fact(sweating='n'),
          Fact(shivering='n'),
          Fact(nasal_congestion='n'),
          Fact(yellowing_skin='n'))
    def disease_5(self):
        self.declare(Fact(disease='Epilepsy'))

# 7
    @Rule(Fact(findDisease='true'),
          Fact(memory_loss='n'),
          Fact(confusion='n'),
          Fact(drowsiness='n'),
          Fact(joint_pain='n'),
          Fact(stiffness='n'),
          Fact(back_pain='n'),
          Fact(wheezing='n'),
          Fact(shortness_of_breath='n'),
          Fact(chest_tightness='n'),
          Fact(anxiety='n'),
          Fact(fever='n'),
          Fact(cough='n'),
          Fact(fatigue='n'),
          Fact(excessive_thirst='n'),
          Fact(seizures='n'),
          Fact(headache='y'),
          Fact(eye_pain='y'),
          Fact(blurred_vision='y'),
          Fact(chest_pain='n'),
          Fact(dizziness='n'),
          Fact(weakness='y'),
          Fact(sweating='n'),
          Fact(shivering='n'),
          Fact(nasal_congestion='n'),
          Fact(yellowing_skin='n'))
    def disease_6(self):
        self.declare(Fact(disease='Glaucoma'))

# 8
    @Rule(Fact(findDisease='true'),
          Fact(memory_loss='n'),
          Fact(confusion='n'),
          Fact(drowsiness='n'),
          Fact(joint_pain='n'),
          Fact(stiffness='n'),
          Fact(back_pain='n'),
          Fact(wheezing='n'),
          Fact(shortness_of_breath='n'),
          Fact(chest_tightness='y'),
          Fact(anxiety='y'),
          Fact(fever='n'),
          Fact(cough='n'),
          Fact(fatigue='y'),
          Fact(excessive_thirst='n'),
          Fact(seizures='n'),
          Fact(headache='n'),
          Fact(eye_pain='n'),
          Fact(blurred_vision='n'),
          Fact(chest_pain='y'),
          Fact(dizziness='n'),
          Fact(weakness='n'),
          Fact(sweating='n'),
          Fact(shivering='n'),
          Fact(nasal_congestion='n'),
          Fact(yellowing_skin='n'))
    def disease_7(self):
        self.declare(Fact(disease='Heart Disease'))

# 9
    @Rule(Fact(findDisease='true'),
          Fact(memory_loss='n'),
          Fact(confusion='n'),
          Fact(drowsiness='y'),
          Fact(joint_pain='n'),
          Fact(stiffness='n'),
          Fact(back_pain='n'),
          Fact(wheezing='n'),
          Fact(shortness_of_breath='y'),
          Fact(chest_tightness='n'),
          Fact(anxiety='n'),
          Fact(fever='y'),
          Fact(cough='n'),
          Fact(fatigue='n'),
          Fact(excessive_thirst='n'),
          Fact(seizures='n'),
          Fact(headache='n'),
          Fact(eye_pain='n'),
          Fact(blurred_vision='n'),
          Fact(chest_pain='n'),
          Fact(dizziness='y'),
          Fact(weakness='y'),
          Fact(sweating='n'),
          Fact(shivering='n'),
          Fact(nasal_congestion='n'),
          Fact(yellowing_skin='n'))
    def disease_8(self):
        self.declare(Fact(disease='Heat Stroke'))

# 10
    @Rule(Fact(findDisease='true'),
          Fact(memory_loss='n'),
          Fact(confusion='n'),
          Fact(drowsiness='n'),
          Fact(joint_pain='n'),
          Fact(stiffness='n'),
          Fact(back_pain='n'),
          Fact(wheezing='n'),
          Fact(shortness_of_breath='n'),
          Fact(chest_tightness='y'),
          Fact(anxiety='y'),
          Fact(fever='n'),
          Fact(cough='n'),
          Fact(fatigue='n'),
          Fact(excessive_thirst='n'),
          Fact(seizures='n'),
          Fact(headache='n'),
          Fact(eye_pain='n'),
          Fact(blurred_vision='n'),
          Fact(chest_pain='n'),
          Fact(dizziness='n'),
          Fact(weakness='n'),
          Fact(sweating='y'),
          Fact(shivering='n'),
          Fact(nasal_congestion='n'),
          Fact(yellowing_skin='n'))
    def disease_9(self):
        self.declare(Fact(disease='Hyperthyroidism'))

# 11
    @Rule(Fact(findDisease='true'),
          Fact(memory_loss='n'),
          Fact(confusion='n'),
          Fact(drowsiness='y'),
          Fact(joint_pain='n'),
          Fact(stiffness='n'),
          Fact(back_pain='n'),
          Fact(wheezing='n'),
          Fact(shortness_of_breath='n'),
          Fact(chest_tightness='n'),
          Fact(anxiety='n'),
          Fact(fever='n'),
          Fact(cough='n'),
          Fact(fatigue='y'),
          Fact(excessive_thirst='n'),
          Fact(seizures='n'),
          Fact(headache='n'),
          Fact(eye_pain='n'),
          Fact(blurred_vision='n'),
          Fact(chest_pain='n'),
          Fact(dizziness='n'),
          Fact(weakness='n'),
          Fact(sweating='n'),
          Fact(shivering='y'),
          Fact(nasal_congestion='n'),
          Fact(yellowing_skin='n'))
    def disease_10(self):
        self.declare(Fact(disease='Hypothermia'))

# 12
    @Rule(Fact(findDisease='true'),
          Fact(memory_loss='n'),
          Fact(confusion='n'),
          Fact(drowsiness='y'),
          Fact(joint_pain='n'),
          Fact(stiffness='n'),
          Fact(back_pain='n'),
          Fact(wheezing='n'),
          Fact(shortness_of_breath='n'),
          Fact(chest_tightness='n'),
          Fact(anxiety='n'),
          Fact(fever='y'),
          Fact(cough='n'),
          Fact(fatigue='n'),
          Fact(excessive_thirst='n'),
          Fact(seizures='n'),
          Fact(headache='n'),
          Fact(eye_pain='n'),
          Fact(blurred_vision='n'),
          Fact(chest_pain='n'),
          Fact(dizziness='n'),
          Fact(weakness='n'),
          Fact(sweating='n'),
          Fact(shivering='n'),
          Fact(nasal_congestion='n'),
          Fact(yellowing_skin='y'))
    def disease_11(self):
        self.declare(Fact(disease='Jaundice'))

# 13
    @Rule(Fact(findDisease='true'),
          Fact(memory_loss='n'),
          Fact(confusion='n'),
          Fact(drowsiness='n'),
          Fact(joint_pain='n'),
          Fact(stiffness='n'),
          Fact(back_pain='n'),
          Fact(wheezing='n'),
          Fact(shortness_of_breath='n'),
          Fact(chest_tightness='n'),
          Fact(anxiety='n'),
          Fact(fever='y'),
          Fact(cough='n'),
          Fact(fatigue='n'),
          Fact(excessive_thirst='n'),
          Fact(seizures='n'),
          Fact(headache='y'),
          Fact(eye_pain='n'),
          Fact(blurred_vision='n'),
          Fact(chest_pain='n'),
          Fact(dizziness='n'),
          Fact(weakness='n'),
          Fact(sweating='n'),
          Fact(shivering='n'),
          Fact(nasal_congestion='y'),
          Fact(yellowing_skin='n'))
    def disease_12(self):
        self.declare(Fact(disease='Sinusitis'))

# 14
    @Rule(Fact(findDisease='true'),
          Fact(memory_loss='n'),
          Fact(confusion='n'),
          Fact(drowsiness='n'),
          Fact(joint_pain='n'),
          Fact(stiffness='n'),
          Fact(back_pain='n'),
          Fact(wheezing='n'),
          Fact(shortness_of_breath='n'),
          Fact(chest_tightness='y'),
          Fact(anxiety='n'),
          Fact(fever='y'),
          Fact(cough='y'),
          Fact(fatigue='y'),
          Fact(excessive_thirst='n'),
          Fact(seizures='n'),
          Fact(headache='n'),
          Fact(eye_pain='n'),
          Fact(blurred_vision='n'),
          Fact(chest_pain='n'),
          Fact(dizziness='n'),
          Fact(weakness='n'),
          Fact(sweating='n'),
          Fact(shivering='n'),
          Fact(nasal_congestion='n'),
          Fact(yellowing_skin='n'))
    def disease_13(self):
        self.declare(Fact(disease='Tuberculosis'))

# 15
    @Rule(Fact(findDisease='true'),
          Fact(memory_loss='n'),
          Fact(confusion='n'),
          Fact(drowsiness='y'),
          Fact(joint_pain='n'),
          Fact(stiffness='n'),
          Fact(back_pain='n'),
          Fact(wheezing='n'),
          Fact(shortness_of_breath='n'),
          Fact(chest_tightness='n'),
          Fact(anxiety='y'),
          Fact(fever='n'),
          Fact(cough='n'),
          Fact(fatigue='n'),
          Fact(excessive_thirst='n'),
          Fact(seizures='n'),
          Fact(headache='y'),
          Fact(eye_pain='n'),
          Fact(blurred_vision='n'),
          Fact(chest_pain='n'),
          Fact(dizziness='n'),
          Fact(weakness='y'),
          Fact(sweating='n'),
          Fact(shivering='n'),
          Fact(nasal_congestion='n'),
          Fact(yellowing_skin='n'))
    def disease_14(self):
        self.declare(Fact(disease='Migraine'))

# 16
    @Rule(Fact(findDisease='true'),
          Fact(memory_loss='n'),
          Fact(confusion='n'),
          Fact(drowsiness='n'),
          Fact(joint_pain='n'),
          Fact(stiffness='n'),
          Fact(back_pain='n'),
          Fact(wheezing='n'),
          Fact(shortness_of_breath='n'),
          Fact(chest_tightness='y'),
          Fact(anxiety='n'),
          Fact(fever='y'),
          Fact(cough='y'),
          Fact(fatigue='n'),
          Fact(excessive_thirst='n'),
          Fact(seizures='n'),
          Fact(headache='n'),
          Fact(eye_pain='n'),
          Fact(blurred_vision='n'),
          Fact(chest_pain='n'),
          Fact(dizziness='n'),
          Fact(weakness='n'),
          Fact(sweating='n'),
          Fact(shivering='n'),
          Fact(nasal_congestion='n'),
          Fact(yellowing_skin='n'))
    def disease_15(self):
        self.declare(Fact(disease='Pneumonia'))

# 17
    @Rule(Fact(findDisease='true'),
          Fact(memory_loss='n'),
          Fact(confusion='n'),
          Fact(drowsiness='n'),
          Fact(joint_pain='n'),
          Fact(stiffness='n'),
          Fact(back_pain='n'),
          Fact(wheezing='n'),
          Fact(shortness_of_breath='n'),
          Fact(chest_tightness='y'),
          Fact(anxiety='n'),
          Fact(fever='n'),
          Fact(cough='y'),
          Fact(fatigue='y'),
          Fact(excessive_thirst='n'),
          Fact(seizures='n'),
          Fact(headache='n'),
          Fact(eye_pain='n'),
          Fact(blurred_vision='n'),
          Fact(chest_pain='n'),
          Fact(dizziness='n'),
          Fact(weakness='n'),
          Fact(sweating='n'),
          Fact(shivering='n'),
          Fact(nasal_congestion='n'),
          Fact(yellowing_skin='n'))
    def disease_16(self):
        self.declare(Fact(disease='Bronchitis'))

# 18
    @Rule(Fact(findDisease='true'),
          Fact(memory_loss='n'),
          Fact(confusion='n'),
          Fact(drowsiness='n'),
          Fact(joint_pain='n'),
          Fact(stiffness='n'),
          Fact(back_pain='n'),
          Fact(wheezing='n'),
          Fact(shortness_of_breath='n'),
          Fact(chest_tightness='n'),
          Fact(anxiety='n'),
          Fact(fever='n'),
          Fact(cough='n'),
          Fact(fatigue='y'),
          Fact(excessive_thirst='n'),
          Fact(seizures='n'),
          Fact(headache='y'),
          Fact(eye_pain='n'),
          Fact(blurred_vision='n'),
          Fact(chest_pain='n'),
          Fact(dizziness='y'),
          Fact(weakness='y'),
          Fact(sweating='n'),
          Fact(shivering='n'),
          Fact(nasal_congestion='n'),
          Fact(yellowing_skin='n'))
    def disease_17(self):
        self.declare(Fact(disease='Anemia'))

# 19
    @Rule(Fact(findDisease='true'),
          Fact(memory_loss='n'),
          Fact(confusion='n'),
          Fact(drowsiness='y'),
          Fact(joint_pain='n'),
          Fact(stiffness='n'),
          Fact(back_pain='n'),
          Fact(wheezing='n'),
          Fact(shortness_of_breath='n'),
          Fact(chest_tightness='n'),
          Fact(anxiety='y'),
          Fact(fever='n'),
          Fact(cough='n'),
          Fact(fatigue='y'),
          Fact(excessive_thirst='n'),
          Fact(seizures='n'),
          Fact(headache='n'),
          Fact(eye_pain='n'),
          Fact(blurred_vision='n'),
          Fact(chest_pain='n'),
          Fact(dizziness='n'),
          Fact(weakness='n'),
          Fact(sweating='n'),
          Fact(shivering='n'),
          Fact(nasal_congestion='n'),
          Fact(yellowing_skin='n'))
    def disease_18(self):
        self.declare(Fact(disease='Depression'))

# 20
    @Rule(Fact(findDisease='true'),
          Fact(memory_loss='n'),
          Fact(confusion='n'),
          Fact(drowsiness='y'),
          Fact(joint_pain='n'),
          Fact(stiffness='n'),
          Fact(back_pain='n'),
          Fact(wheezing='n'),
          Fact(shortness_of_breath='n'),
          Fact(chest_tightness='y'),
          Fact(anxiety='y'),
          Fact(fever='n'),
          Fact(cough='n'),
          Fact(fatigue='n'),
          Fact(excessive_thirst='n'),
          Fact(seizures='n'),
          Fact(headache='n'),
          Fact(eye_pain='n'),
          Fact(blurred_vision='n'),
          Fact(chest_pain='n'),
          Fact(dizziness='n'),
          Fact(weakness='n'),
          Fact(sweating='n'),
          Fact(shivering='n'),
          Fact(nasal_congestion='n'),
          Fact(yellowing_skin='n'))
    def disease_19(self):
        self.declare(Fact(disease='Anxiety Disorder'))

    @Rule(Fact(findDisease='true'), Fact(disease=MATCH.disease), salience=1)

    @Rule(Fact(findDisease='true'), NOT(Fact(disease=W())))
    def no_match(self):
        self.disease = "unknown"

    # Tìm bệnh từ triệu chứng khi không khớp
    def analyze_unknown(self, answers):
        try:
            with open("disease_symptoms.txt", "r", encoding="utf-8") as file:
                dictionary = ast.literal_eval(file.read())
        except FileNotFoundError:
            return "Không tìm thấy file dữ liệu triệu chứng.", []

        yes_symptoms = [k for k, v in answers.items() if v == 'y']

        max_match = 0
        best_match_disease = "Bạn đang hoàn toàn khỏe mạnh."
        possible_diseases = []

        for disease, symptoms in dictionary.items():
            symptom_list = symptoms.split(",")
            match_count = sum(1 for symptom in yes_symptoms if symptom in symptom_list)

            if match_count > 0:
                possible_diseases.append((disease, match_count))
            if match_count > max_match:
                max_match = match_count
                best_match_disease = disease

        possible_diseases.sort(key=lambda x: x[1], reverse=True)
        return best_match_disease, possible_diseases

    # Đọc file mô tả và cách chữa bệnh
    def get_disease_info(self, disease_name):
        try:
              with open(f"disease/disease_descriptions/{disease_name}.txt", "r", encoding="utf-8") as f:
                description = f.read()
        except FileNotFoundError:
            description = "Không có thông tin mô tả bệnh."

        try:
           with open(f"disease/disease_treatments/{disease_name}.txt", "r", encoding="utf-8") as f:
                treatment = f.read()
        except FileNotFoundError:
            treatment = "Không có thông tin điều trị bệnh."

        return description, treatment

# Lớp giao diện Tkinter
class MedicalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hệ Thống Chẩn Đoán Bệnh")
        self.root.geometry("500x300")
        self.engine = MedicalExpert()
        self.username = ""
        # Tên bệnh tiếng Việt
        self.disease_mapping = {
            'Alzheimer': 'bệnh suy giảm trí nhớ Alzheimer',
            'Arthritis': 'bệnh viêm khớp',
            'Asthma': 'bệnh hen suyễn',
            'Covid': 'covid',
            'Diabates': 'bệnh tiểu đường',
            'Epilepsy': 'bệnh động kinh',
            'Glaucoma': 'bệnh tăng nhãn áp',
            'Heart desease': 'bệnh tim',
            'Heat stroke': 'bệnh sốc nhiệt',
            'Hyperthyroidism': 'bệnh cường giáp',
            'Hypothermia': 'bệnh hạ thân nhiệt',
            'Jaundice': 'bệnh vàng da',
            'Sinusitis': 'bệnh viêm xoang',
            'Tuberculosis': 'bệnh lao',
            'Migraine': 'đau nửa đầu',
            'Pneumonia': 'bệnh viêm phổi',
            'Bronchitis': 'bệnh viêm phế quản',
            'Anemia': 'bệnh thiếu máu',
            'Depression': 'bệnh trầm cảm',
            'Anxiety Disorder': 'bệnh rối loạn lo âu'
        }
        # Danh sách câu hỏi
        self.questions = [
            {"text": "Bạn có bị mất trí nhớ không?", "key": "memory_loss"},
            {"text": "Bạn có bị rối loạn nhận thức không?", "key": "confusion"},
            {"text": "Bạn có thường xuyên buồn ngủ không?", "key": "drowsiness"},
            {"text": "Bạn có bị ho không?", "key": "cough"},
            {"text": "Bạn có bị sốt không?", "key": "fever"},
            {"text": "Bạn có cảm thấy tức ngực không?", "key": "chest_tightness"},
            {"text": "Bạn có cảm thấy mệt mỏi không?", "key": "fatigue"},
            {"text": "Bạn có bị đau đầu không?", "key": "headache"},
            {"text": "Bạn có thấy cơ thể yếu đi không?", "key": "weakness"},
            {"text": "Bạn có thường xuyên lo âu không?", "key": "anxiety"},
            {"text": "Bạn có bị đau lưng không?", "key": "back_pain"},
            {"text": "Bạn có thấy các khớp của mình đau không?", "key": "joint_pain"},
            {"text": "Bạn có cảm thấy các khớp khó di chuyển không?", "key": "stiffness"},
            {"text": "Bạn có cảm thấy tiếng thở của mình như khò khè không?", "key": "wheezing"},
            {"text": "Bạn có cảm thấy khó thở không?", "key": "shortness_of_breath"},
            {"text": "Bạn có thấy tần suất khát nước trong một ngày nhiều lên không?", "key": "excessive_thirst"},
            {"text": "Bạn có tiền sử bị co giật không?", "key": "seizures"},
            {"text": "Bạn có cảm thấy đau mắt không?", "key": "eye_pain"},
            {"text": "Bạn có cảm thấy thỉnh thoảng mắt mờ đi không?", "key": "blurred_vision"},
            {"text": "Bạn có cảm thấy đau ngực không?", "key": "chest_pain"},
            {"text": "Bạn đổ mồ hôi nhiều không?", "key": "sweating"},
            {"text": "Bạn có cảm bị nghẹt mũi không?", "key": "nasal_congestion"},
            {"text": "Bạn có hay cảm thấy chóng mặt không?", "key": "dizziness"},
            {"text": "Bạn có thấy tròng mắt và da mình vàng hơn bình thường không?", "key": "yellowing_skin"},
            {"text": "Bạn có cảm thấy rùng mình hoặc cơ thể run rẩy không?", "key": "shivering"},
        ]

        self.current_question = 0
        self.answers = {}
        self.create_name_entry()
        

    def create_name_entry(self):
        # Giao diện nhập tên
        self.title_label = tk.Label(self.root, text="Chào mừng đến với hệ thống chẩn đoán bệnh!", font=("Arial", 16), fg="blue")
        self.title_label.pack(pady=20)

        self.name_label = tk.Label(self.root, text="Mời bạn nhập tên:", font=("Arial", 12))
        self.name_label.pack()

        self.name_entry = tk.Entry(self.root, font=("Arial", 12))
        self.name_entry.pack(pady=10)

        self.start_button = tk.Button(self.root, text="Bắt đầu", command=self.start_diagnosis, font=("Arial", 12))
        self.start_button.pack(pady=10)

    def start_diagnosis(self):
        # Lấy tên từ ô nhập liệu
        self.username = self.name_entry.get().strip()

        # Kiểm tra nếu tên bị trống
        if not self.username:
            tk.messagebox.showwarning("Cảnh báo", "Vui lòng nhập tên của bạn trước khi bắt đầu!")
            return
        
        

        # Xóa giao diện nhập tên
        self.title_label.pack_forget()
        self.name_label.pack_forget()
        self.name_entry.pack_forget()
        self.start_button.pack_forget()


        for widget in self.root.winfo_children():
            widget.destroy()
        # Hiển thị giao diện câu hỏi
        self.create_widgets()



    def create_widgets(self):
        # Tiêu đề
        self.title_label = tk.Label(self.root, text="Hệ Thống Chẩn Đoán Bệnh", font=("Arial", 16), fg="blue")
        self.title_label.pack(pady=10)

         # Hiển thị tên người dùng
        self.name_label = tk.Label(self.root, text=f"Chào bạn: {self.username}", font=("Arial", 12), fg="green")
        self.name_label.pack(pady=5)

        # Hiển thị câu hỏi
        self.question_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.question_label.pack(pady=10)

        # Radiobutton cho câu trả lời
        self.answer_var = tk.StringVar(value="n")
        self.yes_button = tk.Radiobutton(self.root, text="Có", variable=self.answer_var, value="y", font=("Arial", 10))
        self.no_button = tk.Radiobutton(self.root, text="Không", variable=self.answer_var, value="n", font=("Arial", 10))
        self.yes_button.pack()
        self.no_button.pack()

        # Nút tiếp tục
        self.next_button = tk.Button(self.root, text="Tiếp tục", command=self.next_question, font=("Arial", 10))
        self.next_button.pack(pady=10)

        # Hiển thị câu hỏi đầu tiên
        self.display_question()

    def display_question(self):
        if self.current_question < len(self.questions):
            self.question_label.config(text=self.questions[self.current_question]["text"])
        else:
            self.finish_diagnosis()


    def next_question(self):
        # Lưu câu trả lời cho câu hỏi hiện tại
        if self.current_question < len(self.questions):
            key = self.questions[self.current_question]["key"]
            self.answers[key] = self.answer_var.get()

        # Tăng chỉ số câu hỏi
        self.current_question += 1

        # Kiểm tra giới hạn và gọi display_question
        if self.current_question < len(self.questions):
            self.display_question()
        else:
            self.finish_diagnosis()


    def finish_diagnosis(self):
        """
        Xử lý kết quả chẩn đoán và hiển thị cho người dùng.
        """
        # Chạy engine và truyền dữ liệu
        self.engine.reset()
        for key, value in self.answers.items():
            self.engine.declare(Fact(**{key: value}))
        self.engine.run()

        # Kiểm tra bệnh đã xác định hay chưa
        disease_name = self.engine.disease

        # Tra cứu tên bệnh tiếng Việt
        vietnamese_name = self.disease_mapping.get(disease_name, "Không xác định")

        if disease_name == "unknown":
            # Dự đoán bệnh phù hợp nhất khi không có kết quả chính xác
            best_match, _ = self.engine.analyze_unknown(self.answers)
            vietnamese_match = self.disease_mapping.get(best_match, best_match)
            description, treatment = self.engine.get_disease_info(best_match)

            messagebox.showinfo(
                "Kết Quả Chẩn Đoán",
                f"Chào {self.username}!\n\nDự đoán bệnh phù hợp nhất: {vietnamese_match}\n\n"
                f"Mô tả bệnh:\n{description}\n\nCách điều trị:\n{treatment}"
            )
        else:
            # Hiển thị kết quả bệnh chính xác
            description, treatment = self.engine.get_disease_info(disease_name)
            messagebox.showinfo(
                "Kết Quả Chẩn Đoán",
                f"Chào {self.username}!\n\nBạn có thể đang mắc bệnh: {vietnamese_name}\n\n"
                f"Mô tả bệnh:\n{description}\n\nCách điều trị:\n{treatment}"
            )

        # Hỏi người dùng có muốn làm lại không
        self.ask_for_restart()

    
    def ask_for_restart(self):
        # Hỏi người dùng có muốn làm lại hay không
        result = messagebox.askyesno("Tiếp tục?", "Bạn có muốn thực hiện lại chẩn đoán không?")
        if result:
            self.reset_diagnosis()
        else:
            self.root.quit()  # Thoát chương trình

    def reset_diagnosis(self):
        # Reset lại giao diện và bắt đầu lại
        self.current_question = 0
        self.answers = {}
        self.display_question()

# Chạy ứng dụng
if __name__ == "__main__":
    root = tk.Tk()
    app = MedicalApp(root)
    root.mainloop()
