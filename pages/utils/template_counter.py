from django.conf import settings
import os

from typing import List
class TemplatesCounter:

    '''
    Counting created templates in project which can be selected in models
    '''

    def get_count(self) -> int:

        '''
        Count number of available templates
        '''

        return len(self.get_templates_list())

    def get_templates_list(self) -> List[str]:

        '''
        Check if any template exist
        '''
        folder_path = f'{settings.BASE_DIR}/templates/homepage_templates/'
        folder_list = [name for name in os.listdir(folder_path)]
        return folder_list

template_counter = TemplatesCounter()