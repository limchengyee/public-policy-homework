# Python and Turtles

You can join this assignment, [here](https://classroom.github.com/assignment-invitations/39f415bb7b155b439c113add0f03f21c).  It is due October 12 at 1:30am.

### Excitement and Exercises!
There is a 'skeleton' for each of these, in the assignment that you've checked out.  The first five answers are also there, so that you can check your work.  It's just up to you to calculate those answers.  Fill your code into the existing files, as indicated.

1. Find the 9th positive integer that is a multiple of 4, 13, 14, 26, and 50.
2. Fibonacci numbers are defined by adding the previous two terms.  Starting with 1 and 1, that gives 1, 1, 2, 3, 5, 8, etc.  Find the sum of all Fibonnacci numbers divisible by 17 and below 1 billion.  (`while` and `if`, and `%`)
3. The number 175832868806 has no prime factors above 300.  Count the unique prime factors.  (Hint: first make a list of all the primes up to 300.  How would you express a prime in python?)
4. There is a 1000-digit number, below.  If you multiply five consecutive digits, the largest value you can find is _9 × 5 × 9 × 9 × 9 = 32805_.  Multiplying 12 consecutive digits, what is the largest product you can find?
5. Pythagorean triples have the property _a² + b² = c²_.  For instance the familiar 3, 4, 5 triangle has _3² + 4² = 9 + 16 = 25 = 5²_.  There is one pythagorean triple for which _a + b + c = 1000_.  Find the product _a × b × c_.
6. In the _2×2_ gride shown below, the shortest path between two opposite corners is four units long.  There are six options for such a path (see below).  For a _100×100_ grid, the shortest path is 200 units long.  How many such paths are there? </br>
   Hints: What is necessary for a path to be a "shortest path"?
7. A Collatz sequence is defined by:
   1. n → n/2 (for even n)
   2. n → 3n + 1 (for odd n)
 
   Using this rule, for 13, we get: 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1.
   It is believed that the sequence ends at 1, for all numbers.  What is the longest Collatz sequence that _starts_ below 2 million?</br>
   Bonus: Use precomputation and recursive functional calls.
8. Make a Spirograph with turtles.  In a spirograph, a disks rolls of radius _r_ around the inside of a larger ring of radius _R_ without slipping.  The center of that disk thus describes yet another circle, of radius _R - r_.  By sticking a marker through a hole in the disk, one can draw pretty patterns.  (Look for a youtube video if this doesn't make sense, or isn't familiar.)  The critical point is this: if _ω_ is the rate at which the disk proceeds around the center of the ring, then the disk _itself_ rotates at a rate _-ω(R-r)/r_ times the rate.  Create a function that uses turtles to emulate a spirograph; then call that function several times to make something pretty.  
   1. Visit the [turtles documentation](https://docs.python.org/3.5/library/turtle.html) for the possible commands.  
   2. Start by drawing a circle with turtle _A_.
   3. Next, ask turtle _B_ to proceed in a smaller circle around turtle _A_.  Start by retrieving _A_'s position.  Then calculate the appropriate location for _B_ to head to, using the _-(R-r)/r_ ratio, and go to that location.  As a reminder, if the distance from the center is _d_, the circles will be _x<sub>B</sub> = x<sub>A</sub> + d × cos(-θ * (R - r)/r)_, and the _y_ coordinate will be similar except with a sine.
   4. Call your complete spirograph several times, to make pretty spirographs!  There is a line at the end of your skeleton, for saving the images.
   5. As (optional) extensions, you could:
     1. Figure out how many loops around the big ring the disk has to make, before it starts repeating itself.
     2. Make a shading function, so that the colors shift either over time or as a function of the location or direction of the turtle.
     3. Do the math to figure out where the _(R-r)/r_ factor comes from.

Just make sure it's in before Wednesday October 12th at 1:30am!


![Paths](paths.png?raw=true "Paths")
![Spirograph Diagram](spiro_diag.png?raw=true "Spirograph Diagram")
![Spirograph](jamie_spirograph.png?raw=true "Spirograph")



Here is the 1000-digit number, for exercise 4.
> `1334689116556462941882035808943573171674164401363769460864490234588978262666944913475783756741523897`
> `2451842078794008017729485191070221721127038509952508280176431149895323416382564339029748626819508699`
> `0955072496443867036500559413877056832798700698818111509823878655934307473221647215004911386585940003`
> `6834001396323915862736324118712200726467082136557785333250304970064033489578066450615899117582800671`
> `4920068918928063049564469657907330954702349255539722752209584079902759262004445958585816812757463180`
> `8959993123839057795949253567061245191709785620427993669881880847373417906939397055918030430330169483`
> `5535657388574351479006304909345090039619401560275818621377887855535660203417104398980782823962234208`
> `2472624521308758843193838529317281058585486047922915733289925592867620144082168498632352326188791465`
> `7015627819301645817526587333877541158580040204764914823925333504663643182191948572526248328737405212`
> `1386952248950622806575169311906365131300057110279941542555942008569206742619537842879039448112019071`
