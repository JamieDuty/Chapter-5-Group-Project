# Number Guessing Game
kiya, jamie

## Number Guessing Game
number_guessing_game() will generate a random number between 1-1000 unless specified otherwise and will use 2 players and will keep track of the number of turns that each player has used. It will start with a menu that gives 3 options: Guess, Set Range, and Exit. The program will consist of 5 programs: main that will run the program, menu which will display the options and return the choice, return_name which will collect and return the names, random which will generate a random integer that is in a specified minimum and maximum, and guessing that will take turns with guesses and provides feedback on if you are above or below the number.. 

#Number Guessing Game
 Flowchart
```mermaid
graph TD;
  main-->menu;
  main-->return_name;
  main-->random;
  main-->guess;
```

#### Function Diagrams

| `main()`    |               |  kiya     |
| ------------------ | ------------- | ------------ |
|     | takes input from the user for __nothing__  |
|        | returns menu |
***
| `menu()`    |               |     jamie   |
| ------------------ | ------------- | ------------ |
| `    | takes input from the user for __menu choice__  |              |
|   | outputs choice 
***
| `return_name()`    |               |     kiya   |
| ------------------ | ------------- | ------------ |
|    | takes input from the user for __name of players__  |              |           |
|       | takes input for name _of players__ | returns names |
***
| `random()`    |               |     kiya   |
| ------------------ | ------------- | ------------ |
|     | takes input from the user for min and max number  |              |
|      | calculates a number between min and max             |   returns number  |
***
| `guess()`    |               |     jamie   |
| ------------------ | ------------- | ----------- |
| `random:integer`    | takes input from the user for a random number  |              |
| `    | calculates how close to number  | outputs outputs if you were less than, greater than, or equal         |
| `     |  | returns how close you were |
