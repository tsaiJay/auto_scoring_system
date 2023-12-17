import os
import shutil


def make_classified_dir(tails: list, ext: str) -> list:
    dir_list = []
    for t in tails:
        dir_name = 'question{}'.format(t)
        os.makedirs(dir_name, exist_ok=True)
        dir_list.append(dir_name)
    print('--> make folder:', dir_list)
    return dir_list


def check_ext(ext: str, paths: list) -> list:
    error_list = []
    for file in paths:
        if file.split('.')[-1] != ext[1:]:
            error_list.append(file)
    return error_list


def check_tail(tail: list, ext: str, paths: list) -> list:
    err_list = []
    allow_end = [t + ext for t in tail]
    for f in paths:
        if f[-len(tail[0] + ext):] not in allow_end:
            err_list.append(f)
    return err_list


def classify_files(tails: list, paths: list, targets) -> list:
    for file in paths:
        ck_f = '_' + file.split('_')[-1].split('.')[0]
        for t in targets:
            if ck_f in t:
                shutil.copy(file, t)
                break
    print('classiy done!')


if __name__ == "__main__":
    ROOT_DIR = './all_submissions'
    EXT_TYPE = '.py'
    TAIL_RULE = ['_1', '_2']

    target_dirs = make_classified_dir(TAIL_RULE, EXT_TYPE)

    # === list all file in subdir ===
    sub_path = [os.path.join(ROOT_DIR, d) for d in os.listdir(ROOT_DIR)]
    all_file_path = []
    for dir_path in sub_path:
        files = os.listdir(dir_path)
        all_file_path += [os.path.join(dir_path, f) for f in files]

    # === check files extension. ex. .py, .cpp ... ===
    error_ext = check_ext(ext=EXT_TYPE, paths=all_file_path)
    print('extension check : [{}]'.format(EXT_TYPE))
    print('--> ext err/total: {}/{}'.format(len(error_ext), len(all_file_path)))
    print('--> error file:', error_ext)

    # === check files tail. ex. _1, _2 ... ===
    error_tail = check_tail(tail=TAIL_RULE, ext=EXT_TYPE, paths=all_file_path)
    print('tail check : {}'.format(TAIL_RULE))
    print('--> ext err/total: {}/{}'.format(len(error_tail), len(all_file_path)))
    print('--> error file:', error_tail)

    # === classify files to corresponding folder ===
    classify_files(TAIL_RULE, all_file_path, target_dirs)
