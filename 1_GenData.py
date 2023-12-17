import json
import random

random.seed(10)


def generate_function():
    '''
        generate a single test data for a script
        only for this example, please modified this function
        this example code will generate a random string as a human_name
    '''
    import string
    num_letters = random.randint(1, 10)
    name = ''.join(random.choice(string.ascii_letters) for _ in range(num_letters))
    return name


def answer_function(x) -> str:
    '''
        only for this example, please modified this function
    '''
    return 'Hello {}'.format(x)


if __name__ == "__main__":

    TEST_NUM = 10
    EVAL_DATA = 'eval_data.json'

    # =========== generate input =========
    datas = []
    for n in range(TEST_NUM):
        data = generate_function()
        datas.append(data)

    # =========== generate answer =========
    answers = []
    for n in range(TEST_NUM):
        ans = answer_function(datas[n])
        answers.append(ans)

    # =========== save test-case as json file =========
    output_dict = {}
    output_dict['data'] = datas
    output_dict['answer'] = answers

    with open(EVAL_DATA, 'w') as f:
        json.dump(output_dict, f, indent=2)
