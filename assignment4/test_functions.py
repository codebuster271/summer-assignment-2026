from assignment4 import functions as f
from assignment4 import files as files


def run_tests():
    assert f.max_of_three(1, 5, 3) == 5
    assert f.distinct_elements([1, 2, 2, 3, 1]) == [1, 2, 3]
    assert f.multiply_list([2, 3, 4]) == 24
    assert f.factorial(5) == 120
    assert f.reverse_string('abc') == 'cba'
    assert f.is_in_range(5, 1, 10) is True
    assert f.is_in_range(0, 1, 10) is False
    # even numbers printed (not captured here)
    assert f.is_prime(13) is True
    up, low = f.count_case('Hello WORLD')
    assert up == 6 and low == 4

    # file I/O (minimal style)
    demo_path = 'test_demo.txt'
    files.write_text_file(demo_path, 'A\n')
    files.append_text_file(demo_path, 'B\n')
    contents = files.read_text_file(demo_path)
    assert contents == 'A\nB\n'

    print('All tests passed')


if __name__ == '__main__':
    run_tests()
