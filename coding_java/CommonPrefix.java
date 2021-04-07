public class CommonPrefix {

    public static void main(String args[]) {
        StringBuilder prefix = new StringBuilder("");

        for(int i = 0; i < args[0].length()-1; i++) {
            for(int j = 0; j < args.length-1; j++) {

                System.out.println(i);

                if(args[0].charAt(i) == (args[j].charAt(i))) {
                    prefix.append(args[0].charAt(i));
                }
            }
    }

    System.out.println("The common prefix is: " + prefix);

}

}