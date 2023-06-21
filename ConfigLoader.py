import os


aaa = 123

with open('UpgradeData.txt') as f:
    lines = f.readlines()

config = {}
for line in lines:
    if line.startswith('#') or line.startswith('/') or len(line.strip()) == 0:
        continue    # 跳过注释行和空行
    split_line = line.strip().split()    # 按空格分割
    config[split_line[0]] = ' '.join(split_line[1:])  # 第一个字段作为key,其余字段合并为value

print(config["419"])

print(str.split(config["419"]," "))


# "a  b c"
# os.system("pause") 