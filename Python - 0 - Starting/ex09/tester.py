from ft_package.utils import count_in_list
from ft_package.utils import greet


print(count_in_list(["toto", "tata", "toto"], "toto"))
# output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))
# output: 0

greet()
