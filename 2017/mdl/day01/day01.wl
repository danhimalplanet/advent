ClearAll[aoc1p1]
aoc1p1[s_String] := If[StringFreeQ[s, DigitCharacter],
  "0",
  With[{sc = Characters[s]},
      With[{rc = RotateLeft[sc]},
       Pick[sc, Thread[Unevaluated[SameQ[sc, rc]]]]]
      ] // Map[FromDigits] // Total // ToString
  ]

ClearAll[aoc1p2]
aoc1p2[s_String] := If[StringFreeQ[s, DigitCharacter],
  "0",
  With[{sc = Characters[s]},
      With[{rc = RotateLeft[sc, IntegerPart[Length[sc]/2]]},
       Pick[sc, Thread[Unevaluated[SameQ[sc, rc]]]]]
      ] // Map[FromDigits] // Total // ToString
  ]
