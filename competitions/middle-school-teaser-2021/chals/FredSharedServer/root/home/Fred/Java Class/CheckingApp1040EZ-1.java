package estep10;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.NoSuchElementException;
import java.util.Scanner;

public class CheckingApp1040EZ {

	public static void main(String[] args) {
		// initialize all input lines as -1. If a line is not = -1, then it has been
		// changed
		int line1 = -1;
		int line2 = -1;
		int line3 = -1;
		int line5A = -1; // input 0 or 1 --> number that can be claimed as dependents
		int line7 = -1;
		int line10 = -1; // this can be calculated, but you may ask the user to look it up in the table
							// (your choice)

		// if args contains the name of a file, fill the input variables from the file
		if (args.length > 0) {
			Scanner inputFile = null;
			try {
				inputFile = new Scanner(new File(args[0]));
			} catch (FileNotFoundException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
				System.out.println("\nA file name has been detected, but that file does not exist.");
				System.exit(1);
			}
			try {
				line1 = inputFile.nextInt();
				line2 = inputFile.nextInt();
				line3 = inputFile.nextInt();
				line5A = inputFile.nextInt();
				line7 = inputFile.nextInt();
				line10 = inputFile.nextInt();
			} catch (NoSuchElementException e) {
				e.printStackTrace();
				System.out
						.println("\nA file has been detected and read, but the contents are not formatted correctly.");
				System.exit(2);
			}
		}
		// ****************************************************************************************************************
		// Student code starts below this point
		// NOTE: Do not change the value of any of the line variables above if they are
		// not -1 - the value has come from file
		// In other words, instead of just writing
		// line1 = kb.nextInt();
		// you need to write:
		// if(line1 == -1){
		// line1 = kb.nextInt();
		// }
		// *****************************************************************************************************************
		/**
		 * Requirements: Check back daily for updates on the assignment page. 1. All
		 * calculations MUST occur in a method (no matter how small) 2. All user input
		 * must be verified as acceptable 3. ...see assignment page for updates
		 */

		// Line 1
		System.out.println("Line 1:");
		if (line1 == -1) {
			line1 = valid();
		}

		// Line 2
		System.out
				.println("                                            ***                                            ");
		System.out.println("Line 2: ");
		if (line2 == -1) {
			line2 = L2();
		}

		// Line 3
		System.out
				.println("                                            ***                                            ");
		System.out.println("Line 3: ");
		if (line3 == -1) {
			line3 = valid();
		}

		// Line 4
		System.out
				.println("                                            ***                                            ");
		int line4 = L4(line1, line2, line3);

		// Line 5 - Input
		System.out
				.println("                                            ***                                            ");
		System.out.println("Line 5: ");
		if (line5A == -1) {
			line5A = L51();
		}

		// Line 5
		int line5 = L5C(line5A, line1);

		// Line 6
		System.out
				.println("                                            ***                                            ");
		int line6 = L6(line4, line5A);

		// Line 7
		System.out
				.println("                                            ***                                            ");
		System.out.println("Line 7: ");
		if (line7 == -1) {
			line7 = valid();
		}

		// Line 9
		System.out
				.println("                                            ***                                            ");
		int line9 = L9(line7);

		// Line 10
		System.out.println("");
		System.out.println(
				"Please now enter your input for Line 10 - Tax based on the Tax Table for the amount from Line 6: ");
		System.out.println("Your taxable income - Line 6 - is: $" + line6);
		if (line10 == -1) {
			line10 = valid();
		}

		// Line 12
		int line12 = L12(line10);

		// Line 13
		int line13 = L13(line9, line12);

		// Line 14
		int line14 = L14(line9, line12);

		// Printing of Final Results
		System.out.println("");
		System.out.println("Results: ");
		System.out.println("");

		System.out.println("Line 1 - Wages, Salaries, and Tips: $" + line1);
		System.out.println("Line 2 - Taxable Interest: $" + line2);
		System.out.println("Line 3 - Unemployment Compensation & Alaska Permanent Fund Dividends: $" + line3);
		System.out.println("Line 4 - Adjusted Gross Income: $" + line4);
		System.out.println("Line 5 - Dependent Status: $" + line5);
		System.out.println("Line 6 - Taxable Income: $" + line6);
		System.out.println("Line 7 - Income Tax Withheld: $" + line7);
		System.out.println("Line 8 - Earned Income Credit: $0");
		System.out.println("Line 9 - Total Payments and Credits: $" + line9);
		System.out.println("Line 10 - Tax: $" + line10);
		System.out.println("Line 11 - Health Care Individual Responsibility: $0");
		System.out.println("Line 12 - Total Tax: $" + line12);
		System.out.println("Line 13 - Amount: $" + line13);
		System.out.println("Line 14 - Amount Owed: $" + line14);

	}

