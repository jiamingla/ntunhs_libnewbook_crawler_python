# ntunhs_libnewbook_crawler_python  
 用python爬北護基本的新書通告，目前還在很基礎的階段  
## 使用了什麼套件  
#### 
* re  
* Beautifulsoup  
* Selenium  
* request  
---  
## 各個檔案的用途  

### lib_crawl_month_now_2021.py 

 可以查當下的新書通告，包含了中文書、西文書和視聽   
 有遇到很多當月份西文書或視聽沒有資料的情況，有針對例外狀況提出應對  
 用json檔記錄下來，看看之後可不可以上firebase  

### lib_login.py
 
 可以用自己的帳號密碼登入，另外系統預設所有人的密碼是CHANGEME  
 看過網友在CSDN上PO文就是用類似方式去取得學生的借閱情形去做資料分析  

---  
### 還沒寫好的  
#### 之前應該是有寫一個給書的永久連結去把書的資訊爬出來的程式，我再找找看  
