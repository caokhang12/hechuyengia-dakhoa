from experta import *
import ast


class MedicalExpert(KnowledgeEngine):
    username = "",

    @DefFacts()
    def needed_data(self):

        yield Fact(findDisease='true')
        print("Xin chào!! Đây là hệ thống chẩn đoán lâm sàng. \n\nBạn có thể tự chẩn đoán miễn phí \ntôi sẽ đưa ra cho bạn một vài câu hỏi:\n\n")

# xây dựng sự kiện
# 0
    @Rule(Fact(findDisease='true'), NOT(Fact(name=W())), salience=1000)
    def ask_name(self):
        self.username = input("Mời nhập tên của bạn?\n")
        self.declare(Fact(name=self.username))

# 1
    @Rule(Fact(findDisease='true'), NOT(Fact(memoryLoss=W())), salience=995)
    def hasMemoryLoss(self):
        self.memory_loss = input(
            "\nBạn có từng quên mình đang ở đâu hoặc không biết thời gian chính xác không? \nMời nhập Y (Có) / N (Không)\n")
        self.memory_loss = self.memory_loss.lower()
        self.declare(Fact(memoryLoss=self.memory_loss.strip().lower()))

# 2
    @Rule(Fact(findDisease='true'), NOT(Fact(cough=W())), salience=985)
    def hasCough(self):
        self.cough = input(
            "\nBạn có bị ho không?\nMời nhập Y (Có) / N (Không)\n")
        self.cough = self.cough.lower()
        self.declare(Fact(cough=self.cough.strip().lower()))

# 3
    @Rule(Fact(findDisease='true'), NOT(Fact(confusion=W())), salience=975)
    def hasConfusion(self):
        self.confusion = input(
            "\nGần đây bạn có cảm thấy lo lắng, buồn bã hoặc cáu kỉnh nhiều hơn bình thường và thay đổi liên tục không?\nMời nhập Y (Có) / N (Không)\n")
        self.confusion = self.confusion.lower()
        self.declare(Fact(confusion=self.confusion.strip().lower()))

# 4

    @Rule(Fact(findDisease='true'), NOT(Fact(fatigue=W())), salience=970)
    def hasFatigue(self):
        self.fatigue = input(
            "\nBạn có thỉnh thoảng thấy mệt mỏi không?\nMời nhập Y (Có) / N (Không)\n")
        self.fatigue = self.fatigue.lower()
        self.declare(Fact(fatigue=self.fatigue.strip().lower()))

# 5
    @Rule(Fact(findDisease='true'), NOT(Fact(headache=W())), salience=965)
    def hasHeadache(self):
        self.headache = input(
            "\nBạn có bị đau đầu không?\nMời nhập Y (Có) / N (Không)\n")
        self.headache = self.headache.lower()
        self.declare(Fact(headache=self.headache.strip().lower()))

# 6
    @Rule(Fact(findDisease='true'), NOT(Fact(back_pain=W())), salience=955)
    def hasbackPain(self):
        self.back_pain = input(
            "\nBạn có bị đau lưng không?\nMời nhập Y (Có) / N (Không)\n")
        self.back_pain = self.back_pain.lower()
        self.declare(Fact(back_pain=self.back_pain.strip().lower()))

# 7
    @Rule(Fact(findDisease='true'), NOT(Fact(drowsiness=W())), salience=950)
    def hasDrowsiness(self):
        self.drowsiness = input(
            "\nBạn có thấy buồn ngủ với tần suất nhiều trong ngày không?\nMời nhập Y (Có) / N (Không)\n")
        self.drowsiness = self.drowsiness.lower()
        self.declare(Fact(drowsiness=self.drowsiness.strip().lower()))

# 8
    @Rule(Fact(findDisease='true'), NOT(Fact(fever=W())), salience=945)
    def hasfever(self):
        self.fever = input(
            "\nBạn có bị sốt không?\nMời nhập Y (Có) / N (Không)\n")
        self.fever = self.fever.lower()
        self.declare(Fact(fever=self.fever.strip().lower()))

