import os

print(os.listdir("F:/"))

# path = "f:/test/test2/test.txt"
# os.makedirs(path)

path = "./"

print(os.path.abspath(path))

print(os.path.basename(r"D:\video\进击的巨人\进击的巨人第二季 第01集.mp4"))
print(os.path.exists(r"D:\video\进击的巨人\进击的巨人第二季 第01.mp4"))
print(os.path.isfile(r"D:\video\进击的巨人\进击的巨人第二季 第01集.mp4"))
print(os.path.isdir(r"D:\video\进击的巨人\进击的巨人第二季 第01集.mp4"))
print(os.getcwd())
