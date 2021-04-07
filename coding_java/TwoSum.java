public class TwoSum {

    public static void main(String args[]){
        int[] nums = {Integer.parseInt(args[0]), Integer.parseInt(args[1]), Integer.parseInt(args[2]), Integer.parseInt(args[3])};
        int target = Integer.parseInt(args[4]);

        for(int i = 0; i < nums.length; i++) {
            for(int j = 0; j < nums.length; j++) {
                if((nums[j] + nums[i]) == target) {
                    if(j==i){
                    }
                    else{
                        System.out.println("Number " + i + " (" + nums[i] + ") + Number " + j + "(" + nums[j] + ") = The Target (" + target + ")");
                        return;
                    }
                }
            }
        }
    }
}