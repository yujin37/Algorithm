package study;

import java.util.Scanner;

public class question_25672 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		for(int test_case=1; test_case<=T; test_case++) {
			int n = sc.nextInt();
			int k = sc.nextInt();
			
			int[] nums = new int[n];
			for(int i=0; i<n; i++) {
				nums[i] = sc.nextInt();
			}
			
			//초기값 설정
			int left = 0;
			
		
			int totalMax = Integer.MIN_VALUE;
			int cnt = 0;
			for(int i=0; i<n-k; i++) {
				left = left + nums[i];
				cnt++;
				if(cnt>=k) {
					int cnt2=0;
					int right = 0;
					for(int j=i+1; j<n;j++) {
						right = right + nums[j];
						cnt2++;
						if(cnt2 >=k) {
							//System.out.println(left + right);
							
							
							if(totalMax < (left + right)) {
								totalMax = left + right;
							}
							right = right - nums[j-k+1];
						}
						
						
					}
					left = left - nums[i-k+1];
				}
				
				
			}
			System.out.println("#" + test_case + " " + totalMax);

			
			
			
		}
	}
}
