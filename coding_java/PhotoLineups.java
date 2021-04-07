import java.util.Scanner;
import java.util.ArrayList;
import java.util.*;

public class PhotoLineups {

   // TODO: Write method to create and output all permutations of the list of names.
   public static void allPermutations(ArrayList<String> permList, ArrayList<String> nameList) {
      if (nameList.size()==0){
         for(int i = 0; i < permList.size(); i++){
            System.out.print(permList.get(i) + " ");
         }
         System.out.println();
         permList.clear();
         return;
      }

      for(int i = 0; i < nameList.size(); i++) {
 
         String str = nameList.get(i);
         ArrayList<String> rol = new ArrayList<>();
         rol.addAll(nameList.subList(0,i));
         rol.addAll(nameList.subList(i+1, nameList.size()));

         ArrayList<String> listClone = new ArrayList<>();
         listClone.addAll(permList);
         listClone.add(str);
         allPermutations(listClone, rol);
         
      }

   }

   public static void main(String[] args) {
      Scanner scnr = new Scanner(System.in);
      ArrayList<String> nameList = new ArrayList<String>();
      ArrayList<String> permList = new ArrayList<String>();
      
      while(scnr.hasNext()){
         String temp = scnr.next();
         if(temp.contains("-1")){
            break;
         }
         else
            nameList.add(temp);
      }
      
      
      allPermutations(permList, nameList);
      // TODO: Read in a list of names; stop when -1 is read. Then call recursive method.
   }
}
