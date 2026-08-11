import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class question_26389 {
	public static void main(String args[]) throws Exception
	{
		
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();
		
		for(int test_case = 1; test_case <= T; test_case++)
		{
		
			/////////////////////////////////////////////////////////////////////////////////////////////
			char[] trip = sc.next().toCharArray();
			List<Character> content = new ArrayList<>();
			int[] count = {0,0,0,0};
			for(int i=0; i<trip.length; i++) {
				if(trip[i] == 'E') {
					count[0] += 1;
				} else if(trip[i] == 'W') {
					count[1] += 1;
				} else if(trip[i] == 'S') {
					count[2] += 1;
				} else if(trip[i] == 'N') {
					count[3] += 1;
				}
			}

			boolean result = true;
			if(count[0] >0 && count[1] == 0) {
				result = false;
			} else if(count[1] >0 && count[0] == 0) {
				result = false;
			}
			
			if(count[2] >0 && count[3] == 0) {
				result = false;
			} else if(count[3] >0 && count[2] == 0) {
				result = false;
			}
			
			if(result) {
				System.out.println("Yes");
			} else {
				System.out.println("No");
			}

			/////////////////////////////////////////////////////////////////////////////////////////////

		}
	}
}
