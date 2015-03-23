import java.util.*;
import java.lang.*;
import java.io.*;
 
/* Name of the class has to be "Main" only if the class is public. */
class Euclid
{
	//Division Stuff
	public static long lcm (long a, long b)
	{
		return a * b / gcd(a, b);
	}
 
	public static long gcd (long a, long b)
	{
		if (a % b == 0 || b % a == 0)
		{
			return Math.min(a, b);
		}
		else
		{
			long newNum = Math.max(a, b) - (long)(Math.max(a, b) / Math.min(a, b)) * Math.min(a, b);
			return gcd(newNum, Math.min(a, b));
		}
	}
 
	public static long[] linearCombo (long a, long b)
	{
		if (a - b == gcd(a, b))
		{
			long[] combo = {a, b};
    		return combo; 
		}
		long rem1 = Math.max(a, b);
		long rem2 = Math.min(a, b);
		long firstCoef1 = 1;
		long firstCoef2 = 0;
		long secondCoef1 = 0;
		long secondCoef2 = 1;
		while (rem1 % rem2 != 0)
		{
			long divisor = (long)(rem1 / rem2);
			long tempRem = rem1 - divisor * rem2;
			long tempFirstCoef = firstCoef1 - divisor * firstCoef2;
			long tempSecondCoef = secondCoef1 - divisor * secondCoef2;
			rem1 = rem2;
			rem2 = tempRem;
			firstCoef1 = firstCoef2;
			firstCoef2 = tempFirstCoef;
			secondCoef1 = secondCoef2;
			secondCoef2 = tempSecondCoef;
		}
		if (a > b)
		{
			long[] answer = {firstCoef2, secondCoef2};
			System.out.println(a + "(" + answer[0] + ")" + b + "(" + answer[1] + ") = " + gcd(a, b));
			return answer; 
		}
		else
		{
			long[] answer = {secondCoef2, firstCoef2};
			System.out.println(a + "(" + answer[0] + ") + " + b + "(" + answer[1] + ") = " + gcd(a, b));
			return answer; 
		}
	}
 
	public static int[] modInverse(int[] congruence)
	{
		int a = 1;
		while ((congruence[0] * a) % congruence[2] != congruence[1])
		{
			a++;
		}
		int[] arr = {1, a, congruence[2]};
		return arr;
	}
 
	public static HashSet<Integer> incongruentSols (long a, long b, long c)
	{
		HashSet solutions = new HashSet<Integer>();
		if (b % gcd(a, c) == 0)
		{
			long numSols = gcd(a, c);
			long sol = (c + b * linearCombo(a, c)[0] / numSols) % c;
			for (int i = 0; i < numSols; i++)
			{
				solutions.add((sol + c * i / numSols) % c);	
			}
		}
		return solutions;
	}
 
	public static void main (String[] args) throws java.lang.Exception
	{
    // your code goes here
	}
}
