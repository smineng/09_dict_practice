# 辞書を定義
fruits_dict = {"りんご": "Apple",
          "ぶどう": "Grape",
          "みかん": "Orange"}

#print(fruits["ぶどう"])
#print(fruits["みかん"])
#print(fruits["りんご"])


#Keyだけforループ
for jp_name in fruits_dict.keys():
    print(jp_name)

#Valueだけforループ
for en_name in fruits_dict.values():
    print(en_name)

#KeyとValueを同時にforループ
for jp_name, en_name in fruits_dict.items():
    print(f"{jp_name}は英語で{en_name}")
