with Ada.Text_IO;  use Ada.Text_IO;
with Ada.Strings.Unbounded;  use Ada.Strings.Unbounded;
with Ada.Integer_Text_IO; use Ada.Integer_Text_IO;
 
procedure captcha_part_2 is
   File : File_Type;
   input : Unbounded_String;
   sum : Integer := 0;
   strlen : Integer;
   advance : Integer;
begin
   Open (File => File,
         Mode => In_File,
         Name => "input.txt");
   loop
      exit when End_Of_File (File);
      input := To_Unbounded_String (Get_Line (File));
   end loop;
 
   Close (File);
   strlen := Integer (To_String (input)'Length);
   advance := strlen / 2;
   for Num in 1 .. strlen loop
      if Num > advance then 
         if element (input, Num) = element (input, Num - advance) then
            sum := sum + Integer'Value ((1 => element (input, Num)));
         end if;
      else
         if element (input, Num) = element (input, Num + advance) then
            sum := sum + Integer'Value ((1 => element (input, Num)));
         end if;
      end if;
   end loop;

   Put (sum);

end captcha_part_2;
