REMOVE_COMMAND = "remove"
ADD_COMMAND = "add"
END_COMMAND = "end"
BEGINNING_COMMAND = "beginning"


def list_manipulator(nums, *args):
    if args:
        first_param, second_param, *numbers = args
        if first_param == REMOVE_COMMAND and second_param == END_COMMAND:
            if not numbers:
                return nums[:-1]
            else:
                amount_of_numbers = 0
                for x in numbers:
                    amount_of_numbers += x
                return nums[:-amount_of_numbers]
        elif first_param == REMOVE_COMMAND and second_param == BEGINNING_COMMAND:
            if not numbers:
                return nums[1:]
            else:
                amount_of_numbers = 0
                for x in numbers:
                    amount_of_numbers += x
                return nums[amount_of_numbers:]
        elif first_param == ADD_COMMAND and second_param == END_COMMAND:
            for x in numbers:
                nums.append(x)
            return nums
        elif first_param == ADD_COMMAND and second_param == BEGINNING_COMMAND:
            for x in reversed(numbers):
                nums.insert(0, x)
            return nums
