Object subclass: #Day01
	instanceVariableNames: ''
	classVariableNames: ''
	poolDictionaries: ''
	category: 'Self-Advent'!
!Day01 commentStamp: 'fn 12/1/2018 23:51' prior: 0!
2018-12-01

Do:

Day01 part1.
Day01 part2.

part2 is very slow.
!


!Day01 methodsFor: 'as yet unclassified' stamp: 'fn 12/1/2018 23:19'!
part1: numbersArray
	| numbers freq |
	(numbersArray = nil) ifTrue: [numbers := self readInput.] ifFalse: [numbers := numbersArray copy.].
	freq := 0.
	numbers
		do: [:each | freq := freq + each].
	^ freq! !

!Day01 methodsFor: 'as yet unclassified' stamp: 'fn 12/1/2018 23:38'!
part2: numbersArray
	| stream freq seen |
	(numbersArray isNil) ifTrue: [stream := self readInput readStream.] ifFalse: [stream := numbersArray readStream.].
	freq := 0.
	seen := Set new.
	[seen includes: freq]
		whileFalse: [| i |
			i := stream next.
			i = nil
				ifTrue: [stream reset.]
				ifFalse: [seen add: freq. freq := freq + i.].
		].
	^ freq! !

!Day01 methodsFor: 'as yet unclassified' stamp: 'fn 12/1/2018 23:27'!
readInput
	| ls numbers |
	numbers := OrderedCollection new.
	ls := (FileStream fileNamed: '/tmp/input.txt') contentsOfEntireFile splitBy: String lf.
	ls
		do: [:each | each ~= ''
				ifTrue: [numbers add: each asInteger]].
	^ numbers! !

"-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- "!

Day01 class
	instanceVariableNames: ''!

!Day01 class methodsFor: 'as yet unclassified' stamp: 'fn 12/1/2018 23:22'!
part1

^Day01 new part1: nil.! !

!Day01 class methodsFor: 'as yet unclassified' stamp: 'fn 12/1/2018 23:22'!
part2

^Day01 new part2: nil.! !


TestCase subclass: #Day01Test
	instanceVariableNames: ''
	classVariableNames: ''
	poolDictionaries: ''
	category: 'Self-Advent'!
!Day01Test commentStamp: 'fn 12/1/2018 23:56' prior: 0!
Use the TestRunner.!
]style[(19)FBitmap DejaVu Sans#14!


!Day01Test methodsFor: 'as yet unclassified' stamp: 'fn 12/1/2018 23:27'!
testPart01
	| day01 |
	day01 := Day01 new.
	self
		assert: (day01 part1: #(1 -2 3 1))
		equals: 3.
	self
		assert: (day01 part1: #(1 1 1))
		equals: 3.
	self
		assert: (day01 part1: #(1 1 -2))
		equals: 0.
	self
		assert: (day01 part1: #(-1 -2 -3))
		equals: -6! !

!Day01Test methodsFor: 'as yet unclassified' stamp: 'fn 12/1/2018 23:26'!
testPart02
	| day01 |
	day01 := Day01 new.
	self
		assert: (day01 part2: #(1 -2 3 1))
		equals: 2.
	self
		assert: (day01 part2: #(1 -1))
		equals: 0.
	self
		assert: (day01 part2: #(3 3 4 -2 -4))
		equals: 10.
	self
		assert: (day01 part2: #(-6 3 8 5 -6))
		equals: 5.
	self
		assert: (day01 part2: #(7 7 -2 -7 -4))
		equals: 14! !
