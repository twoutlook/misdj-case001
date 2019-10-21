
# 練習在 github 協作

## 在工作目錄 clone 本項目
在你的工作區，新建一個檔案夾 misdj-case001，以後我們稱之為本項目的工作目錄


```
git clone https://github.com/twoutlook/misdj-case001.git
```

## 建立該項目的虛擬環境
虛擬環境是指 Python3.6 以上的。


```
python3 -m venv venv
```
## 啟用上述虛擬環境並安裝所需
虛擬環境是指 Python3.6 以上的。


```
source venv/bin/activate
pip install -r misdj-case001/requirements.txt
```

### 檢查虛擬環境安裝是否正確

使用指令  pip freeze 查看，是否如同以下結果
```
(venv) $ pip freeze
defusedxml==0.6.0
diff-match-patch==20181111
Django==2.2.6
django-import-export==1.2.0
et-xmlfile==1.0.1
jdcal==1.4.1
MarkupPy==1.14
odfpy==1.4.0
openpyxl==3.0.0
pytz==2019.3
PyYAML==5.1.2
sqlparse==0.3.0
tablib==0.14.0
xlrd==1.2.0
xlwt==1.3.0
```

## 以 Mac 使用者 為例
到這裡要達到的效果是這樣子的

```
$ pwd
/Users/pinglingchen/django-team
$ tree -L 2 misdj-case001/
misdj-case001/
├── misdj-case001
│   ├── README.md
│   ├── case001
│   ├── case001-data
│   ├── db.sqlite3
│   ├── go
│   ├── img
│   ├── manage.py
│   ├── misdj
│   ├── misdj-ww-steps-master
│   ├── note
│   ├── others
│   ├── requirements.txt
│   └── sharing
└── venv
    ├── bin
    ├── include
    ├── lib
    ├── pip-selfcheck.json
    └── pyvenv.cfg

13 directories, 7 files
```