# 9
    @Rule(Fact(findDisease='true'), NOT(Fact(joint_pain=W())), salience=940)
    def hasJointpain(self):
        self.joint_pain = input(
            "\nBạn có thấy các khớp của mình đau không?\nMời nhập Y (Có) / N (Không)\n")
        self.joint_pain = self.joint_pain.lower()
        self.declare(Fact(joint_pain=self.joint_pain.strip().lower()))

# 10
    @Rule(Fact(findDisease='true'), NOT(Fact(stiffness=W())), salience=935)
    def hasStiffness(self):
        self.stiffness = input(
            "\nBạn có cảm thấy các khớp khó di chuyển không?\nMời nhập Y (Có) / N (Không)\n")
        self.stiffness = self.stiffness.lower()
        self.declare(Fact(stiffness=self.stiffness.strip().lower()))

# 11
    @Rule(Fact(findDisease='true'), NOT(Fact(wheezing=W())), salience=925)
    def hasWheezing(self):
        self.wheezing = input(
            "\nBạn có cảm thấy tiếng thở của mình như khò khè không?\nMời nhập Y (Có) / N (Không)\n")
        self.wheezing = self.wheezing.lower()
        self.declare(Fact(wheezing=self.wheezing.strip().lower()))

# 12
    @Rule(Fact(findDisease='true'), NOT(Fact(shortness_of_breath=W())), salience=930)
    def hasShortnessOfBreath(self):
        self.shortness_of_breath = input(
            "\nBạn có cảm thấy khó thở không?\nMời nhập Y (Có) / N (Không)\n")
        self.shortness_of_breath = self.shortness_of_breath.lower()
        self.declare(
            Fact(shortness_of_breath=self.shortness_of_breath.strip().lower()))

# 13
    @Rule(Fact(findDisease='true'), NOT(Fact(chest_tightness=W())), salience=920)
    def hasChestTightness(self):
        self.chest_tightness = input(
            "\nBạn có cảm thấy tức ngực không?\nMời nhập Y (Có) / N (Không)\n")
        self.chest_tightness = self.chest_tightness.lower()
        self.declare(
            Fact(chest_tightness=self.chest_tightness.strip().lower()))

# 14
    @Rule(Fact(findDisease='true'), NOT(Fact(anxiety=W())), salience=915)
    def hasAnxiety(self):
        self.anxiety = input(
            "\nBạn có hay lo lắng trong khoảng thời gian dài hoặc lo lắng mà không rõ lý do không?\nMời nhập Y (Có) / N (Không)\n")
        self.anxiety = self.anxiety.lower()
        self.declare(Fact(anxiety=self.anxiety.strip().lower()))

# 15
    @Rule(Fact(findDisease='true'), NOT(Fact(excessive_thirst=W())), salience=910)
    def hasExcessiveThirst(self):
        self.excessive_thirst = input(
            "\nBạn có thấy tần suất khát nước trong một ngày nhiều lên không?\nMời nhập Y (Có) / N (Không)\n")
        self.excessive_thirst = self.excessive_thirst.lower()
        self.declare(
            Fact(excessive_thirst=self.excessive_thirst.strip().lower()))

# 16
    @Rule(Fact(findDisease='true'), NOT(Fact(seizures=W())), salience=905)
    def hasSeizures(self):
        self.seizures = input(
            "\nBạn có tiền sử bị co giật không?\nMời nhập Y (Có) / N (Không)\n")
        self.seizures = self.seizures.lower()
        self.declare(Fact(seizures=self.seizures.strip().lower()))

# 17
    @Rule(Fact(findDisease='true'), NOT(Fact(eye_pain=W())), salience=900)
    def hasEyePain(self):
        self.eye_pain = input(
            "\nBạn có cảm thấy đau mắt không?\nMời nhập Y (Có) / N (Không)\n")
        self.eye_pain = self.eye_pain.lower()
        self.declare(Fact(eye_pain=self.eye_pain.strip().lower()))

# 18
    @Rule(Fact(findDisease='true'), NOT(Fact(blurred_vision=W())), salience=895)
    def hasBlurredVision(self):
        self.blurred_vision = input(
            "\nBạn có cảm thấy thỉnh thoảng mắt mờ đi không?\nMời nhập Y (Có) / N (Không)\n")
        self.blurred_vision = self.blurred_vision.lower()
        self.declare(Fact(blurred_vision=self.blurred_vision.strip().lower()))

