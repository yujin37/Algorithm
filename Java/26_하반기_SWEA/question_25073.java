package study;

import java.util.Scanner;

public class question_25073 {
	public static void main(String args[]) throws Exception
	{
		
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();
		/*
		   여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
		*/

		for(int test_case = 1; test_case <= T; test_case++)
		{
		
			/////////////////////////////////////////////////////////////////////////////////////////////
			
			int n = sc.nextInt();
			int m = sc.nextInt();
			int k = sc.nextInt();
			
			long[][] dp = new long[m+1][k];
			for(int i=0;i<=m; i++) {
				for(int j=0; j<k; j++) {
					
					dp[i][j] = Integer.MAX_VALUE;
					
				}
			}
			dp[0][0] = 0;
			long[][] next = new long[m + 1][k];
			for(int p=0; p<n; p++) { 
				
				for (int i = 0; i <= m; i++) {
				    for (int j = 0; j < k; j++) {
				        next[i][j] = Integer.MAX_VALUE;
				    }
				}
				for(int i=0;i<=m; i++) {
					for(int j=0; j<k; j++) {
						if(dp[i][j] == Integer.MAX_VALUE) { 
							continue;
						}
						
						long score = dp[i][j];
						
						//이번 문제 틀리는 경우 
						
						next[i][0] = Math.min(next[i][0], score);
						//이번 문제를 맞추는 경우 
						if(i<m) { //아직 목표한 값까지 못맞추었다면
							if(j+1 < k) { //이번 문제 맞춰도 아직 연속 정답 k가 아닌 경우
								
								long nextScore = score + 1;
								next[i+1][j+1] = Math.min(next[i+1][j+1], nextScore);
								
							} else {
								
								long nextScore = (score + 1) * 2;
								
								next[i+1][0] = Math.min(next[i+1][0], nextScore);
								//System.out.println(dp[i+1][j+1][0]);
							
								
							}
									
						}
						
					}
				}
				long[][] temp = dp;
				dp = next;
				next = temp;
			}
			
			long answer = Integer.MAX_VALUE;
			
			for (int l = 0; l < k; l++) {
			    answer = Math.min(answer, dp[m][l]);
			}

			System.out.println("#" + test_case + " " + answer);
			/////////////////////////////////////////////////////////////////////////////////////////////

		}
	}
}
