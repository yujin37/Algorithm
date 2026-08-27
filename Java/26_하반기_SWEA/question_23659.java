package study;

import java.util.Scanner;

public class question_23659 {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		for(int test_case=1; test_case<=T; test_case++) {
			int n = sc.nextInt();
			int p = sc.nextInt();
			
			int[] soils1 = new int[n];
			int[] soils2 = new int[n];
			
			for(int i=0;i<n; i++) {
				soils1[i] = sc.nextInt();
			}
			for(int i=0;i<n; i++) {
				soils2[i] = sc.nextInt();
			}
			
			//비료 계산해보기 
			int[][] dp = new int[n][2];
			dp[0][0] = soils1[0];
			dp[0][1] = soils2[0];
			
			for(int j=1; j<n; j++) {
				
				dp[j][0] = Math.max(dp[j-1][0] + soils1[j]-p, dp[j-1][1] + soils1[j]);
			
				dp[j][1] = Math.max(dp[j-1][1] + soils2[j]-p, dp[j-1][0] + soils2[j]);
				
				
			}
			int result = Math.max(dp[n-1][0], dp[n-1][1]);
			System.out.println("#" + test_case + " " + result);
		}
	}

}
