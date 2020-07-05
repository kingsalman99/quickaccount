"""
CLI
"""

from main import CreateRamdonAccount
from main import CreateManuallyAccount


class SelectOption(CreateRamdonAccount, CreateManuallyAccount):
    """
    Introduction what the user wants.
    """
    
    def __init__(self, *args, **kwargs):        
        option = input(
            'Welcome, what do you want to do?\n'
            '\n1- Create RANDOM account'
            '\n2- Create MANUAL account\n'
            '\nChoose: '
        )

        self.selected_option(option)
        
    def selected_option(self, option):
        if option != '1' and option != '2':
            self.__init__()
            
        self.provider(option)              
    
    def provider(self, option):
        message_provider = (
            '\nChoose the service provider:\n'
            '\n1- Gmail\n'
            '2- Hotmail\n'
            '3- Yahoo\n'
            '4- Proton mail\n'
            '5- Temporary mail\n'
            '\nChoose: '
        )
        
        provider = input(message_provider)
        
        while provider != '1' and provider != '2' and\
            provider != '3' and provider != '4' and\
            provider != '5':
                    
            provider = input(message_provider)
                    
            if provider == '1' or provider == '2' or\
                provider == '3' or provider == '4' or\
                provider == '5':
                
                if option == '1':            
                    self.random_provider(provider)
                
                else:
                    pass
                
        if option == '1':            
            self.random_provider(provider)
                
        else:
            pass


if __name__ == '__main__':
    SelectOption()