	// Input Validation - making sure that what they have entered is an integer
	public static int valid() {
		boolean test1 = true;
		int line = 0;
		while (test1) {
			Scanner kb1 = new Scanner(System.in);
			try {
				line = kb1.nextInt();
				test1 = false;
			} catch (Exception InputMismatchException) {
				System.out.println("You entered non-numerical data.  Please try again:");
			}
		}
		return line;
	}

	// Line 2 - User Input
	public static int L2() {
		int line2 = valid();
		if (line2 > 1500) {
			System.out.println("You have entered a value above $1500 for Line 2 - Taxable Interest.");
			System.exit(2);
		}

		return line2;

	}

	// Line 4 - Calculation
	public static int L4(int line1, int line2, int line3) {
		return line1 + line2 + line3;
	}

	// Line 5 - User Input
	public static int L51() {
		int line5A = valid();
		boolean test;
		if (line5A == 0 || line5A == 1) {
			test = false;
		} else {
			test = true;
		}
		while (test) {//In case if people continue to not input the right integers
			if (line5A != 0 || line5A != 1) {
				Scanner kb5 = new Scanner(System.in);
				System.out.println("You entered a value that is neither '0' nor '1' - please try again: ");
				try {
					line5A = kb5.nextInt();
					test = false;
				} catch (Exception InputMismatchException) {
					System.out.println("You entered non-numerical data.  Please try again:");
				}
			}
			if (line5A == 0 || line5A == 1) {
				break;
			}
		}
		return line5A;
	}

	// Line 5 - Calculation 1
	public static int L5C(int line5A, int line1) {
		if (line5A == 0) {
			line5A = 10400;
		} else {
			line5A = L5C2(line1);
		}
		return line5A;
	}

	// Line 5 - Calculation 2
	public static int L5C2(int line5A) {
		line5A = line5A + 350;
		int line5B = 1050;
		int line5C = Math.max(line5A, line5B);
		int line5D = 6350;
		int line5E = Math.min(line5C, line5D);
		int line5F = 0;
		int line5G = line5E + line5F;
		return line5G;

	}

	// Line 6 - Calculation
	public static int L6(int line4, int line5) {
		int line6 = line4 - line5;
		if (line6 < 0) {
			line6 = 0;
		}
		if (line6 > 100000) {
			System.out.println("Invalid. \nYour Taxable Income - Line 6 - is greater than $100,000.  ");
			System.exit(2);
		}
		return line6;
	}

	// Line 9 - Calculation
	public static int L9(int line7) {
		int line9 = line7;
		return line9;

	}

	// Line 12 - Calculation
	public static int L12(int line10) {
		int line12 = line10;
		return line12;
	}

	// Line 13 - Calculations
	public static int L13(int line9, int line12) {
		int line13 = 0;
		if (line9 > line12) {
			line13 = line9 - line12;
		} else {
			line13 = 0;
		}
		return line13;
	}

	// Line 14 - Calculations
	public static int L14(int line9, int line12) {
		int line14 = 0;
		if (line12 > line9) {
			line14 = line12 - line9;
		} else {
			line14 = 0;
		}
		return line14;
	}
}
