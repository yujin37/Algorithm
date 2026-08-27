package study;

import java.util.Scanner;

public class question_14510 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		
		for(int test_case=1; test_case<=T; test_case++) {
			int n = sc.nextInt();
			int[] trees = new int[n];
			int[][] left = new int[n][2];
			
			int maxTree = -1;
			for(int i=0; i<n; i++) {
				trees[i] = sc.nextInt();
				if(maxTree < trees[i]) {
					maxTree = trees[i];
				}
				
			}
			int num1=0; 
			int num2=0;
			for(int i=0;i<n; i++) {
				left[i][0] = (maxTree-trees[i])/2;
				left[i][1] = (maxTree-trees[i])%2;
				
				num2 = num2+ left[i][0];
				num1 = num1 + left[i][1];
			}
			int mindate = Math.max(2 * num2, 2 * num1 - 1);
			
			for(int i=num2; i>=0; i--) {
				num2-=1;
				num1+=2;
				int now = Math.max(2 * num2, 2 * num1 - 1);
				mindate = Math.min(mindate, now);
			}	
			System.out.println("#" + test_case + " " + mindate);
			//System.out.println(num2 + " " +  num1);
		}
	}
}
