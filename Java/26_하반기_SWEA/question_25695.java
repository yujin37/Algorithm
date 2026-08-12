package study;

import java.util.Scanner;

public class question_25695 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int test_case=1; test_case <= T; test_case++) {
			int x=sc.nextInt();
			int y=sc.nextInt();
			int z=sc.nextInt();
			
			int a=-1, b=-1, c=-1;
			if(y==z && z>=x) {
				c=y;
				a=x;
				b=x;
			}
			if(x==y && y>=z) {
				b=x;
				a=z;
				c=z;
			}
			if(x==z && z>=y) {
				a=x;
				b=y;
				c=y;
			}
			
			System.out.println(a+ " " + b + " " + c);
		}
	}
}
