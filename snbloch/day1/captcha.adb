with Ada.Text_IO;  use Ada.Text_IO;
with Ada.Strings.Unbounded;  use Ada.Strings.Unbounded;
with Ada.Integer_Text_IO; use Ada.Integer_Text_IO;
 
procedure captcha is
   File : File_Type;
   input : Unbounded_String;
   sum : Integer := 0;
   strlen : Integer;
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
   for Num in 1 .. (strlen - 1) loop 
      if element (input, Num) = element (input, Num + 1) then
          sum := sum + Integer'Value ((1 => element (input, Num)));
      end if;
   end loop;
   if element (input, 1) = element (input, strlen) then
      sum := sum + Integer'Value ((1 => element (input, strlen)));
   end if;

   Put (sum);

end captcha;
