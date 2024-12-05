class Grade:
    def __init__(self):
        self.grades = 0.0
        self.attempt = 0
        self.average = 0.0
        self.point_grade = 0.0
        self.remarks = ""

    def calculate_grade(self):
        while True:
            grade = float(input("Input Grade (Enter -1 to stop): "))
            if grade == -1:
                break
            elif 0 <= grade <= 100:
                self.grades += grade
                self.attempt += 1
            else:
                continue

        if self.attempt > 0:
            self.average = self.grades / self.attempt
            self.point_grade = ((100 - self.average) + 10) / 10
            self.set_remarks()
        else:
            self.average = 0.0
            self.point_grade = 0.0
            self.remarks = "No grades entered."

        self.print_grade()

    def set_remarks(self):
        if self.point_grade <= 0.00:
            self.remarks = "No such grade"
        elif self.point_grade <= 9.00:
            self.remarks = "Dropped"
        elif self.point_grade >= 5.00:
            self.remarks = "Failed"

        if 80 <= self.average < 85:
            self.remarks = "Passed - Satisfactory"
        elif 85 <= self.average < 90:
            self.remarks = "Passed - Good"
        elif 90 <= self.average < 95:
            self.remarks = "Passed - Average"
        elif 95 <= self.average < 100:
            self.remarks = "Passed - Very Good"
        elif self.average == 100:
            self.remarks = "Passed - Excellent"
        else:
            self.remarks = "Out of range or Invalid"

    def print_grade(self):
        print("---------------------------------")
        print(f"Average             : {self.average:.2f}\n"
              f"Point Grade         : {self.point_grade:.2f}\n"
              f"Remarks             : {self.remarks}")
        print("---------------------------------")

calc_grade = Grade()
calc_grade.calculate_grade()
