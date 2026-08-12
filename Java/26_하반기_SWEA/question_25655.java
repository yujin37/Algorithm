package study;

import java.util.Arrays;
import java.util.Scanner;

public class question_25655 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		for(int test_case=1; test_case <= T; test_case++) {
			int n=sc.nextInt();
			String result ="";
			while(n>0) {
				if(n==1) {
					result += "4";
					n-=1;
				} else {
					result += "8";
					n-=2;
				}
			}
			if(result.equals("4")) {
				result = "0";
			}
			char[] result_char = result.toCharArray();
			Arrays.sort(result_char);
			System.out.println(result_char);
			
		}
	}

}
