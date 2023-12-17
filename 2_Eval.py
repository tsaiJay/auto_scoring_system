import subprocess
import os
from tqdm import tqdm
import json


class DATA_FEEDER(object):
    def __init__(self, path: str):
        self.PATH = path
        self.RAW_DATA = self.json_read(self.PATH)

        self.datas = self.RAW_DATA['data']
        self.answers = self.RAW_DATA['answer']
        # self.single_data_lines = len(self.datas[0])

    def __len__(self):
        return len(self.datas)

    def json_read(self, path):
        with open(path, 'r') as f:
            data = json.load(f)
        return data


def test(scripts: list, datas: list) -> dict:
    # TIME_OUT = 2  # seconds

    ans_dict = {}
    for script in tqdm(scripts):
        tqdm.write('==>> now in {}'.format(script))
        try:
            ans_dict[script] = []
            for idx, data in enumerate(datas):
                ''' ========= exe file =========== '''
                process = subprocess.Popen(['python', script],
                                           stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                           stderr=subprocess.PIPE, text=True)

                ''' ========= single_test input management =========== '''
                for d in data:
                    command = '{}'.format(d)
                    process.stdin.write(command + "\n")
                    process.stdin.flush()

                process.stdin.close()

                ''' ========= output management =========== '''
                return_code = process.wait()

                if return_code == 0:
                    ans_dict[script].append(process.stdout.read().strip("\n"))
                else:
                    ans_dict[script].append('exe_error')

                ''' ========= closeup procedure ========= '''
                process.stdout.close()
                process.stderr.close()
                process.terminate()

        except subprocess.CalledProcessError as e:
            print(f"Error running {script}: {e}")

    return ans_dict


def calculate_score(preds: dict, gt: list) -> list:
    score_txt = []
    for k, v in ans_dict.items():
        err_idx = []
        count = 0
        for i in range(len(gt)):
            if str(gt[i]) == str(v[i]):
                count += 1
            else:
                err_idx.append(i)
        acc = count / len(gt)
        score_txt.append('{} acc:{:.2f}[{:3d}/{:3d}]  err_idx:{}'.format(k, acc, count, len(gt), err_idx))
    return score_txt


if __name__ == "__main__":

    ROOT_DIR = 'hw_test1'
    INPUT_JSON = 'eval_data_1.json'
    OUTPUT_FILE = 'eval_result_' + ROOT_DIR + '.json'
    SCORE_FILE = 'eval_score_' + ROOT_DIR + '.txt'

    feeder = DATA_FEEDER(INPUT_JSON)
    scripts = [os.path.join(ROOT_DIR, s) for s in os.listdir(ROOT_DIR)]

    # ========= submition testing  =========
    ans_dict = test(scripts, feeder.datas)

    # ========= score calculating =========
    score_txt = calculate_score(ans_dict, feeder.answers)

    # ========= save file =========
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(ans_dict, f, indent=2)

    with open(SCORE_FILE, 'w') as f:
        for s in score_txt:
            f.write(s + '\n')

'''
    note:
        timeout detector
'''
