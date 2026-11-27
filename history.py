def show_histories(histories):
    if not histories:
        print("\nHistory is empty!\n")
        return

    print("\n----- History -----\n")

    for i, history in enumerate(histories, start=1):
        print(
            f"{i}. {history['num1']} "
            f"{history['operation']} "
            f"{history['num2']} = {history['result']}"
        )

    print("\n----- End -----\n")
