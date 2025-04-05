class Solution {
    public String solution(String s) {
        String answer = "";
        String[] splitted = s.split(" ");
        int max_val = Integer.parseInt(splitted[0]);
        int min_val = Integer.parseInt(splitted[0]);
        for (int i = 0; i < splitted.length; i++) {
            int num = Integer.parseInt(splitted[i]);
            if (num > max_val) {
                max_val = num;
            } else if (num < min_val){
                min_val = num;
            }
        }
        answer += min_val + "";
        answer += " ";
        answer += max_val + "";
        
        return answer;
    }
}