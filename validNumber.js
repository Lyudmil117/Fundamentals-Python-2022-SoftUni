function number(input) {
    let num = Number(input[0]);

    if (num < 100 || num > 200){
        if (num != 0){
            console.log("invalid")
        }
    }
}

number([75])
