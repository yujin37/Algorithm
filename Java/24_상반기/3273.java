import java.util.*;
import java.io.*;

public class Baekjoon_3273 {
    public static void main(String[] args)  throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int a[] = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());
        HashSet<Integer> set = new HashSet<>();
        for(int i = 0; i<n ; i++){
            a[i] = Integer.parseInt(st.nextToken());
            set.add(a[i]);
        }

        int x = Integer.parseInt(br.readLine());
        

        int cnt = 0;
        for(int i = 0; i<n; i++) {
            if(set.contains(x-a[i])) {
                cnt++;
            }
        }

        System.out.println(cnt/2);


    }
}
