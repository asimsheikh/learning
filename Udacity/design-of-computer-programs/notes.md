# Lesson 1

## Outlining the problem 

The goal is to build a poker playing program.

We need to have an idea about the problem domain, the main concepts. In the case
of a poker playing game, the major concepts are 

- cards (which have numbers symbols on them)
- hand (a collection of cards)
- suit (the symbol on the card eg hearts, diamonds, clubs, spacdes)
- rank (where the card sits in the heirarchy of value, eg A > K > Q ....)
- hand rank (how do you value the whole hand)	
	- n-kind (how many of the same rank eg 2 aces or 3 10's)
	- straight (the hand are all sequential eg 8,9,10,J,Q) 
	- flush (all the same suit)

These concepts need to be modelled and represented in the computer.

## Representing hands 

We need a method to represent the hands, examples could include 

```python
[ 'JS', 'JD', '2S', '2C', '7H']
[ (11, 'S'), (11, 'D'), (2, 'S') ]
"JS JD 2S 2C 2D"
```

## Poker function

We need to build out a function that matches the signature 

```python
 def poker(hands) -> hand:
	"Return the best hand: poker([hand1, hand2 ... handn]) -> hand"
	return ??
```

We have a python builtin that selects the highest number from a list, the **max**
function.

```python 
assert max([1,2,-10]) == 2
assert max([1,2,-10], key=abs) == -10
```

## Testing 

Testing is the process of building test cases that allow us to understand if our
software is meeting expectations.

```python
def test_poker():
    straight_flush = "6C 7C 8C 9C TC".split()
    four_of_kind = "9D 9H 9S 9C 7D".split()
    full_house = "TD TC TH 7C 7D".split()
    
    assert poker(straight_flush, four_of_kind, full_house) == straight_flush
```


