class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        String s = a + "";
        s += b + "";
        int s_to_i = Integer.parseInt(s);
        int result = 2 * a * b;
        System.out.println(s_to_i);
        if (s_to_i >= result) {
            answer = s_to_i;
        } else {
            answer = result;
        }
        
        return answer;
    }
}