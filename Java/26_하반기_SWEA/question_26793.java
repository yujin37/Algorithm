import java.util.Arrays;
import java.util.Scanner;

public class question_26793 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int test_case=1; test_case <= T; test_case++) {
			int n = sc.nextInt();
			int[][] tasks = new int[n][2];
			
			for(int i=0; i<n; i++) {
				
				tasks[i][0] = sc.nextInt();
				tasks[i][1] = sc.nextInt();
			}
			Arrays.sort(tasks, (a,b) -> Integer.compare(a[1], b[1]));
			
			int time=0;

			long video = Integer.MAX_VALUE;
			for(int i=0; i<tasks.length; i++) {
				long maxVideo = (long) tasks[i][1] - time - tasks[i][0];

			    video = Math.min(video, maxVideo);
				time += tasks[i][0];

			}
			System.out.println(video);
			

		}
				
	}

}
