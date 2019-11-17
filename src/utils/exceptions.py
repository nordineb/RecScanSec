class ReconTexceptions(Exception):

      def __init__(self,msg='ReconT Base Exception'):
          self._msg = msg
          
      def __str__(self):
          return self._msg

class RequestException(ReconTexceptions):

      def __init__(self,msg='Request Exceptions'):
          super().__init__(msg)          

      def __str__(self):
          return self._msg
          
        