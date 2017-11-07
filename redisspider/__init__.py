# # -*- coding: utf-8 -*-
import re, sys


def format_channel(str):
    return "        %s {}\n" % str.strip()


if __name__ == "__main__":
    gradle_path = 'build.gradle'

    channel_str = ['web', 'xiaomi', 'guangdiantong2']
    file = open(gradle_path, mode='r')
    file1 = open("./build.gradle_bak", mode='w')
    iswrite = False
    flag  = False
    flag2 = False
    pre = 0
    for line in file.readlines():
        if 'productFlavors' in line and not flag and 'productFlavors.' not in line:
            file1.write(line)
            flag = True
        if flag:
            if '{' in line:
                pre += 1
            if '}' in line:
                pre -= 1
            if not flag2 and flag:
                for channel in channel_str:
                    if channel in line:
                        flag2 = True
                        break


        if pre == 0:
            file1.write(line)
            flag = False
            continue
        if not flag2 and flag:
            continue
        file1.write(line)
        if flag and flag2 and (line.strip('  \n') == '}' or '{}' in line):
            flag2 = False


    file1.flush()
    file1.close()
    file.close()