# 19
    @Rule(Fact(findDisease='true'), NOT(Fact(chest_pain=W())), salience=890)
    def hasChestPain(self):
        self.chest_pain = input(
            "\nBạn có cảm thấy đau ngực không?\nMời nhập Y (Có) / N (Không)\n")
        self.chest_pain = self.chest_pain.lower()
        self.declare(Fact(chest_pain=self.chest_pain.strip().lower()))

# 20
    @Rule(Fact(findDisease='true'), NOT(Fact(weakness=W())), salience=885)
    def hasWeakness(self):
        self.weakness = input(
            "\nBạn có cảm thấy cơ thể mình nhiều lúc bị mất lực không?\nMời nhập Y (Có) / N (Không)\n")
        self.weakness = self.weakness.lower()
        self.declare(Fact(weakness=self.weakness.strip().lower()))

# 21
    @Rule(Fact(findDisease='true'), NOT(Fact(sweating=W())), salience=880)
    def hasSweating(self):
        self.sweating = input(
            "\nBạn đổ mồ hôi nhiều không?\nMời nhập Y (Có) / N (Không)\n")
        self.sweating = self.sweating.lower()
        self.declare(Fact(sweating=self.sweating.strip().lower()))

# 22
    @Rule(Fact(findDisease='true'), NOT(Fact(shivering=W())), salience=875)
    def hasShivering(self):
        self.shivering = input(
            "\nBạn có cảm thấy rùng mình hoặc cơ thể run rẩy không?\nMời nhập Y (Có) / N (Không)\n")
        self.shivering = self.shivering.lower()
        self.declare(Fact(shivering=self.shivering.strip().lower()))

# 23
    @Rule(Fact(findDisease='true'), NOT(Fact(nasal_congestion=W())), salience=870)
    def hasNasalCongestion(self):
        self.nasal_congestion = input(
            "\nBạn có cảm bị nghẹt mũi không?\nMời nhập Y (Có) / N (Không)\n")
        self.nasal_congestion = self.nasal_congestion.lower()
        self.declare(
            Fact(nasal_congestion=self.nasal_congestion.strip().lower()))

# 24
    @Rule(Fact(findDisease='true'), NOT(Fact(dizziness=W())), salience=865)
    def hasDizziness(self):
        self.dizziness = input(
            "\nBạn có hay cảm thấy chóng mặt không?\nMời nhập Y (Có) / N (Không)\n")
        self.dizziness = self.dizziness.lower()
        self.declare(Fact(dizziness=self.dizziness.strip().lower()))

# 25
    @Rule(Fact(findDisease='true'), NOT(Fact(yellowing_skin=W())), salience=860)
    def hasYellowingSkin(self):
        self.yellowing_skin = input(
            "\nBạn có thấy tròng mắt và da mình vàng hơn bình thường không?\nMời nhập Y (Có) / N (Không)\n")
        self.yellowing_skin = self.yellowing_skin.lower()
        self.declare(Fact(yellowing_skin=self.yellowing_skin.strip().lower()))

# 26
    @Rule(Fact(findDisease='true'), NOT(Fact(disease=W())), salience=-1)
    def unmatched(self):
        self.declare(Fact(disease='unknown'))

