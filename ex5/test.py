# Q1
from ex5.ex5 import sum_nums, copy_lines_with_str, write_twin_primes, calc_avg_position_per_band

q1_input_file_name = "q1_input_1.txt"
print(sum_nums(q1_input_file_name) == 139)

# Q2
# compare manually your output files with the correct output files
copy_lines_with_str("q2_input_1.txt", "q2_output_1_Rocky_res.txt", "Rocky")
copy_lines_with_str("q2_input_1.txt", "q2_output_1_ere_res.txt", "ere")
copy_lines_with_str("q2_input_2.txt", "q2_output_2_Rocky_res.txt", "Rocky")
copy_lines_with_str("q2_input_2.txt", "q2_output_2_boy_res.txt", "boy")
copy_lines_with_str("q2_input_2.txt", "q2_output_2_Nancy_res.txt", "Nancy")

# Q3
write_twin_primes(4, "q3_output_1_res.txt")
write_twin_primes(20, "q3_output_2_res.txt")
try:
    num = 0
    write_twin_primes(num, "q3_output_2_res.txt")  # this line should raise an exception
    print("Exception must be raised for this input")
except ValueError as ex:
    correct_error_message = "Illegal value num={}".format(num)
    if ex.args[0] == correct_error_message:
        print("True")
    else:
        print("Wrong message in raise exception. \nExpected:\t{}\ngot:\t\t{}".format(correct_error_message,
                                                                                     ex.args[0]))

# Q4
res_1 = calc_avg_position_per_band("q4_input_1.txt")
print(res_1['The Beatles'] == 23 and res_1['Radiohead'] == 11 and res_1['ABBA'] == 4)
try:
    input_file = "q4_input_2.txt"
    res_1 = calc_avg_position_per_band(input_file)
    print("Exception must be raised for this input")
except ValueError as ex:
    correct_error_message = "At least one of the bands does not appear in the file {}".format(input_file)
    if ex.args[0] == correct_error_message:
        print("True")
    else:
        print("Wrong message in raise exception. \nExpected:\t{}\ngot:\t\t{}".format(correct_error_message,
                                                                                     ex.args[0]))
