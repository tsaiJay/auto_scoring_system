import pandas as pd


if __name__ == "__main__":
    ROOT_PATH = './'
    SCORE_EXCEL = './student_list.xlsx'
    FILE_LIST = ['mid_exam_eval1/eval_score_exam_1.txt',
                 'mid_exam_eval2/eval_score_exam_2.txt',
                 'mid_exam_eval3/eval_score_exam_3.txt']
    TITLE = 'mid'
    WEIGHT = [0.3, 0.3, 0.4]

    df = pd.read_excel(SCORE_EXCEL)

    # === 登記成績 ===
    num_question = len(FILE_LIST)
    for idx in range(num_question):
        with open(FILE_LIST[idx], 'r') as score_file:
            lines = score_file.readlines()
            for line in lines:
                # === get ID and Score from each line ==
                ID = '_'.join(line.split('.py')[0].split('\\')[1].split('_')[:-1]).upper()
                score = float(line[32:40].strip())

                # === find student in excel dataframe and update the score ==
                student = df[df['學(帳)號'] == ID]
                if not student.empty:
                    df.loc[df['學(帳)號'] == ID, '{}{}'.format(TITLE, idx + 1)] = score  # df.loc[row, cols]
                    df.loc[df['學(帳)號'] == ID, '{}{}_w'.format(TITLE, idx + 1)] = score * WEIGHT[idx]
                else:
                    print("cannot find student")

    # === 計算加權平均 ===
    question_list = ['{}{}_w'.format(TITLE, i + 1) for i in range(num_question)]
    df['Raw_Score'] = df[question_list].sum(axis=1)
    df = df.drop(question_list, axis=1)

    df.to_excel('Raw_Score.xlsx', index=False)
