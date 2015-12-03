#BEGIN_HEADER
#END_HEADER


class ranjansample:
    '''
    Module Name:
    ranjansample

    Module Description:
    A KBase module: ranjansample
    '''

    ######## WARNING FOR GEVENT USERS #######
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    #########################################
    #BEGIN_CLASS_HEADER
    workspaceURL = None
    myprops = None
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.workspaceURL = config['workspace-url']
        self.myprops = config['myprops']
        #END_CONSTRUCTOR
        pass

    def myfunc1(self, ctx, wrkspace, myname):
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN myfunc1


        returnVal = wrkspace + "___" + myname + "___" + self.myprops

        #END myfunc1

        # At some point might do deeper type checking...
        if not isinstance(returnVal, basestring):
            raise ValueError('Method myfunc1 return value ' +
                             'returnVal is not type basestring as required.')
        # return the results
        return [returnVal]