# # 27
#     @Rule(Fact(findDisease='true'), NOT(Fact(disease=W())), salience=-1)
#     def allYes(self):
#         self.declare(Fact(disease='warning'))

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
    def getDisease(self, disease):

        vietnamese_symptoms = {
            'memory_loss': 'mất trí nhớ',
            'confusion': 'rối loạn nhận thức',
            'drowsiness': 'buồn ngủ',
            'joint_pain': 'đau khớp',
            'stiffness': 'cứng khớp',
            'back_pain': 'đau lưng',
            'wheezing': 'thở khò khè',
            'shortness_of_breath': 'khó thở',
            'chest_tightness': 'tức ngực',
            'anxiety': 'lo âu',
            'fever': 'sốt',
            'cough': 'ho',
            'fatigue': 'mệt mỏi',
            'excessive_thirst': 'khát nước nhiều',
            'seizures': 'co giật',
            'headache': 'đau đầu',
            'eye_pain': 'đau mắt',
            'blurred_vision': 'mờ mắt',
            'chest_pain': 'đau ngực',
            'dizziness': 'chóng mặt',
            'weakness': 'suy nhược',
            'sweating': 'đổ mồ hôi',
            'shivering': 'run rẩy',
            'nasal_congestion': 'nghẹt mũi',
            'yellowing_skin': 'vàng da'

        }

        vietnamese_disease = {
            'alzheimer': 'bệnh suy giảm trí nhớ Alzheimer',
            'arthritis': 'bệnh viêm khớp',
            'asthma': 'bệnh hen suyễn',
            'Covid': 'covid',
            'diabates': 'bệnh tiểu đường',
            'epilepsy': 'bệnh động kinh',
            'glaucoma': 'bệnh tăng nhãn áp',
            'heart desease': 'bệnh tim',
            'heat stroke': 'bệnh sốc nhiệt',
            'hyperthyroidism': 'bệnh cường giáp',
            'hypothermia': 'bệnh hạ thân nhiệt',
            'jaundice': 'bệnh vàng da',
            'sinusitis': 'bệnh viêm xoang',
            'tuberculosis': 'bệnh lao',
            'migraine': 'đau nửa đầu',
            'pneumonia': 'bệnh viêm phổi',
            'bronchitis': 'bệnh viêm phế quản',
            'anemia': 'bệnh thiếu máu',
            'depression': 'bệnh trầm cảm',
            'anxiety Disorder': 'bệnh rối loạn lo âu'
        }

        if (disease == 'unknown'):
            mapDisease = []
            mapDisease.append('memory_loss')
            mapDisease.append('confusion')
            mapDisease.append('drowsiness')
            mapDisease.append('joint_pain')
            mapDisease.append('stiffness')
            mapDisease.append('back_pain')
            mapDisease.append('wheezing')
            mapDisease.append('shortness_of_breath')
            mapDisease.append('chest_tightness')
            mapDisease.append('anxiety')
            mapDisease.append('fever')
            mapDisease.append('cough')
            mapDisease.append('fatigue')
            mapDisease.append('excessive_thirst')
            mapDisease.append('seizures')
            mapDisease.append('headache')
            mapDisease.append('eye_pain')
            mapDisease.append('blurred_vision')
            mapDisease.append('chest_pain')
            mapDisease.append('dizziness')
            mapDisease.append('weakness')
            mapDisease.append('sweating')
            mapDisease.append('shivering')
            mapDisease.append('nasal_congestion')
            mapDisease.append('yellowing_skin')

            mapDisease_vn = [vietnamese_symptoms[symptom]
                             for symptom in mapDisease]
            print('\n\nCác triệu chứng đã kiểm tra:', mapDisease_vn)
            mapDisease_val = [self.memory_loss,
                              self.confusion,
                              self.drowsiness,
                              self.joint_pain,
                              self.stiffness,
                              self.back_pain,
                              self.wheezing,
                              self.shortness_of_breath,
                              self.chest_tightness,
                              self.anxiety,
                              self.fever,
                              self.cough,
                              self.fatigue,
                              self.excessive_thirst,
                              self.seizures,
                              self.headache,
                              self.eye_pain,
                              self.blurred_vision,
                              self.chest_pain,
                              self.dizziness,
                              self.weakness,
                              self.sweating,
                              self.shivering,
                              self.nasal_congestion,
                              self.yellowing_skin]

            print('\n\nNhững triệu chứng bạn cung cấp :', mapDisease_val)

            file = open("disease_symptoms.txt", "r")
            contents = file.read()
            dictionary = ast.literal_eval(contents)
            file.close()

            yes_symptoms = []
            for i in range(0, len(mapDisease_val)):
                if mapDisease_val[i] == 'y':
                    yes_symptoms.append(mapDisease[i])

            max_val = 0
            yes_symptoms_vn = [vietnamese_symptoms[symptom]
                               for symptom in yes_symptoms]
            print('\n\nNhững triệu chứng đã phát hiện: ', yes_symptoms_vn)
            possible_diseases = []
            for key in dictionary.keys():
                val = dictionary[key].split(",")
                count = 0
                # print(key, ":", val)
                for x in val:
                    if x in yes_symptoms:
                        count += 1
                # print('Count:',count)
                if count > 0:
                    possible_diseases.append(key)
                if count > max_val:
                    max_val = count
                    pred_dis = key

            if max_val == 0:
                print("không có triệu chứng nào? Bạn thật khỏe mạnh!!")

            # if len(possible_diseases) > 0:
            #     print("\n\nCác bệnh bạn có thể đang mắc phải:")
            #     print(
            #         '\n_________________________________________________________________________________________________')
            #     for disease in possible_diseases:
            #         disease_vn = vietnamese_disease.get(
            #             disease.strip().lower(), disease)

            #         # print("Các bệnh có thể xảy ra:", possible_diseases)
            #         # print("Từ điển tên bệnh tiếng Việt:", disease_vn)
            #         print(disease_vn)
            #         print('\nMột vài thông tin về bệnh:', disease_vn)
            #         f = open("disease/disease_descriptions/" +
            #                  disease + ".txt", "r", encoding="utf8")
            #         print(f.read())
            #         print(
            #             '_________________________________________________________________________________________________')
            #         print('\nĐừng quá lo lắng', self.username,
            #               '. Tôi có một số giải pháp dành cho bạn!\n')
            #         f = open("disease/disease_treatments/" +
            #                  disease + ".txt", "r", encoding="utf8")
            #         print(f.read())
            #         print(
            #             '\n_________________________________________________________________________________________________')
            else:
                if (len(possible_diseases)) > 18:
                    print(
                        'tôi rất tiếc về trường hợp của bạn, có lẽ bạn nên liên hệ luật sư để viết di chúc')
                else:
                    pred_dis_vn = vietnamese_disease.get(
                        pred_dis.strip().lower(), pred_dis)
                    # print(len(possible_diseases))
                    print(
                        "\n\nTôi không thể chẩn đoán một cách chính xác bệnh mà bạn đang mắc phải, dự đoán cho thấy rằng bạn có thể đang mắc phải bệnh:", pred_dis_vn)

                    print(
                        '\n_________________________________________________________________________________________________')

                    print('\n\nMột vài thông tin về bệnh:', pred_dis_vn)

                    f = open("disease/disease_descriptions/" +
                             pred_dis + ".txt", "r")
                    print(f.read())
                    print(
                        '_________________________________________________________________________________________________ ')
                    print('\n\nĐừng quá lo lắng ', self.username,
                          '. Tôi có một số giải pháp dành cho bạn!\n')
                    f = open("disease/disease_treatments/" +
                             pred_dis + ".txt", "r")
                    print(f.read())
                    print(
                        '\n_________________________________________________________________________________________________ ')
        else:
            disease_vn = vietnamese_disease.get(
                disease.strip().lower(), disease)
            print('Bạn có thể đang mắc phải bệnh này: ', disease_vn)
            print('\n\n')
            print(
                '\n_________________________________________________________________________________________________ ')
            print('Một vài thông tin về bệnh:\n')
            print(disease_vn)
            f = open("disease/disease_descriptions/" +
                     disease + ".txt", "r")
            print(f.read())
            print(
                '\n_________________________________________________________________________________________________ ')
            print('\n\nĐừng quá lo lắng ', self.username,
                  '. Tôi có một số giải pháp dành cho bạn!\n')
            f = open("disease/disease_treatments/" + disease + ".txt", "r")
            print(f.read())


if __name__ == "__main__":
    while True:
        engine = MedicalExpert()
        engine.reset()

        engine.run()

        # Hỏi người dùng có muốn tiếp tục không
        continue_diagnosis = input(
            "Bạn có muốn tiếp tục không (y/n)? ").strip().lower()
        if continue_diagnosis != 'y':
            print("Cảm ơn bạn đã sử dụng hệ thống chẩn đoán!")
            break
