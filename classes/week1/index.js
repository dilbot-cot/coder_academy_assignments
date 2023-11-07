function rollDice (condition, diceSize = 20) {
    let result1 = Math.floor(Math.random() * diceSize) + 1;
    let result2 = Math.floor(Math.random() * diceSize) + 1;

    switch(condition) {
        case "advantage":
            console.log(`First dice roll result is ${result1}`);
            console.log(`Second dice roll result is ${result2}`);
            console.log(`Your roll with ${condition} is ${Math.max(result1, result2)}`);
            break;
        case "disadvantage": // Fixed spelling
            console.log(`First dice roll result is ${result1}`);
            console.log(`Second dice roll result is ${result2}`);
            console.log(`Your roll with ${condition} is ${Math.min(result1, result2)}`);
            break;
        default:
            console.log(`You got a ${result1}`);
    }
}

rollDice("advantage");
rollDice("disadvantage");
rollDice("")

// expect(rollResults.finalResult).toBeGreaterThanOrEqual(Math.min(...rollResults.rolls));