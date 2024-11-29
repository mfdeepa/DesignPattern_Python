from Creational.Builder.builder_convert_java.student import Student, Gender, InvalidArgumentException

if __name__ == "__main__":
    try:
        # Create a Student object using the Builder
        student = (
            Student.create_builder()
            .set_name("Deepa")
            .set_age(26)
            .set_gender(Gender.Female)
            .set_psp(88.99)
            .set_university_name("Scaler University")
            .set_phone_number("1324242498")
            .build()
        )
        print(student)
    except InvalidArgumentException as e:
        print(f"Error: {e}")
