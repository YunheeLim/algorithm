import java.util.*;

class Solution
{
    public int solution(int []A, int []B)
    {
        int answer = 0;
        Arrays.sort(A);
        Arrays.sort(B);
        for (int i = 0; i < B.length / 2; i++) {
            int tmp = B[i];
            B[i] = B[B.length - 1 - i];
            B[B.length - 1 - i] = tmp;
        }
        
        for (int i = 0; i < A.length; i++) {
            answer += A[i] * B[i];
        }

        return answer;
    }
}