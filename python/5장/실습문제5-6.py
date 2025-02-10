file_names = ["file1.py", "file2.txt", "file3.pptx", "file4.doc"]
list1 = []
for i in range(len(file_names)):
    list1 = file_names[i].split(".")
    print(file_names[i], "=> 파일명:", list1[0], ", 확장자", list1[1])
