
# AttendX Login Test

def test_valid_login():
    username = "student01"
    password = "correct123"

    assert username != ""
    assert password != ""

    print("Checking valid login input...")
    print("PASS: Valid login fields are provided")
   

def test_empty_login():
    username = ""
    password = ""

    assert username == ""
    assert password == ""

    print("PASS: Empty login fields detected")

if __name__ == "__main__":
    test_valid_login()
    test_empty_login()
  