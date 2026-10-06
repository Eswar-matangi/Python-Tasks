college = "SRGEC"  # Global variable
def classroom():
    branch = "CSE"  # Enclosing variable
    def student():
        name = "Eswar"  # Local variable
        print(name)     # Local
        print(branch)  # Enclosing
        print(college)   # Global
        def marks():
            score = 92  # Local to marks()
            print(score)
            print(branch)  # Enclosing
            print(college)   # Global

        marks()
    student()
classroom()