#!/usr/bin/env python3
from collections import defaultdict
import re

def count_duplicates(string):
    char_counts = defaultdict(int)

    # Count the occurrences of each character
    for char in string:
        char_counts[char] += 1

    duplicates = []  # List for characters with duplicates
    uniques = []  # List for characters without duplicates

    # Separate characters into duplicates and uniques
    for char, count in char_counts.items():
        if count > 1:
            duplicates.append((char, count))
        else:
            uniques.append(char)

    # Sort the duplicates list by the number of duplicates in descending order
    duplicates.sort(key=lambda x: x[1], reverse=True)

    return duplicates, uniques

def keep_chinese_characters(string):
    chinese_chars = re.findall(r'[\u4e00-\u9fff]+', string)
    cleaned_string = ''.join(chinese_chars)
    return cleaned_string


# Example usage
my_string = """
这个错误提示表明在调用DeleteThingGroup操作时请求中包含的安全令牌无效。

通常情况下这个错误是由于使用了无效或过期的安全令牌导致的。安全令牌通常用于验证和授权对AWS亚马逊网络服务资源的访问权限。

要解决这个问题你可以尝试以下步骤

检查令牌有效性确保你使用的安全令牌是有效的并且没有过期。如果你是使用AWS Identity and Access Management (IAM) 创建的访问密钥可以在AWS控制台的IAM部分进行验证和更新。

检查令牌权限确保你的安全令牌具有执行DeleteThingGroup操作所需的必要权限。你可以通过IAM角色或用户策略来管理权限。检查相关策略是否正确配置并包含DeleteThingGroup操作的权限。

检查网络连接确保你的应用程序能够与AWS服务进行通信没有任何网络连接问题。检查网络设置、防火墙或代理配置确保可以正常访问AWS服务。

如果你仍然遇到问题建议参考AWS官方文档、开发者论坛或联系AWS支持以获取更详细的帮助和指导。
"""
cleaned_string = keep_chinese_characters(my_string)


duplicates, uniques = count_duplicates(cleaned_string)

print("Characters with duplicates:")
for char, count in duplicates:
    print(f"Character: {char}, Duplicates: {count}")

print("\nCharacters without duplicates:")
for char in uniques:
    print(f"Character: {char}")
