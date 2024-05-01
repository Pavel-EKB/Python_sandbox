def is_config_valid(validator, data_struct):
  return validator(data_struct)

#tmp_conf = {"test1": 123}
tmp_conf = ("test1", 123)

is_tmp_valid = lambda x: True if "test1" in x else False

print (is_config_valid(is_tmp_valid, tmp_conf))

# Замыкание
def linear_builder(k, b):
  def helper(x):
    return k * x + b
  return helper

linf = linear_builder(3, 9)
print (linf(5))

# Каррирование
def curr_faddr(x):
  def tmp_a(y):
    def tmp_b(z):
      return x+y+z
    return tmp_b
  return tmp_a

print(curr_faddr(1)(2)(3))

#На базе нее можно строить частично примененные функции:
p_c_faddr = curr_faddr(1)(2)
print (p_c_faddr(3))