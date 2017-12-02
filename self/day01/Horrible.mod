MODULE Horrible;

   IMPORT Oberon, Texts, Files, SYSTEM, Args;

   (* cannot figure out how to use an ARRAY OF CHAR, have to give it a size *)
   TYPE TINPUT = ARRAY 4096 OF CHAR;

   VAR W: Texts.Writer;
      S: Texts.Scanner;
      F: Files.File;
      R: Files.Rider;
      FNAME, INPUT: TINPUT;
      INLEN: SYSTEM.INT32;

   PROCEDURE DumbCharToInt(ch: CHAR): INTEGER;
   BEGIN;
      RETURN ORD(ch) - ORD("0")
   END DumbCharToInt;

   PROCEDURE CalcSum1(thing: TINPUT; len: SYSTEM.INT32): INTEGER;
      VAR cur: CHAR;
         s, i: INTEGER;
   BEGIN;
      s := 0; i := 1;
      cur := thing[0];

      WHILE i < len-1 DO
         IF cur = thing[i] THEN s := s + DumbCharToInt(cur) END;
         cur := thing[i];
         INC(i)
      END;
      (* digit after the last one is the first one *)
      IF cur = thing[0] THEN s := s + DumbCharToInt(cur) END;

      RETURN s
   END CalcSum1;

   PROCEDURE CalcSum2(thing: TINPUT; len: SYSTEM.INT32) : INTEGER;
      VAR midchar: CHAR;
         s: INTEGER;
         i, mid: SYSTEM.INT32;
   BEGIN;
      s := 0;
      len := len - 1;
      mid := len DIV 2;

      FOR i := 0 TO len DO
         midchar := thing[(i+mid) MOD len];
         IF thing[i] = midchar THEN s := s + DumbCharToInt(midchar) END
      END;

      RETURN s
   END CalcSum2;

BEGIN
   Texts.OpenWriter(W);
   Texts.OpenScanner(S, Oberon.Par.text, Oberon.Par.pos); Texts.Scan(S);
   (* defaults *)
   INPUT := "1212";
   INLEN := 5;

   IF Args.argc = 2 THEN
      Args.Get(1, FNAME);
      F := Files.Old(FNAME);
      IF F # NIL THEN
         INLEN := Files.Length(F);
         Files.Set(R, F, 0);
         Files.ReadString(R, INPUT);
         Files.Close(F);
      END;
   END;
   Texts.WriteInt(W, CalcSum1(INPUT, INLEN), -5); Texts.WriteLn(W);
   Texts.WriteInt(W, CalcSum2(INPUT, INLEN), -5); Texts.WriteLn(W);
   Texts.Append(Oberon.Log, W.buf)
END Horrible.
