using System;

public class Program {
	public static int[] SmallestDifference(int[] arrayOne, int[] arrayTwo) {
		Array.sort(arrayOne);
		Array.sort(arrayTwo);
		int idxOne = 0;
		int idxTwo = 0;
		int smallest = Int32.MaxValue;
		int current = Int32.MaxValue;
		int[] smallestPair = new int[2];
		while(idxOne < arrayOne.length && idxTwo < arrayTwo.Length){
    	int firstNum = arrayOne[idxOne];
			int secondNum = arrayTwo[idxTwo];
			if(firstNum < secondNum){
				current = secondNum - firstNum;
				idxTwo++;
			} else if (secondNum < firstNum) {
				current = firstNum - secondNum;
				idxTwo++;
			} else{
				return new int[] {firstNum, scondNum};
			}
     	if (smallest > current){
				smallest = current;
				smallestPair = new int[] {firstNum, secondNum};
			}
			
		}
		return smallestPair;
	}
}