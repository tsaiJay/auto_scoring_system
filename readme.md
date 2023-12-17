# Auto-Scoring-System

## 功能說明
針對moodle學習平台的學生作業自動批改並計算分數的程式，程式分為四個步驟:
- 分類檔案 (0_Classifier.py)
- 複製需要的檔案到資料夾中
- 生成測試資料 (1_GenData.py)
- 測試並計分 (2_Eval.py)


## 目錄結構
下載moodle 3.7資料夾的目錄結構應該為
```
       all_submissions/
        ├── studentA/
        │   ├── studentA_1.py
        │   ├── studentA_2.py
        │   └── studentA_3.py
        ├── studentB/
        │   ├── studentB_1.py
        │   ├── studentB_2.py
        │   └── studentB_3.py
```

## Step1: Classifier
此程式將自動依題號分類所有程式碼到對應資料夾(自動創建)中，過程中檢查副檔名、尾綴等資訊，分類好的檔案會在新生成的資料夾中，預設為question_1、questiton_2...。
- 請更改最上層資料夾
- 請更改附檔名 (EXY_TYPE)
- 請更改檔名尾綴，放在list中 (TAIL_RULE )
```
    ROOT_DIR = './all_submissions'
    EXT_TYPE = '.py'
    TAIL_RULE = ['_1', '_2', '_3']
```
執行程式
```
    python 0_Classifier.py
```

## Step2: Movefile
此步驟請手動將1_GenData.py、2_Eval.py、複製到對應的資料夾每個question中都需要獨立一份
```
       folder_for_question1/
        ├── question_1/
        │   ├── studentA_1.py
        │   ├── studentB_1.py
        │   └── studentC_1.py
        ├── 1_GenData.py
        └── 2_Eval.py
       folder_for_question2/
        ├── question_2/
        │   ├── studentA_2.py
        │   ├── studentB_2.py
        │   └── studentC_2.py
        ├── 1_GenData.py
        └── 2_Eval.py
```

## Step3: GenerateData
生成測試資料及對應解答
- 請更改 generate_function() 依照需求創建測資(字串格式)
- 若單次執行考題需要多行輸入請使用'\n'連結多行輸入
- 請更改 answer_function() 生成測資對應的正確解答
- 執行後生成檔案 eval_data.json，包含測試資料及對應解答

    
執行程式
```
    python 1_GenData.py
```
## Step3: Evaluation
執行所有程式碼並輸入測資，最後輸出通過比率
- 生成執行結果檔案

執行程式
```
    python 2_Eval.py
```


Score.py
    自動計算原始成績，並輸出excel檔案



### 待更新功能:
- [ ] 將第二步驟: 調整資料夾檔案自動化
- [ ] 3_Score未完成
- [ ] 新增可以快速調閱每個繳交結果的程式


未整理
```
exe_error: 程式無法正常執行
Eval_代碼說明
_ERR(error): 該小題輸出錯誤
_MAT(match error): 單一測資輸出答案數量不符，部分扣分
_CHA(character): 數值測試包含冗於文字檔
_TLE: 執行超時
```