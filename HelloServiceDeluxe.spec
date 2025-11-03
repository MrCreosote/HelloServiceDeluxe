module HelloServiceDeluxe {

    funcdef say_hello(string name) returns (string message);
    /* for testing multiple returns */
    funcdef say_hellos(string name1, string name2)
        returns (string msg1, string msg2);
    funcdef how_rude(string name) returns ();
};
