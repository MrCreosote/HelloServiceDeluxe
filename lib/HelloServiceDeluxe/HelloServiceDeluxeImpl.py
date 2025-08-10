# -*- coding: utf-8 -*-
#BEGIN_HEADER
#END_HEADER


class HelloServiceDeluxe:
    '''
    Module Name:
    HelloServiceDeluxe

    Module Description:
    
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.1.1"
    GIT_URL = "https://github.com/mrcreosote/HelloServiceDeluxe.git"
    GIT_COMMIT_HASH = "10ca14e770178fa3586ed6d710e0f2456ba14da1"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        #END_CONSTRUCTOR
        pass


    def say_hello(self, ctx, name):
        """
        :param name: instance of String
        :returns: instance of String
        """
        # ctx is the context object
        # return variables are: message
        #BEGIN say_hello
        message = "Hello, "+name+". I am a service."
        print('returning: ' + message)
        #END say_hello

        # At some point might do deeper type checking...
        if not isinstance(message, str):
            raise ValueError('Method say_hello return value ' +
                             'message is not type str as required.')
        # return the results
        return [message]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
