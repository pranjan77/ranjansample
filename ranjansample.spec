/*
A KBase module: ranjansample
*/

module ranjansample {
	/*
	Insert your typespec information here.
	*/

    /* My inputs */
    typedef string myname;
    typedef string wrkspace;


    /* My outputs */
    typedef structure {
        string test;
    } outputmessage;

    /* My implementation template for the sample */
    funcdef myfunc1(wrkspace, myname)  returns (outputmessage) authentication required;
};
