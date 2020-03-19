from typing import List, Union, Tuple, Dict

class ListOfChoicesGenerator:


    def choices_list_generator(self, number_of_elements: int) -> List[Tuple[str, Union[str, int]]]:

      '''
      Iterate over dict and return it as a 1lvl nested list

      '''
      CHOICES_LIST = []

      for item in self.choices_dict_generator(number_of_elements).items():
        _, value = item
        CHOICES_LIST.append((value, value))
      return CHOICES_LIST

    def choices_dict_generator(self, number_of_elements: int) -> Dict:

      '''
      Generate dict with given number_of_elements and return it
      '''
      if isinstance(number_of_elements, int):
        return {f'{i}':i for i in range(1, number_of_elements + 1)}
      elif isinstance(number_of_elements, list):
        return {f'{i}':i for i in number_of_elements}


choice_generator = ListOfChoicesGenerator()

