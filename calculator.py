run = 1;

while run == 1:
    a = input("Enter a number or a letter to exit: ");
    try: 
        int(a);
        op = input("Enter an operation: ");
        b = input("Enter another number: ");

        if(b.isdigit):
            a = int(a);
            b = int(b);
            result = "";

            #if everything's good, 'ok' should be 1
            ok = 1;

            if(op == "+"):
                result = a + b;
            elif(op == "-"):
                result = a - b;
            elif(op == "*"):
                result = a * b;
            elif(op == "/"):
                result = a / b;
            else:
                print("No operation '" + str(op) + "'");
                ok = 0;
            
            if ok == 1:
                print(">>>>> " + str(result));

    except ValueError:
        run = 0;
