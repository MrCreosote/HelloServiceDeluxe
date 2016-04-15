#BEGIN_HEADER
#END_HEADER


class HelloService:
    '''
    Module Name:
    HelloService

    Module Description:
    A KBase module: HelloService
    '''

    ######## WARNING FOR GEVENT USERS #######
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    #########################################
    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        #END_CONSTRUCTOR
        pass

    def say_hello(self, ctx, name):
        # ctx is the context object
        # return variables are: message
        #BEGIN say_hello
        message = "Hello, "+name+".  I am a service."
        #END say_hello

        # At some point might do deeper type checking...
        if not isinstance(message, basestring):
            raise ValueError('Method say_hello return value ' +
                             'message is not type basestring as required.')
        # return the results
        return [message]
