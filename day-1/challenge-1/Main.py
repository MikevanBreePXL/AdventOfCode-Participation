def main():
    rotation_point = 50
    passed_zero_counter = 0

    def rotate_right(number_to_rotate, amount): 
        # Rotate right has a limit of 99, rolls back to 0
        result = number_to_rotate + int(amount)
        result = result % 100
        if result == 0:
            nonlocal passed_zero_counter
            passed_zero_counter += 1
        return result

    def rotate_left(number_to_rotate, amount):
        # Rotate left has a limit of 0, rolls back to 99
        result = number_to_rotate - int(amount)
        while result < 0:
            result += 100
        if result == 0:
            nonlocal passed_zero_counter
            passed_zero_counter += 1
        return result

    with open("input.txt", "r") as file:
        for line in file:
            line = line.strip()
            if line[0] == "L":
                rotation_point = rotate_left(rotation_point, line[1:])
            elif line[0] == "R":
                rotation_point = rotate_right(rotation_point, line[1:])
    
    print(f"Final rotation point: {rotation_point}")
    print(f"Passed zero counter: {passed_zero_counter}")

if __name__ == "__main__":
    main()