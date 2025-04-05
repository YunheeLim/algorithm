import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        LinkedList<Integer> queue = new LinkedList<>();
        queue.offer(arr[0]);
        for (int num : arr) {
            if (queue.getLast() != num) {
                queue.offer(num);
            }
        }
        
        int idx = 0;
        int size = queue.size();
        int[] answer = new int[size];
        
//         while (!queue.isEmpty()) {
//             System.out.println(queue.peek());
            
//         }
        
        for (int i = 0; i < size; i++) {
            answer[idx] = queue.peek();
            queue.poll();
            idx++;
        }
        return answer;
    }
}