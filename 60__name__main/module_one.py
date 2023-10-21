# if __name__ == "__main__"

# 1. Module can be run as a standalone program
# 2. Module can be imported and used by other modules

# Python interpreter sets "special variables", one of which is __name__
# then Python will execute the code found within __main__

# Python will assign the __name__ variable a value of "__main__" if it's
# the original module being run

# import module_two
# # print("module_one: module_one.__name__", __name__)
# # print("module_one: module_two.__name__", module_two.__name__)

# if __name__ == "__main__":
#   print("running this module directly")
# else:
#   print("running other module indirectly")

def main():
  pass

def hello():
  print("Hello!")


if __name__ == "__main__":
  main()
  hello()