import hashlib
# 待加密信息
str = 'blog123'
# 创建md5对象
m = hashlib.md5()
# Tips
# 此处必须encode
# 若写法为m.update(str)  报错为： Unicode-objects must be encoded before hashing
# 因为python3里默认的str是unicode
# 或者 b = bytes(str, encoding='utf-8')，作用相同，都是encode为bytes
b = str.encode(encoding='utf-8')
m.update(b)
str_md5 = m.hexdigest()
print('MD5加密前为 ：' + str)
print('MD5加密后为 ：' + str_md5)
